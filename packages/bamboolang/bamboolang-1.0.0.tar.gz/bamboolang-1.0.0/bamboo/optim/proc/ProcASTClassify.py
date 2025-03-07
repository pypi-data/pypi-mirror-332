from typing import Dict, List, cast, Tuple
from collections import Counter

from bamboo.lang.ir import Expr, IRCallable, IRSpace, IRTransformer, IRVisitor, IRPrinter
from bamboo.lang.ir.stat import ForStat, AssignStat
from bamboo.lang.ir.expr import (
    FieldExpr,
    BinExpr,
    IntExpr,
    AttrExpr,
    FieldCallExpr,
    IRStub,
)

from bamboo.optim.trans import ParForStat
from bamboo.optim.proc import OptForStat, FieldVarInfo
from bamboo.optim.proc.partition import (
    ProcessPartition,
    PartitionConfiguration,
    ProcessTile,
)
from bamboo.optim.proc.helper import IsSubList


# 根据划分，将AST分类
class ProcASTClassify(IRTransformer):
    ProcList: List[int]
    Range: Tuple[int, int]

    def visit_OptForStat(self, ctx: IRCallable, ir: OptForStat):
        if IsSubList(self.ProcList, ir.ProcInvolved):
            return ir
        else:
            return None

    def visit_FieldCallExpr(self, ctx: IRCallable, ir: FieldCallExpr):
        func_name = ir.symb.name
        if isinstance(ir.symb, IRStub) and func_name == "sum":
            # Todo暂时只做一行的sum
            if self.Range[0] <= ir.args[4].val and ir.args[4].val <= self.Range[1]:
                return ir
            else:
                ir.symb.name = "none"
                return ir
        if isinstance(ir.symb, IRStub) and func_name == "ncRead":
            return ir

        return ir

    def __call__(self, ctx: IRCallable, ProcList: List[int], Range: Tuple[int, int]):
        if isinstance(ctx, IRSpace):
            self.ProcList = ProcList
            self.Range = Range
            super().__call__(ctx)
