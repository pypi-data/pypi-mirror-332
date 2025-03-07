import math
import sys
from typing import Dict, List, cast
from collections import Counter
import copy
from itertools import chain

from bamboo.lang.ir import (
    Expr,
    IRCallable,
    IRSpace,
    IRTransformer,
    IRVisitor,
    IRPrinter,
    Var,
)
from bamboo.lang.ir.stat import ForStat, AssignStat, IfStat, Stat
from bamboo.lang.ir.expr import (
    FieldExpr,
    BinExpr,
    UniExpr,
    IntExpr,
    AttrExpr,
    CallExpr,
    IRFunc,
    IRStub,
)
from bamboo.lang.dtype import FieldInfo, ShapedFieldInfo, HybridT

from bamboo.optim.trans import ParForStat
from bamboo.optim.proc import OptForStat, FieldVarInfo, VarInfo
from bamboo.optim.proc.partition import (
    ProcessPartition,
    PartitionConfiguration,
    ProcessTile,
)
from bamboo.optim.proc.helper import IsConstField, GetIdx, DTypeToStr, CutFuncName

from bamboo.configuration import GlobalConfiguration as gc


# 将parafor变为OptFor，为其添加输入输出field信息
class OptForTransformer(IRTransformer):
    ProcPartition: PartitionConfiguration
    AllInvolvedList: List[List[int]]
    FieldHaloRange: Dict[int, List]
    FieldGH: Dict[int, bool]
    GlobalConst: List[FieldVarInfo]
    Complexity: int
    UseGlobalHalo: bool = False

    def visit_ParForStat(self, ctx: IRCallable, ir: ParForStat):
        """_summary_

        Args:
            ctx (IRCallable): _description_
            ir (ParForStat): _description_
            asdasdsadasda

            asdas
        """

        def FindField(ir: Expr):
            if isinstance(ir, FieldExpr):
                infoid = id(ir.field.info.desc)

                print(
                    "Check const",
                    ir.field.local_name,
                    ir.field.info.desc.const,
                    IsConstField(ir),
                )

                if IsConstField(ir):
                    if not HasFieldInfo(infoid, ConstField):
                        ConstField.append(
                            FieldVarInfo(
                                infoid,
                                ir.field.local_name,
                                DTypeToStr(ir.field.info.dtype),
                                ir.field.info.shape,
                                ir.field.info.desc.pos,
                                False,
                                False,
                            )
                        )
                    if not HasFieldInfo(infoid, self.GlobalConst):
                        self.GlobalConst.append(ConstField[-1])
                else:
                    if not HasFieldInfo(infoid, FieldIn):
                        CheckFieldHalo(
                            infoid,
                            ir.field.local_name,
                            DTypeToStr(ir.field.dtype),
                            ir.field.info.shape,
                            ir.field.info.desc.pos,
                            0,
                        )

                    for expr in ir.idx:
                        pos, gh = GetIdx(expr, VarDeclare)
                        if pos == 0:
                            RangeSpace.append(False)
                        else:
                            RangeSpace.append(True)
            elif isinstance(ir, CallExpr):
                # self.Complexity = 2
                if isinstance(ir.symb, IRFunc) or isinstance(ir.symb, IRStub):
                    if CutFuncName(ir.symb.name) not in FuncCall:
                        FuncCall.append(CutFuncName(ir.symb.name))
                    for args in ir.args:
                        if isinstance(args, BinExpr):
                            FindField(args.lhs)
                            FindField(args.rhs)
                        elif isinstance(args, UniExpr):
                            FindField(args.rhs)
                        elif isinstance(args, FieldExpr):
                            infoid = id(args.field.info.desc)

                            if IsConstField(args):
                                if not HasFieldInfo(infoid, ConstField):
                                    ConstField.append(
                                        FieldVarInfo(
                                            infoid,
                                            args.field.local_name,
                                            DTypeToStr(args.field.info.dtype),
                                            args.field.info.shape,
                                            args.field.info.desc.pos,
                                            False,
                                        )
                                    )
                                if not HasFieldInfo(infoid, self.GlobalConst):
                                    self.GlobalConst.append(ConstField[-1])
                            else:
                                if not HasFieldInfo(infoid, FieldIn):
                                    CheckFieldHalo(
                                        infoid,
                                        args.field.local_name,
                                        DTypeToStr(args.field.info.dtype),
                                        args.field.info.shape,
                                        args.field.info.desc.pos,
                                        0,
                                    )
                                    # FieldIn.append(FieldVarInfo(infoid,args.field.local_name,DTypeToStr(args.field.info.dtype),args.field.info.shape,args.field.info.desc.pos,True))

                                for expr in args.idx:
                                    pos, gh = GetIdx(expr, VarDeclare)
                                    if pos == 0:
                                        RangeSpace.append(False)
                                    else:
                                        RangeSpace.append(True)
                        else:
                            pass
            elif isinstance(ir, BinExpr):
                FindField(ir.lhs)
                FindField(ir.rhs)
            elif isinstance(ir, UniExpr):
                FindField(ir.rhs)

        def HasFieldInfo(fieldid: int, FieldList: List[FieldVarInfo]):
            for info in FieldList:
                if info.id == fieldid:
                    return True

            return False

        def CheckFieldHalo(fieldid: int, name: str, DType: str, shape, pos, fieldflag):
            FieldInfo = FieldVarInfo(fieldid, name, DType, shape, pos, False, False)

            if fieldid in self.FieldHaloRange:
                for i in range(0, 4):
                    if self.FieldHaloRange[fieldid][i] != 0:
                        FieldInfo.HaloOrient.append(True)
                    else:
                        FieldInfo.HaloOrient.append(False)
                flag: bool = False

                for x in FieldInfo.HaloOrient:
                    flag |= x

                FieldInfo.UpdateHalo = flag

            if fieldflag == 1:
                FieldOut.append(FieldInfo)
            else:
                FieldIn.append(FieldInfo)

        def ProcInvolved_OneLine(pos: int):
            for ProcessTile in self.ProcPartition.TileProcList:
                if pos in range(ProcessTile.range[0], ProcessTile.range[1] + 1):
                    ProcInvolved.append(ProcessTile.id)

        def AddVarDeclare(var: Var):
            newVar = True
            for varD in VarDeclare:
                if varD.name == var.name:
                    newVar = False
                    break
            if newVar:
                if isinstance(var.dtype, HybridT):
                    VarDeclare.append(VarInfo(var.name, DTypeToStr(var.dtype.name), True))
                else:
                    VarDeclare.append(VarInfo(var.name, DTypeToStr(var.dtype)))

        # 循环范围左闭右开
        def ProcInvolved_Range(beg: int, end: int, all: bool = False):
            for ProcessTile in self.ProcPartition.TileProcList:
                # Tocheck 循环范围与进程范围相交
                if max(ProcessTile.range[0], beg) <= min(ProcessTile.range[1], end - 1) or all:
                    # if  ProcessTile.range[0] <= beg and beg <= ProcessTile.range[1] or all:
                    ProcInvolved.append(ProcessTile.id)

        def NewInvolvedList(Involved: List[int]):
            for list in self.AllInvolvedList:
                ta = Counter(list)
                tb = Counter(Involved)
                if ta == tb:
                    return
            self.AllInvolvedList.append(copy.deepcopy(Involved))

        def StencilSpace() -> str:
            # print("!@!@!@!@!@!@!@" + str(RangeSpace))

            if len(RangeSpace) == 0 or len(FieldOut) == 0:
                return "not"

            Space: List[bool] = [False, False, False]

            for i, flag in enumerate(RangeSpace):
                Space[i % 3] |= flag

            if Space[0] == False and Space[1] == False and Space[2] == False:
                return "o"

            if Space[0] == True and Space[1] == False and Space[2] == False:
                return "x"
            if Space[0] == False and Space[1] == True and Space[2] == False:
                return "y"
            if Space[0] == False and Space[1] == False and Space[2] == True:
                return "z"

            if Space[0] == True and Space[1] == True and Space[2] == False:
                return "xy"
            if Space[0] == True and Space[1] == False and Space[2] == True:
                return "xz"
            if Space[0] == False and Space[1] == True and Space[2] == True:
                return "yz"

            if Space[0] == True and Space[1] == True and Space[2] == True:
                return "xyz"

        def AnaylzeStat(stat: Stat):
            if isinstance(stat, AssignStat):
                # In
                FindField(stat.src)

                # Out & Involved
                dst = stat.dst
                if isinstance(dst, FieldExpr) and not IsConstField(dst):
                    infoid = id(dst.field.info.desc)
                    if not HasFieldInfo(infoid, FieldOut):
                        info = dst.field.info
                        CheckFieldHalo(
                            infoid,
                            dst.field.local_name,
                            DTypeToStr(dst.field.info.dtype),
                            dst.field.info.shape,
                            dst.field.info.desc.pos,
                            1,
                        )

                    # 检查j范围
                    # **默认已知gmcore只会产生不同纬度的负载不均衡
                    if ProcInvolved == []:
                        expr = dst.idx[1]
                        if isinstance(expr, IntExpr):
                            pos = expr.val
                            ProcInvolved_OneLine(pos)
                        elif isinstance(expr, AttrExpr):
                            var = expr.var
                            for parfor in original_ir.ranges:
                                if var == parfor.var:
                                    ProcInvolved_Range(parfor.begin, parfor.end, False)
                                    break
                elif isinstance(dst, FieldExpr) and IsConstField(dst):
                    if ProcInvolved == []:
                        ProcInvolved_Range(0, 0, True)
                elif isinstance(dst, AttrExpr):
                    AddVarDeclare(dst.var)
                    # print("Attr!!!" , dst, type(dst), dst.dtype, dst.var.name, dst.var.dtype)
            elif isinstance(stat, ForStat):
                # self.Complexity = 2
                self.UseGlobalHalo = True
                for_stat = cast(ForStat, stat)
                AddVarDeclare(for_stat.var)
                current_body = for_stat.body
                for innerstat in current_body:
                    AnaylzeStat(innerstat)
            elif isinstance(stat, IfStat):
                # self.Complexity = 3
                if_stat = cast(IfStat, stat)
                current_body = if_stat.body
                for innerstat in current_body:
                    AnaylzeStat(innerstat)

        FieldIn: List[FieldVarInfo] = []
        FieldOut: List[FieldVarInfo] = []
        ConstField: List[FieldVarInfo] = []
        FuncCall: List[str] = []
        VarDeclare: List[VarInfo] = []
        ProcInvolved: List[int] = []
        RangeSpace: List[bool] = []
        SpaceFlag: str

        self.UseGlobalHalo = False
        self.Complexity = 1

        original_ir = ir
        current_body = ir.body
        # while isinstance(current_body[0],ForStat):
        #     for_stat = cast(ForStat, current_body[0])
        #     current_body = for_stat.body
        #     self.Complexity = 2

        # while isinstance(current_body[0], IfStat):
        #     if_stat = cast(IfStat,current_body[0])
        #     current_body = if_stat.body
        #     self.Complexity = 2

        for stat in current_body:
            AnaylzeStat(stat)
            # if isinstance(stat,AssignStat):
            #     #In
            #     FindField(stat.src)

            #     #Out & Involved
            #     dst = stat.dst
            #     if isinstance(dst,FieldExpr) and not IsConstField(dst):
            #         infoid = id(dst.field.info)
            #         if not HasFieldInfo(infoid,FieldOut):
            #             info = dst.field.info
            #             CheckOutHalo(infoid, dst.field.local_name, DTypeToStr(dst.field.info.dtype),dst.field.info.shape,dst.field.info.desc.pos )

            #         #检查j范围
            #         #**默认已知gmcore只会产生不同纬度的负载不均衡
            #         if ProcInvolved == []:
            #             expr = dst.idx[1]
            #             if isinstance(expr,IntExpr):
            #                 pos = expr.val
            #                 ProcInvolved_OneLine(pos)
            #             elif isinstance(expr,AttrExpr):
            #                 var = expr.var
            #                 for parfor in original_ir.ranges:
            #                     if var == parfor.var:
            #                         ProcInvolved_Range(parfor.begin,parfor.end,False)
            #                         break
            #     elif isinstance(dst,FieldExpr) and IsConstField(dst):
            #         if ProcInvolved == []:
            #             ProcInvolved_Range(0,0,True)

        SpaceFlag = StencilSpace()

        FuncName = CutFuncName(ir.ranges[0].var.prefix)

        # ToCheck 2d space stencil
        # if (len(ir.ranges)!=3):
        #     self.Complexity = 2
        # for field in FieldOut:
        #     if field.shape[2] == 1:
        #         self.Complexity = 2
        if ir.ranges[0].var.prefix.find("Init") != -1:
            self.Complexity = 2

        for field in ConstField:
            if field.shape[2] != 1 and (field.shape[0] != 1 or field.shape[1] != 1):
                self.Complexity = 2
        # if SpaceFlag not in ["o","x","y","xy","z","xz"]:
        if SpaceFlag not in ["o", "x", "y", "xy", "z", "xz"]:
            self.Complexity = 2
        # hflx_ppm_inner
        # if FuncName in ["hflx_ppm_outer"]:
        #     if self.UseGlobalHalo:
        #         self.Complexity = 2

        # if SpaceFlag == 'x' and self.UseGlobalHalo:
        #     print("CHECK X GLOBAL",FuncName)
        # if FuncName in ["vflx_ppm","calc_we_lev",]:
        #     self.Complexity = 2
        if SpaceFlag in ["z", "xz"]:
            # if self.UseGlobalHalo:
            #     self.Complexity = 2
            if ir.ranges[0].end - ir.ranges[1].begin < gc.Grid.NumLev / 2:
                self.Complexity = 2

            # To Remember 如debug需要,可以在此开放优化白名单,逐一检查
            # if FuncName not in ["calc_ph","calc_m","calc_wedudlev_wedvdlev","calc_grad_ptf","pgf_lin97","vflx_ppm","calc_gz_lev","calc_we_lev"]:
            # if FuncName not in []:
            #     self.Complexity = 2

        # if FuncName.find("SetBoundaryZ")!= -1:
        #     print("Check ir!!!")
        #     print(ir.ranges)

        if len(ir.ranges) == 3:
            if (
                ir.ranges[1].end - ir.ranges[1].begin == 1
                and ir.ranges[0].end - ir.ranges[0].begin == 1
            ):
                self.Complexity = 2

        if FuncName.find("prepare") != -1:
            self.Complexity = 2

        for field in FieldOut:
            if field.id in self.FieldGH:
                field.UpdateHaloGlobal = self.FieldGH[field.id]
            else:
                # ToRemember
                pass

        NewInvolvedList(ProcInvolved)
        OptFor = OptForStat(
            original_ir.lineno,
            original_ir.ranges,
            original_ir.body,
            FieldIn,
            FieldOut,
            ConstField,
            ProcInvolved,
            FuncCall,
            VarDeclare,
            SpaceFlag,
            self.Complexity,
            self.UseGlobalHalo,
        )
        # if self.UseGlobalHalo:
        #     setattr(OptFor,"Use",True)

        printer = IRPrinter()
        OptFor.print(printer)
        print(printer)

        return OptFor

    def __call__(
        self,
        ctx: IRCallable,
        FieldHaloRange: Dict[int, List],
        FieldGH: Dict[int, bool],
        ProcPartition: PartitionConfiguration,
    ):
        if isinstance(ctx, IRSpace):
            self.ProcPartition = ProcPartition
            self.FieldHaloRange = FieldHaloRange
            self.FieldGH = FieldGH
            self.AllInvolvedList = []
            self.GlobalConst = []
            self.UseGlobalHalo = False
            super().__call__(ctx)
            return self.AllInvolvedList, self.GlobalConst
