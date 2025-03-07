from typing import List, cast
from bamboo.lang.ir import IRCallable, IRSpace, IRTransformer, Stat
from bamboo.lang.ir.stat import IfStat


class Predictor(IRTransformer):
    def __call__(self, ctx: IRCallable):
        super().__call__(ctx)

    def visit_IfStat(self, ctx: IRCallable, ir: IfStat):
        predicted_body: List[Stat] = []
        for stat in ir.body:
            if isinstance(stat, IfStat):
                stats = self.visit(ctx, stat)
                if isinstance(stats, list):
                    predicted_body.extend(stats)
                else:
                    predicted_body.append(stat)
            else:
                predicted_body.append(stat)
        ir.body = predicted_body

        predicted_orelse: List[Stat] = []
        for stat in ir.orelse:
            if isinstance(stat, IfStat):
                stats = self.visit(ctx, stat)
                if isinstance(stats, list):
                    predicted_orelse.extend(stats)
                else:
                    predicted_orelse.append(stat)
            else:
                predicted_orelse.append(stat)
        ir.orelse = predicted_orelse

        if hasattr(ir.test, "_value"):
            return ir.body if getattr(ir.test, "_value") != 0 else ir.orelse
        else:
            return ir
