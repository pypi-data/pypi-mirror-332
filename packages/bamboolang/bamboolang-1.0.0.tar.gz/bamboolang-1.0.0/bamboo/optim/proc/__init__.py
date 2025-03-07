from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, cast, Dict
import copy

from bamboo.lang.ir import IRPrinter, Stat, Var
from bamboo.optim.trans import ParForRange
from bamboo.optim.proc.graph import FieldGraph


@dataclass
class UniqueProcASTInfo:
    def __init__(
        self,
        ProcTlieList: List[int],
        ProcRange: Tuple[int, int],
        TimeOpList: List[List[Tuple[str, List[Any]]]],
    ):
        self.ProcTlieList = ProcTlieList
        self.ProcRange = ProcRange
        self.TimeOpList = copy.deepcopy(TimeOpList)
        self.TimeOpFieldGraph: List[FieldGraph] = []
        self.FieldHaloRange: Dict[int, List] = {}
        self.ProcHaloRange: List[int] = [0, 0, 0]


@dataclass
class VarInfo:
    def __init__(self, name: str = "", dtype: str = "", Isstruct: bool = False):
        self.name = name
        self.dtype = dtype
        self.Isstruct = Isstruct

    def __str__(self):
        return f"name = {self.name}, dtype = {self.dtype}"


@dataclass
class FieldVarInfo:
    def __init__(
        self,
        id: int = -1,
        name: str = "",
        dtype: str = "",
        shape: Tuple[int, int, int] = [0, 0, 0],
        pos: Tuple[bool, bool, bool] = [True, True, True],
        UpdateHalo: bool = False,
        UpdateHaloGlobal: bool = False,
    ):
        self.id = id
        self.name = name
        self.dtype = dtype
        self.shape = shape
        self.pos = pos
        self.UpdateHalo = UpdateHalo
        self.UpdateHaloGlobal = UpdateHaloGlobal
        self.HaloOrient = []

    def __str__(self):
        return f"id = {self.id}, name = {self.name}, dtype = {self.dtype}, shape = {self.shape}, pos = {self.pos}, UpdateHalo = {self.UpdateHalo}, HaloOrient = {self.HaloOrient}"


@dataclass
class OptForStat(Stat):
    # 暂未考虑一个循环内，某变量同时在等号左右两侧的情况
    ranges: List[ParForRange]
    body: List[Stat]
    FieldIn: List[FieldVarInfo]
    FieldOut: List[FieldVarInfo]
    ConstField: List[FieldVarInfo]
    ProcInvolved: List[int]
    FuncCall: List[str]
    VarDeclare: List[VarInfo]
    StencilType: str  # o x y z xy xz yz xyz
    Complexity: str
    UseGlobalHalo: bool

    # def __init__(self,ranges: List[ParForRange], body: List[Stat], FieldIn : List[FieldVarInfo])

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
        printer.writeln("Opt Info:")
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
        printer.ident -= 2
        printer.writeln("}")
        printer.writeln("Const Field: {")
        printer.ident += 2
        for field in self.ConstField:
            printer.writeln(field.name)
        printer.ident -= 2
        printer.writeln("}")

        printer.writeln("Var Declare: {")
        printer.ident += 2
        for field in self.VarDeclare:
            printer.writeln(str(field))
        printer.ident -= 2
        printer.writeln("}")
        printer.writeln("Complex: {")
        printer.ident += 2
        printer.writeln(self.StencilType)
        printer.writeln(str(self.Complexity))
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
