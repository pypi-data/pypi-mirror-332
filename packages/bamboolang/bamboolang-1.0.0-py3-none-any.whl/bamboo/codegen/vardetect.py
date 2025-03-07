from typing import List
from bamboo.lang.ir import IRVisitor, IRCallable
from bamboo.lang.ir.expr import FieldExpr, AttrExpr, FieldExpr, BinExpr, UniExpr
from bamboo.lang.ir.stat import Stat


class LoopVarDetector(IRVisitor):
    def __init__(self, ctx: IRCallable):
        self.vars = []
        self.dim = {}
        self.ctx = ctx

    def VarDimDetect(self, vars: List[str], for_body: List[Stat]):
        self.vars = vars
        self.dim = {}
        for stat in for_body:
            self.visit(self.ctx, stat)
        return self.dim

    def visit_AttrExpr(self, ctx: IRCallable, ir: AttrExpr):
        ret = ""
        if ir.var.name in self.vars:
            ret = ir.var.name
        return ret

    def visit_BinExpr(self, ctx: IRCallable, ir: BinExpr):
        ret_l = self.visit(ctx, ir.lhs)
        ret_r = self.visit(ctx, ir.rhs)
        ret = ""
        if ret_l in self.vars:
            ret = ret_l
        if ret_r in self.vars:
            ret = ret_r
        return ret

    def visit_UniExpr(self, ctx: IRCallable, ir: UniExpr):
        ret = self.visit(ctx, ir.rhs)
        return ret

    def visit_FieldExpr(self, ctx: IRCallable, ir: FieldExpr):
        id = 0
        for inx in ir.idx:
            inx_var = self.visit(ctx, inx)
            if inx_var in self.vars:
                self.dim[inx_var] = id
            id = id + 1
