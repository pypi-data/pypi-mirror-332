from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Union, cast
from bamboo.lang.ir import (
    Expr,
    IRCallable,
    IRSpace,
    IRTransformer,
    IRVisitor,
    MemCtx,
    Stat,
    Var,
)
from bamboo.lang.ir.expr import AttrExpr, BinExpr, BinOp, FieldExpr, IntExpr, UniExpr
from bamboo.lang.ir.stat import AssignStat, ForStat
from bamboo.optim.trans import ParForRange, ParForStat


def constexpr(expr: Expr) -> Union[int, float, None]:
    if hasattr(expr, "_value"):
        return getattr(expr, "_value")
    else:
        return None


@dataclass
class _ParFor:
    var: Var
    begin: int
    end: int
    step: int
    body: List[Stat]
    idx: int = -1


class ParallelFilter(IRVisitor):
    def __init__(self, parallel_zone: List[_ParFor]) -> None:
        super().__init__()
        self.parallel_zone = parallel_zone

    def visit_AttrExpr(self, ctx, ir: AttrExpr):
        if ir.ctx == MemCtx.Store:
            for id, forstat in enumerate(self.parallel_zone):
                if forstat.var == ir.var:
                    self.parallel_zone = self.parallel_zone[:id]
                    break

    def fetch_relation(self, ir: Expr):
        c = constexpr(ir)

        if c is not None:
            return cast(int, c)

        if isinstance(ir, AttrExpr):
            return (ir.var, 0)
        elif isinstance(ir, BinExpr):
            lr = self.fetch_relation(ir.lhs)
            rr = self.fetch_relation(ir.rhs)

            if isinstance(lr, tuple) and isinstance(rr, int) and ir.op in (BinOp.Add, BinOp.Sub):
                if ir.op == BinOp.Add:
                    return (lr[0], lr[1] + rr)
                else:
                    return (lr[0], lr[1] - rr)

        return None

    def visit_FieldExpr(self, ctx, ir: FieldExpr):
        # TODO: THIS IS WEIRD, NEEDS DISCUSSION!!!
        related_idx = [self.fetch_relation(x) for x in ir.idx]
        for idx, i in enumerate(related_idx):
            if isinstance(i, tuple):
                idx_var: Var = i[0]
                for id, forstat in enumerate(self.parallel_zone):
                    if forstat.var == idx_var:
                        if forstat.idx == -1:
                            forstat.idx = idx
                        if forstat.idx != idx:
                            self.parallel_zone = self.parallel_zone[:id]
                            break

    def __call__(self, ctx: IRCallable, body: List[Stat]):
        if len(self.parallel_zone) == 0:
            return self.parallel_zone

        for stat in body:
            # mark the access pattern of each variable and field
            self.visit(ctx, stat)

        return self.parallel_zone


class Parallelizer(IRTransformer):
    def __call__(self, ctx: IRCallable):
        if isinstance(ctx, IRSpace):
            super().__call__(ctx)

    def recog_parallel_zone(self, ctx: IRSpace, ir: ForStat):
        original_ir = ir  # save the original ir node

        parallel_loop_zone: List[_ParFor] = []

        # search for loop ranges that could be parallel
        current_body: List[Stat] = [ir]

        def validate_body(a):
            return len(current_body) == 1 and isinstance(current_body[0], ForStat)

        while validate_body(current_body):
            for_stat = cast(ForStat, current_body[0])

            # make sure these things are constant
            begin, end, step = (
                constexpr(for_stat.begin),
                constexpr(for_stat.end),
                constexpr(for_stat.step),
            )

            def validate_loop_range(a):
                return a is not None and isinstance(a, int)

            is_valid_range = (
                validate_loop_range(begin)
                and validate_loop_range(end)
                and validate_loop_range(step)
            )

            # make the type checker happy
            begin, end, step = cast(int, begin), cast(int, end), cast(int, step)

            if not is_valid_range:
                break

            # make sure loop variable does not appear again
            for loop_zone in parallel_loop_zone:
                if loop_zone.var == for_stat.var:
                    return original_ir

            # add to loop zone
            parallel_loop_zone.append(_ParFor(for_stat.var, begin, end, step, for_stat.body))

            current_body = for_stat.body

        parallel_loop_zone = parallel_loop_zone[:3]
        parallel_loop_zone = ParallelFilter(parallel_loop_zone)(ctx, current_body)

        if len(parallel_loop_zone) == 0:
            return original_ir
        else:
            return ParForStat(
                original_ir.lineno,
                [ParForRange(x.var, x.begin, x.end, x.step) for x in parallel_loop_zone],
                parallel_loop_zone[-1].body,
            )

    def visit_ParForStat(self, ctx, ir):
        return ir

    def visit_ForStat(self, ctx: IRSpace, ir: ForStat):
        return self.recog_parallel_zone(ctx, ir)
