from typing import Dict, List, cast, Set
from bamboo.lang.dtype import FieldInfo
from bamboo.lang.ir import Expr, IRCallable, IRVisitor, IRPrinter
from bamboo.lang.ir.expr import (
    FieldExpr,
    AttrExpr,
    BinExpr,
    UniExpr,
    BinOp,
    CallExpr,
    IRFunc,
    IRStub,
    IRExternFunc,
    FieldT,
)
from bamboo.lang.ir.stat import AssignStat
from bamboo.optim.trans.parallel import constexpr
from bamboo.optim.proc.helper import IsConstField, GetIdx


# 分析所有AssignStat,给出各Field的halo大小
class HaloAnalyzer(IRVisitor):
    HaloDict: Dict[int, List] = {}
    HaloGlobal: Dict[int, bool] = {}
    ExternList: Set[str] = set()

    def AnalyzeField(self, ir: FieldExpr):
        halo: List = []
        if IsConstField(ir):
            return
        # print(ir)
        # print(ir.field.info)
        # print(id(ir.field.info))
        # print(ir.field.local_name)
        for expr in ir.idx:
            pos, gh = GetIdx(expr)

            if pos >= 0:
                halo.append(0)
                halo.append(pos)
            else:
                halo.append(pos)
                halo.append(0)

            if id(ir.field.info.desc) in self.HaloGlobal:
                self.HaloGlobal[id(ir.field.info.desc)] = (
                    self.HaloGlobal[id(ir.field.info.desc)] | gh
                )
            else:
                self.HaloGlobal[id(ir.field.info.desc)] = gh

        if id(ir.field.info.desc) in self.HaloDict:
            for i in range(0, 6):
                if i & 1:
                    self.HaloDict[id(ir.field.info.desc)][i] = max(
                        self.HaloDict[id(ir.field.info.desc)][i], halo[i]
                    )
                else:
                    self.HaloDict[id(ir.field.info.desc)][i] = min(
                        self.HaloDict[id(ir.field.info.desc)][i], halo[i]
                    )
        else:
            self.HaloDict[id(ir.field.info.desc)] = halo

    def FindField(self, ir: Expr):
        if isinstance(ir, FieldExpr):
            self.AnalyzeField(ir)
        elif isinstance(ir, UniExpr):
            self.FindField(ir.rhs)
        elif isinstance(ir, BinExpr):
            self.FindField(ir.lhs)
            self.FindField(ir.rhs)
        elif isinstance(ir, CallExpr):
            if isinstance(ir.symb, IRFunc) or isinstance(ir.symb, IRStub):
                for args in ir.args:
                    if isinstance(args, BinExpr):
                        self.FindField(args.lhs)
                        self.FindField(args.rhs)
                    elif isinstance(args, UniExpr):
                        self.FindField(args.rhs)
                    elif isinstance(args, FieldExpr):
                        self.AnalyzeField(args)
                    else:
                        pass
        else:
            pass

    def visit_AssignStat(self, ctx: IRCallable, ir: AssignStat):
        # printer = IRPrinter()
        # ir.print(printer)
        # print(printer)
        # print("assignstat" + "*" *20)
        # print(ir)
        # print("*" * 20)
        self.FindField(ir.src)

    def visit_CallExpr(self, ctx: IRCallable, ir: CallExpr):
        halo: List = [-1, 1, -1, 1, 0, 0]

        # update for ExternLib call
        if isinstance(ir.symb, IRExternFunc):
            if ir.symb.name != "":
                self.ExternList.add(ir.symb.name)
            for item in ir.args:
                if isinstance(item, FieldT):
                    if id(item.info.desc) in self.HaloDict:
                        for i in range(0, 6):
                            if i & 1:
                                self.HaloDict[id(item.info.desc)][i] = max(
                                    self.HaloDict[id(item.info.desc)][i], halo[i]
                                )
                            else:
                                self.HaloDict[id(item.info.desc)][i] = min(
                                    self.HaloDict[id(item.info.desc)][i], halo[i]
                                )
                    else:
                        self.HaloDict[id(item.info.desc)] = halo

                    # 外部库中有计算才设置halo为最大
                    if ir.symb.avg_flops != 0:
                        self.HaloGlobal[id(item.info.desc)] = True
                    print(
                        "Check LibCall GH",
                        ir.symb.name,
                        ir.symb.avg_flops,
                        item.local_name,
                    )
                    # if id(item.info.desc) in self.HaloGlobal:
                    #     self.HaloGlobal[id(item.info.desc)] = True
                    # else:
                    #     self.HaloGlobal[id(item.info.desc)] = True

    def __call__(self, ctx: IRCallable) -> Dict[FieldInfo, List]:
        self.HaloDict = {}
        super().__call__(ctx)

        # print("$"*20)
        # print(self.HaloDict)
        # print("$"*20)

        return self.HaloDict, self.HaloGlobal, self.ExternList
