from typing import cast, List
from bamboo.lang.dtype import DataT, NumT, IntT, FloatT
from bamboo.lang.dtype_ext import LonLatFieldDesc

from bamboo.lang.ir import IRVisitor, IRNode, IRCallable
from bamboo.lang.ir.expr import Expr, FieldExpr, AttrExpr, BinExpr, BinOp
from bamboo.optim.proc import VarInfo
from bamboo.optim.trans.parallel import constexpr


def GetIdx(ir: Expr, VarDeclare: List[VarInfo] = []):
    c = constexpr(ir)
    gh = False

    if c is not None:
        return 0, False

    if isinstance(ir, AttrExpr):
        if VarDeclare != []:
            for var in VarDeclare:
                if var.name == ir.var.name:
                    return 1, True
            return 0, False
        else:
            return 0, False
    elif isinstance(ir, BinExpr):
        lr = ir.lhs
        rr = ir.rhs
        if isinstance(rr, BinExpr) or isinstance(rr, AttrExpr):
            res = 1
            gh = True
        else:
            res = rr.val
        if ir.op == BinOp.Add:
            return (res), gh
        else:
            return (-res), gh

    return 0, gh


# ToCheck LonLatField信息没进来 isinstance(desc,LonLatFieldDesc) = False
def IsConstField(field: Expr):
    if not isinstance(field, FieldExpr):
        return False

    # cast(FieldExpr,field)
    desc = field.field.info.desc
    # print("Why??",field.field.local_name,field.field.info.desc.const,isinstance(desc,LonLatFieldDesc))

    if desc == None:
        return False

    return desc.const

    # if (isinstance(desc,LonLatFieldDesc)):
    #     cast(LonLatFieldDesc,desc)
    #     return desc.const


def IsSubList(sub: List[int], big: List[int]):
    for x in sub:
        if not x in big:
            return False
    return True


def DTypeToStr(DType: DataT) -> str:
    DTypeStr: str = ""
    if isinstance(DType, IntT):
        DTypeStr = "int"
    elif isinstance(DType, FloatT):
        if DType.bits_width == 32:
            DTypeStr = "float"
        elif DType.bits_width == 64:
            DTypeStr = "double"
    else:
        DTypeStr = DType

    return DTypeStr


def CutFuncName(prefix: str) -> str:
    funcname: str = ""
    for x in prefix:
        if x != "<":
            funcname += x
        else:
            return funcname
