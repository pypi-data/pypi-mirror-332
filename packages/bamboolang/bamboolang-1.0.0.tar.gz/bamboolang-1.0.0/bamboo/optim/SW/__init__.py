from dataclasses import dataclass
from typing import List

from bamboo.lang.ir import IRPrinter, Stat, Var
from bamboo.optim.proc import OptForStat, FieldVarInfo, VarInfo


@dataclass
class SWOptForStat(OptForStat):
    FieldList: List[FieldVarInfo]
    VarList: List[VarInfo]
    OptLevel: int
    # 1=basic blocking 每个stencil所有变量halo设置大小相同
    # 2=1的基础上增加滑动窗口优化
    # x y z
    Mapping: List[int]
    Blocking: List[int]

    def print(self, printer: IRPrinter):
        printer.writeln("parallel for {")
        printer.ident += 2
        for r in self.ranges:
            printer.writeln(f"{r.var} in ({r.begin}, {r.end}, {r.step})")
        printer.ident -= 2
        printer.writeln("} {")
        printer.ident += 2
        for s in self.body:
            printer.writeln(str(type(s)))
            s.print(printer)

        printer.writeln("{")
        printer.ident += 2
        printer.writeln("SW Opt Info:")
        printer.writeln("OptLevel: " + str(self.OptLevel))
        printer.writeln("Mapping: {")
        printer.ident += 2
        printer.writeln(str(self.Mapping))
        printer.ident -= 2
        printer.writeln("}")
        printer.writeln("Blocking: {")
        printer.ident += 2
        printer.writeln(str(self.Blocking))
        printer.ident -= 2
        printer.writeln("}")
        printer.writeln("Field In: {")
        printer.ident += 2
        for field in self.FieldIn:
            printer.writeln(str(field))
        printer.ident -= 2
        printer.writeln("}")

        printer.writeln("Field out: {")
        printer.ident += 2
        for field in self.FieldOut:
            printer.writeln(str(field))
        printer.writeln(self.StencilType)
        printer.ident -= 2
        printer.writeln("}")

        printer.writeln("Const Field: {")
        printer.ident += 2
        for field in self.ConstField:
            printer.writeln(field.name)
        printer.ident -= 2
        printer.writeln("}")

        printer.writeln("Process Involved: {")
        printer.ident += 2
        for id in self.ProcInvolved:
            printer.writeln(str(id))
        printer.ident -= 2
        printer.writeln("}")
        printer.ident -= 2
        printer.writeln("}")
        printer.ident -= 2
        printer.writeln("}")
