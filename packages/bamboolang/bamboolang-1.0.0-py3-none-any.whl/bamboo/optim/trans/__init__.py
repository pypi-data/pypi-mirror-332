from dataclasses import dataclass
from typing import List

from bamboo.lang.ir import IRPrinter, Stat, Var


@dataclass
class ParForRange:
    var: Var
    begin: int
    end: int
    step: int


@dataclass
class ParForStat(Stat):
    ranges: List[ParForRange]
    body: List[Stat]

    def print(self, printer: IRPrinter):
        printer.writeln("parallel for {")
        printer.ident += 2
        for r in self.ranges:
            printer.writeln(f"{r.var} in ({r.begin}, {r.end}, {r.step})")
        printer.ident -= 2
        printer.writeln("} {")
        printer.ident += 2
        for s in self.body:
            s.print(printer)
        printer.ident -= 2
        printer.writeln("}")
