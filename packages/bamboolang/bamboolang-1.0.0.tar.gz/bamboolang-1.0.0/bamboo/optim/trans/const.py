from typing import cast
from bamboo.lang.ir import IRSpace, IRVisitor
from bamboo.lang.ir.expr import FloatExpr, IntExpr, ShapeExpr, BinExpr, UniExpr
from bamboo.lang.dtype import ShapedFieldInfo


class ConstPropagator(IRVisitor):
    # ParFor range is not visited

    def visit_IntExpr(self, ctx: IRSpace, ir: IntExpr):
        setattr(ir, "_value", ir.val)

    def visit_FloatExpr(self, ctx: IRSpace, ir: FloatExpr):
        setattr(ir, "_value", ir.val)

    def visit_BinExpr(self, ctx: IRSpace, ir: BinExpr):
        try:
            setattr(ir, "_value", int(eval(str(ir))))
        except:
            pass

    def visit_UniExpr(self, ctx: IRSpace, ir: UniExpr):
        try:
            setattr(ir, "_value", int(eval(str(ir))))
        except:
            pass
