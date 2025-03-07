from typing import cast
from bamboo.lang.ir import IRSpace, IRVisitor
from bamboo.lang.ir.expr import FloatExpr, IntExpr, ShapeExpr, BinExpr, UniExpr
from bamboo.lang.dtype import ShapedFieldInfo


class Updater(IRVisitor):
    # update field info in current ast
    # ParFor range is not visited

    def visit_ShapeExpr(self, ctx: IRSpace, ir: ShapeExpr):
        if isinstance(ir.field.info, ShapedFieldInfo):
            cast(ShapedFieldInfo, ir.field.info)
            setattr(ir, "_value", ir.field.info.shape[ir.idx])
