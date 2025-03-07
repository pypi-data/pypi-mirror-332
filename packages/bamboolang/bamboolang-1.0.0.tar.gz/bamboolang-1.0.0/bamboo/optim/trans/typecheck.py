from typing import List, Tuple, cast, Union
from bamboo.lang.dtype import (
    FieldT,
    FloatT,
    IntT,
    NumT,
    HybridT,
    StrT,
    ValT,
    HybridFieldT,
    VoidT,
)
from bamboo.lang.ir import Expr, IRCallable, IRFunc, IRVisitor, IRExternFunc
from bamboo.lang.ir.expr import (
    AttrExpr,
    BinExpr,
    BinOp,
    BoolOp,
    CallExpr,
    FieldCallExpr,
    CompOp,
    FieldExpr,
    FloatExpr,
    CastExpr,
    ShapeExpr,
    IRStub,
    IntExpr,
    StrExpr,
    UniExpr,
    ExternCallExpr,
    UniOp,
)
from bamboo.lang.ir.stat import (
    AssignStat,
    ExprStat,
    ForStat,
    IfStat,
    PassStat,
    RetStat,
    SpaceStat,
)


class TypeChecker(IRVisitor):
    def vexpr(self, ctx: IRCallable, ir: Expr) -> ValT:
        self.visit(ctx, ir)
        return ir.dtype

    # ========== Expression ==========

    def visit_BinExpr(self, ctx: IRCallable, ir: BinExpr):
        lt, rt = self.vexpr(ctx, ir.lhs), self.vexpr(ctx, ir.rhs)

        err_msg = f"invalid bin-op '{ir.op.value}' on '{lt}' and '{rt}'"

        if isinstance(ir.op, BinOp) or isinstance(ir.op, CompOp):
            if isinstance(lt, StrT) or isinstance(rt, StrT):
                if not (ir.op == CompOp.Eq or ir.op == CompOp.Ne):
                    ctx.syntax_error("str only supports == and != as comparision operators")
                if not (isinstance(lt, StrT) and isinstance(rt, StrT)):
                    ctx.type_error(err_msg)
            elif not (isinstance(lt, NumT) and isinstance(rt, NumT)):
                ctx.type_error(err_msg)
            ir.dtype = IntT(1) if isinstance(ir.op, CompOp) else NumT.implicit_cast(lt, rt)
        elif isinstance(ir.op, BoolOp):
            # if not (lt == IntT(1) and rt == IntT(1)):
            if not (isinstance(lt, IntT) and isinstance(rt, IntT)):
                ctx.type_error(err_msg)
            ir.dtype = IntT(1)

    def visit_UniExpr(self, ctx: IRCallable, ir: UniExpr):
        rt = self.vexpr(ctx, ir.rhs)

        # check if ! on bool and neg on number
        check_f = {
            UniOp.Not: lambda x: x == IntT(1),
            UniOp.Neg: lambda x: isinstance(x, NumT),
        }

        if not check_f[ir.op](rt):
            ctx.type_error(f"invalid uni-op '{ir.op.value}' on '{rt}'")

        ir.dtype = rt

    def visit_IntExpr(self, ctx: IRCallable, ir: IntExpr):
        ir.dtype = IntT(ir.length)

    def visit_FloatExpr(self, ctx: IRCallable, ir: FloatExpr):
        ir.dtype = FloatT(ir.length)

    def visit_CastExpr(self, ctx: IRCallable, ir: CastExpr):
        ir.dtype = ir.cast_type

    def visit_ShapeExpr(self, ctx: IRCallable, ir: ShapeExpr):
        assert ir.idx >= 0 and ir.idx <= 2

        ir.dtype = IntT(32)

    def visit_StrExpr(self, ctx: IRCallable, ir: StrExpr):
        ir.dtype = StrT()

    def visit_AttrExpr(self, ctx: IRCallable, ir: AttrExpr):
        dtype = ir.var.dtype
        for attr in ir.attrs:
            if isinstance(dtype, HybridT) and dtype.has(attr):
                dtype = dtype.get(attr)
            else:
                ctx.type_error(f"invalid attribute '{attr}' for type '{dtype}'")

        ir.dtype = dtype

    def visit_FieldExpr(self, ctx: IRCallable, ir: FieldExpr):
        assert not isinstance(ctx, IRFunc)

        for id, idx in enumerate(ir.idx):
            it = self.vexpr(ctx, idx)
            if not isinstance(it, IntT):
                ctx.type_error(f"invalid field index type '{it}' at {id}")

        if isinstance(ir.field, HybridFieldT):
            ctx.type_error(
                f"hybrid field type '{ir.field.local_name}.{'.'.join(ir.attrs)}' can not be directly accessed"
            )

        # check elements now
        elt = ir.field.info.dtype
        for attr in ir.attrs:
            if not isinstance(elt, HybridT) or not elt.has(attr):
                ctx.type_error(f"invalid attribute '{attr}' for type '{elt}'")

            elt = elt.get(attr)

        ir.dtype = elt

    def check_call(
        self,
        ctx: IRCallable,
        args: List[Union[Expr, FieldT]],
        func: Union[IRCallable, IRStub],
    ):
        if len(args) != len(func.arg_type):
            if isinstance(func, IRExternFunc):
                return func.dtype
            ctx.type_error(f"invalid call to '{func.name}', mismatch argument length")

        for id, (arg_name, expect_arg_t) in enumerate(func.arg_type):
            arg = args[id]
            if isinstance(arg, Expr):
                arg_t = self.vexpr(ctx, arg)
            else:
                arg_t = arg

            if isinstance(arg_t, NumT) and isinstance(expect_arg_t, NumT):
                typecheck_fail = not NumT.compatible(arg_t, expect_arg_t)
            else:
                typecheck_fail = arg_t != expect_arg_t

            if typecheck_fail:
                ctx.type_error(
                    f"invalid call to '{func.name}', mismatch argument type '{arg_t}' with '{expect_arg_t}' at {id}({arg_name})"
                )

        return func.dtype

    def visit_CallExpr(self, ctx: IRCallable, ir: CallExpr):
        ir.dtype = self.check_call(ctx, cast(List[Union[Expr, FieldT]], ir.args), ir.symb)

    def visit_FieldCallExpr(self, ctx: IRCallable, ir: FieldCallExpr):
        self.visit(ctx, ir.field_expr)
        ir.dtype = self.check_call(ctx, cast(List[Union[Expr, FieldT]], ir.args), ir.symb)

    # def visit_ExternCallExpr(self, ctx: IRCallable, ir: ExternCallExpr):
    #     pass

    # ========== Statement ==========

    def visit_ExprStat(self, ctx: IRCallable, ir: ExprStat):
        self.vexpr(ctx, ir.expr)

    def visit_ForStat(self, ctx: IRCallable, ir: ForStat):
        ranget = (
            self.vexpr(ctx, ir.begin),
            self.vexpr(ctx, ir.step),
            self.vexpr(ctx, ir.end),
        )

        def allisinstance(t, tt):
            for i in t:
                if not isinstance(i, tt):
                    return False
            return True

        if not allisinstance(ranget, IntT):
            ctx.type_error(f"invalid for range type '{ranget}'")

        if ir.var.dtype.undef():
            ir.var.dtype = cast(IntT, ranget[0])

        if not isinstance(ir.var.dtype, IntT):
            ctx.type_error(f"invalid for var type '{ir.var.dtype}'")

        for stat in ir.body:
            self.visit(ctx, stat)

    def visit_IfStat(self, ctx: IRCallable, ir: IfStat):
        dtype = self.vexpr(ctx, ir.test)
        if not isinstance(dtype, IntT):
            ctx.type_error(f"invalid condition type '{dtype}'")

        for stat in ir.body:
            self.visit(ctx, stat)

        for stat in ir.orelse:
            self.visit(ctx, stat)

    def visit_AssignStat(self, ctx: IRCallable, ir: AssignStat):
        def check_strict(ctx: IRCallable, st: ValT, dt: ValT, class_t):
            if isinstance(st, class_t) or isinstance(dt, class_t):
                if st != dt:
                    ctx.type_error(f"invalid assign from '{dt}' to '{st}'")
                else:
                    return True

        st = self.vexpr(ctx, ir.src)

        if isinstance(ir.dst, AttrExpr) and len(ir.dst.attrs) == 0 and ir.dst.var.dtype.undef():
            ir.dst.var.dtype = st

        dt = self.vexpr(ctx, ir.dst)

        if isinstance(dt, VoidT):
            ctx.type_error(f"invalid assign from '{dt}' type")

        assert isinstance(st, ValT) and isinstance(dt, ValT)

        if check_strict(ctx, st, dt, HybridT):
            return
        if check_strict(ctx, st, dt, StrT):
            return

        assert isinstance(st, NumT) and isinstance(dt, NumT)

        failure_num = not NumT.compatible(st, dt)

        if failure_num:
            ctx.type_error(f"invalid assign from '{dt}' to '{st}'")

    def visit_PassStat(self, ctx: IRCallable, ir: PassStat):
        pass

    def visit_RetStat(self, ctx: IRCallable, ir: RetStat):
        rt = self.vexpr(ctx, ir.expr)

        if rt != ctx.dtype:
            ctx.type_error(f"invalid return type from '{rt}' to '{ctx.dtype}'")

    def visit_SpaceStat(self, ctx: IRCallable, ir: SpaceStat):
        self.check_call(ctx, ir.args, ir.space)
        for stat in ir.space.body:
            self.visit(ctx, stat)
