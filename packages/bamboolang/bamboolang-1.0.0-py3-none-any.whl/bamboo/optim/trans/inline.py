from typing import List, cast
from bamboo.lang.ir import Var
from bamboo.lang.dtype import FieldT, HybridFieldT
from bamboo.lang.ir import Expr, IRCallable, IRSpace, IRTransformer, Stat
from bamboo.lang.ir.expr import AttrExpr, MemCtx
from bamboo.lang.ir.stat import AssignStat, SpaceStat


class Inliner(IRTransformer):
    def __call__(self, ctx: IRCallable):
        if isinstance(ctx, IRSpace):
            super().__call__(ctx)

    def visit_SpaceStat(self, ctx: IRSpace, ir: SpaceStat):
        # perform inline, we've passed type check now

        inlined_stats: List[Stat] = []
        for idx, arg in enumerate(ir.args):
            if isinstance(arg, Expr):
                tmp_var = AttrExpr(
                    ir.lineno, cast(Var, ir.space.arg_vars[idx][1]), MemCtx.Store, ()
                )
                inlined_stats.append(AssignStat(ir.lineno, arg, tmp_var))
            else:
                ctx.inline_fields[arg].extend(ir.space.inline_fields[ir.space.arg_vars[idx][1]])

        # field inline
        for current_field, flist in ctx.inline_fields.items():
            for field in flist:
                field.ref = current_field.ref

        inlined_stats.extend(ir.space.body)
        return inlined_stats
