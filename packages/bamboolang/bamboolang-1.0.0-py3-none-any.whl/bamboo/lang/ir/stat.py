from dataclasses import dataclass
from typing import List, Union
from bamboo.lang.dtype import FieldT
from bamboo.lang.ir import IRPrinter, IRSpace, Stat, Expr, Var
from bamboo.lang.ir.expr import PostExpr


@dataclass
class AssignStat(Stat):
    src: Expr
    dst: PostExpr

    def print(self, printer: IRPrinter):
        printer.writeln(f"{self.dst} = {self.src}")


@dataclass
class PassStat(Stat):
    def print(self, printer: IRPrinter):
        printer.writeln("pass")


@dataclass
class ForStat(Stat):
    var: Var
    begin: Expr
    step: Expr
    end: Expr
    body: List[Stat]

    def print(self, printer: IRPrinter):
        printer.writeln(f"for {self.var} in ({self.begin}, {self.end}, {self.step}) {{")
        printer.ident += 2
        for s in self.body:
            s.print(printer)
        printer.ident -= 2
        printer.writeln("}")


@dataclass
class ExprStat(Stat):
    expr: Expr

    def print(self, printer: IRPrinter):
        printer.writeln(str(self.expr))


@dataclass
class RetStat(Stat):
    expr: Expr

    def print(self, printer: IRPrinter):
        printer.writeln(f"return {str(self.expr)}")


@dataclass
class SpaceStat(Stat):
    space: IRSpace
    args: List[Union[Expr, FieldT]]

    def print(self, printer: IRPrinter):
        printer.writeln(f"{self.space.name}({', '.join(map(str, self.args))})")


@dataclass
class IfStat(Stat):
    test: Expr
    body: List[Stat]
    orelse: List[Stat]

    def print(self, printer: IRPrinter):
        printer.writeln(f"if ({self.test}) {{")
        printer.ident += 2
        for s in self.body:
            s.print(printer)
        printer.ident -= 2
        if len(self.orelse) > 0:
            printer.writeln(f"}} else {{")
            printer.ident += 2
            for s in self.orelse:
                s.print(printer)
            printer.ident -= 2
            printer.writeln("}")
        else:
            printer.writeln("}")
