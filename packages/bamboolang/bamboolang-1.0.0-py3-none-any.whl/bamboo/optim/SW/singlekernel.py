import math
import copy
from typing import Dict, List, cast, Tuple
from itertools import chain

from bamboo.lang.ir import Expr, IRCallable, IRSpace, IRTransformer, IRVisitor, IRPrinter
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
from bamboo.lang.dtype import (
    VoidT,
    IntT,
    FloatT,
    FieldT,
    HybridFieldT,
    HybridT,
    ShapedFieldInfo,
)

from bamboo.optim.proc import OptForStat, FieldVarInfo, VarInfo
from bamboo.optim.proc.helper import IsConstField, GetIdx, DTypeToStr

from bamboo.optim.SW import SWOptForStat
from bamboo.optim.SW.helper import GetSpace, Sizeof, CutFieldName

from bamboo.configuration import GlobalConfiguration as gc


class SWOptForTransformerSingle(IRTransformer):
    ProcDomain: Tuple[int, int, int]
    FieldHaloRange: Dict[str, List]
    ProcHaloRange: List[int]

    def visit_OptForStat(self, ctx: IRCallable, ir: OptForStat):
        mapping: List[int] = []
        blocking: List[int] = []
        FieldList: List[FieldVarInfo] = []
        VarList: List[VarInfo] = []

        # pos 0 lhs 1 rhs
        def UpDateID(name: str, id: int, pos: int):
            AddField = True
            for field in chain(SWOPTFor.FieldIn, SWOPTFor.FieldOut, SWOPTFor.ConstField):
                if field.name == name:
                    field.id = id
                    AddField = False

            if AddField:
                for field in chain(SWOPTFor.FieldIn, SWOPTFor.FieldOut):
                    if field.id == id and field.name != name:
                        newField = copy.deepcopy(field)
                        newField.name = name
                        if pos == 0:
                            SWOPTFor.FieldOut.append(newField)
                        else:
                            SWOPTFor.FieldIn.append(newField)

        # def HybridInfoCollect(self, dd: HybridT):
        #     sname = dd.name
        #     sCode = 'struct ' + sname + '{\n'
        #     sList = []
        #     for item in dd.items:
        #         sCode = sCode + self._indent * ' ' + self.GetType(item[1]) + ' ' + item[0] + ';\n'
        #         sList.append((self.GetType(item[1]), item[0]))
        #         if isinstance(item[1], HybridT):
        #             self.HybridInfoCollect(item[1])
        #     sCode = sCode + '};\n'
        #     if not sname in self.fieldCode:
        #         self.fieldCode[sname] = sCode
        #         self.fieldList[sname] = []
        #         for item in sList:
        #             self.fieldList[sname].append(item)
        #         self.fieldOrder.append(sname)

        def FindField(ir: Expr):
            # ToRemeber AddFuncCall
            if isinstance(ir, FieldExpr):
                infoid = id(ir.field.info.desc)
                UpDateID(ir.field.local_name, infoid, 1)
            elif isinstance(ir, UniExpr):
                FindField(ir.rhs)
            elif isinstance(ir, BinExpr):
                FindField(ir.lhs)
                FindField(ir.rhs)
            elif isinstance(ir, AttrExpr):
                vname = ir.var.name
                dtype = ir.var.dtype
                newReadVar = True
                for var in SWOPTFor.VarDeclare:
                    if var.name == ir.var.name:
                        newReadVar = False
                        break
                if newReadVar:
                    if isinstance(ir.var.dtype, HybridT):
                        print(ir, ir.attrs)
                        vname = vname + "->" + ir.attrs[0]
                        dd = cast(HybridT, ir.var.dtype)
                        for x in dd.items:
                            if x[0] == CutFieldName(vname):
                                dtype = x[1]
                                break
                    for vi in VarList:
                        if vi.name == vname:
                            return
                    VarList.append(VarInfo(vname, DTypeToStr(dtype)))
            elif isinstance(ir, CallExpr):
                if isinstance(ir.symb, IRFunc) or isinstance(ir.symb, IRStub):
                    for args in ir.args:
                        if isinstance(args, BinExpr):
                            FindField(args.lhs)
                            FindField(args.rhs)
                        elif isinstance(args, UniExpr):
                            FindField(args.rhs)
                        elif isinstance(args, FieldExpr):
                            infoid = id(args.field.info.desc)
                            UpDateID(args.field.local_name, infoid, 1)
                else:
                    pass
            else:
                pass

        def UpdateStat(stat: Stat):
            if isinstance(stat, AssignStat):
                # right
                FindField(stat.src)
                # left
                dst = stat.dst
                # print("Check UpdateStat LHS",dst,type(dst))
                if isinstance(dst, FieldExpr):
                    UpDateID(dst.field.local_name, id(dst.field.info.desc), 0)
                # if isinstance(dst,FieldExpr):
                #     UpDateID(dst.field.local_name, id(dst.field.info.desc))
            elif isinstance(stat, ForStat):
                for_stat = cast(ForStat, stat)
                current_body = for_stat.body
                for innerstat in current_body:
                    UpdateStat(innerstat)
            elif isinstance(stat, IfStat):
                if_stat = cast(IfStat, stat)
                current_body = if_stat.body
                for innerstat in current_body:
                    UpdateStat(innerstat)

        def UpDateFieldInfo():
            current_body = ir.body
            while isinstance(current_body[0], ForStat):
                for_stat = cast(ForStat, current_body[0])
                current_body = for_stat.body

            while isinstance(current_body[0], IfStat):
                if_stat = cast(IfStat, current_body[0])
                current_body = if_stat.body

            for stat in current_body:
                UpdateStat(stat)

        # 检查是否转换
        # 常量和单纯赋值不转换
        if (ir.StencilType) == "not":
            return ir

        # 从简单开始
        if (ir.Complexity) != 1:
            return ir

        # 生成默认SWOPT
        SWOPTFor = SWOptForStat(
            ir.lineno,
            ir.ranges,
            ir.body,
            ir.FieldIn,
            ir.FieldOut,
            ir.ConstField,
            ir.ProcInvolved,
            ir.FuncCall,
            ir.VarDeclare,
            ir.StencilType,
            ir.Complexity,
            ir.UseGlobalHalo,
            FieldList,
            VarList,
            2,
            mapping,
            blocking,
        )

        # IsUse = None
        # IsUse = getattr(ir,"Use", None)
        # if IsUse != None:
        #     SWOPTFor.UseGlobalHalo = True
        #     print("USE!!!!!!")
        #     print(SWOPTFor)

        if GetSpace(ir.StencilType) == 1:
            # 水平面计算
            # if not ir.UseGlobalHalo:

            if len(ir.ranges) == 3:
                mapping.append(1)
                mapping.append(2)
                mapping.append(32)
                blocking.append(256)
                blocking.append(8)
                blocking.append(1)

            else:
                mapping.append(1)
                mapping.append(4)
                mapping.append(1)
                blocking.append(128)
                blocking.append(8)
                blocking.append(1)

            # if (len(ir.ranges)) == 3:
            #     if ir.ranges[1].end - ir.ranges[1].begin == 1:
            #         mapping.append(1)
            #         mapping.append(1)
            #         mapping.append(64)
            #         blocking.append(256)
            #         blocking.append(1)
            #         blocking.append(1)

            # else:
            #     mapping.append(1)
            #     mapping.append(2)
            #     mapping.append(32)
            #     blocking.append(64)
            #     blocking.append(8)
            #     blocking.append(1)
        elif GetSpace(ir.StencilType) == 2:
            # 垂面计算
            if ir.UseGlobalHalo == False:
                mapping.append(1)
                mapping.append(8)
                mapping.append(8)
                blocking.append(256)
                blocking.append(1)
                blocking.append(4)
            else:
                mapping.append(8)
                mapping.append(8)
                mapping.append(1)
                blocking.append(64)
                blocking.append(1)
                blocking.append(32)

            # if (len(ir.ranges)) == 3:
            #     if ir.ranges[1].end - ir.ranges[1].begin == 1:
            #         mapping.append(1)
            #         mapping.append(1)
            #         mapping.append(32)
            #         blocking.append(256)
            #         blocking.append(1)
            #         blocking.append(2)

        # 多timeop复制后fieldinfo中的id信息尚未更新,而新的prochalorange是根据计算式重新更新的,此处需更新id信息，以在主核给入正确的halo信息
        UpDateFieldInfo()

        # 统计变量和大小
        VarNum = len(ir.FieldIn) + len(ir.FieldOut)
        ConstNum = len(ir.ConstField)

        if SWOPTFor.UseGlobalHalo:
            hx = self.ProcHaloRange[0]
            hy = self.ProcHaloRange[1]
            hz = self.ProcHaloRange[2]
        else:
            hx = 0
            hy = 0
            hz = 0
            for field in chain(ir.FieldIn, ir.FieldOut):
                if self.FieldHaloRange.__contains__(field.id):
                    hx = max(
                        hx,
                        max(
                            -self.FieldHaloRange[field.id][0],
                            self.FieldHaloRange[field.id][1],
                        ),
                    )
                    hy = max(
                        hy,
                        max(
                            -self.FieldHaloRange[field.id][2],
                            self.FieldHaloRange[field.id][3],
                        ),
                    )
                    hz = max(
                        hz,
                        max(
                            -self.FieldHaloRange[field.id][4],
                            self.FieldHaloRange[field.id][5],
                        ),
                    )

        VarSize = 0
        VarCount = 0
        ConstSize = 0
        for field in chain(ir.FieldIn, ir.FieldOut):
            VarSize += (blocking[0] + 2 * hx) * (blocking[1] + 2 * hy) * Sizeof(field.dtype)
            VarCount += 1
        # for field in ir.ConstField:
        #     ConstSize += (self.ProcDomain[0] + 2*hx) * (self.ProcDomain[1] + 2*hy) * (self.ProcDomain[2] + 2*hz) * Sizeof(field.dtype)
        print(
            "Check LDM B",
            hx,
            VarSize / 1024,
            VarCount,
            blocking[0],
            hx,
            blocking[1],
            hy,
            Sizeof(field.dtype),
            (blocking[0] + 2 * hx) * (blocking[1] + 2 * hy) * Sizeof(field.dtype) * VarCount,
        )
        while VarSize / 1024 > gc.Backend.LDMSize:
            if blocking[1] >= 2:
                tmpb1 = blocking[1]
                blocking[1] = int(blocking[1] / 2)
                VarSize = (
                    VarCount * (blocking[0] + 2 * hx) * (blocking[1] + 2 * hy) * Sizeof(field.dtype)
                )
            else:
                tmpb0 = blocking[0]
                blocking[0] = int(blocking[0] / 2)
                VarSize = (
                    VarCount * (blocking[0] + 2 * hx) * (blocking[1] + 2 * hy) * Sizeof(field.dtype)
                )

        print(
            "Check LDM",
            hx,
            VarSize / 1024,
            VarCount,
            blocking[0],
            hx,
            blocking[1],
            hy,
            Sizeof(field.dtype),
            (blocking[0] + 2 * hx) * (blocking[1] + 2 * hy) * Sizeof(field.dtype) * VarCount,
        )

        for field in chain(ir.FieldIn, ir.FieldOut):
            flag = True
            # print("New Check",field,SWOPTFor.FieldList)
            for fieldl in SWOPTFor.FieldList:
                # print("detail check",field,fieldl)
                if field.name == fieldl.name:
                    flag = False
                    break
            if flag:
                SWOPTFor.FieldList.append(field)

        return SWOPTFor

    def __call__(
        self,
        ctx: IRCallable,
        ProcDomain: Tuple[int, int, int],
        FieldHaloRange: Dict[str, List],
        ProcHaloRange: List[int],
    ):
        if isinstance(ctx, IRSpace):
            self.ProcDomain = ProcDomain
            self.FieldHaloRange = FieldHaloRange
            self.ProcHaloRange = ProcHaloRange
            super().__call__(ctx)
