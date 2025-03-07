from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple, Union
from bamboo.lang.dtype import DataT, FieldT, TimedFieldInfo, ValT
from bamboo.lang.ir import Expr, IRExternFunc, IRFunc, Var, MemCtx


class BinOp(Enum):
    Add = "+"
    Sub = "-"
    Mul = "*"
    Div = "/"
    Pow = "**"
    Mod = "%"
    BitAnd = "&"
    BitOr = "|"
    BitXor = "^"


class CompOp(Enum):
    Eq = "=="
    Ne = "!="
    Gt = ">"
    Lt = "<"
    Ge = ">="
    Le = "<="


class BoolOp(Enum):
    And = "and"
    Or = "or"


class UniOp(Enum):
    Neg = "-"
    Not = "not"


@dataclass
class BinExpr(Expr):
    lhs: Expr
    rhs: Expr
    op: Union[BinOp, CompOp, BoolOp]

    def __str__(self) -> str:
        return f"({self.lhs} {self.op.value} {self.rhs})"


@dataclass
class UniExpr(Expr):
    rhs: Expr
    op: UniOp

    def __str__(self) -> str:
        return f"({self.op.value} {self.rhs})"


@dataclass
class IntExpr(Expr):
    val: int
    length: int = 32

    def __str__(self) -> str:
        if self.length == 1:
            return ["False", "True"][self.val]
        else:
            return str(self.val)


@dataclass
class FloatExpr(Expr):
    val: float
    length: int = 64

    def __str__(self) -> str:
        return str(self.val)


@dataclass
class StrExpr(Expr):
    val: str

    def __str__(self) -> str:
        return f"'{self.val}'"


@dataclass
class CastExpr(Expr):
    src: Expr
    cast_type: ValT

    def __str__(self) -> str:
        return f"cast<{str(self.cast_type)}>({str(self.src)})"


@dataclass
class ShapeExpr(Expr):
    field: FieldT
    idx: int

    def __str__(self) -> str:
        return f"{self.field.local_name}.shape_{['x','y','z'][self.idx]}"


@dataclass
class PostExpr(Expr): ...


@dataclass
class AttrExpr(PostExpr):
    var: Var
    ctx: MemCtx
    attrs: Tuple[str, ...]

    def __str__(self) -> str:
        if len(self.attrs) == 0:
            return str(self.var)
        else:
            return str(self.var) + "." + ".".join(self.attrs)


@dataclass
class FieldExpr(PostExpr):
    field: FieldT
    ctx: MemCtx
    idx: List[Expr]
    attrs: Tuple[str, ...]

    @property
    def time(self):
        if not isinstance(self.field.info, TimedFieldInfo):
            return -1 if self.ctx == MemCtx.Load else 0
        else:
            return self.field.info.time

    def __str__(self) -> str:
        attr_str = "" if len(self.attrs) == 0 else "." + ".".join(self.attrs)
        return f"{self.field.local_name}[{self.time}][{', '.join(map(str, self.idx))}]{attr_str}"


@dataclass
class IRStub:
    name: str  # for hybrid class construction and builtin functions
    arg_type: List[Tuple[str, DataT]]
    dtype: ValT

    def __str__(self) -> str:
        args = ", ".join(map(lambda x: f"{x[1]} {x[0]}", self.arg_type))
        return f"extern {self.dtype} {self.name}({args})"


@dataclass
class CallExpr(Expr):
    symb: Union[IRStub, IRFunc, IRExternFunc]
    args: List[Union[Expr, FieldT]]

    def __str__(self) -> str:
        return f"{self.symb.name}({', '.join(map(str, self.args))})"


class ExternCallMethod(Enum):
    INIT = "init"
    RUN = "run"
    FINALIZE = "finalize"


@dataclass
class ExternCallExpr(CallExpr):
    method: ExternCallMethod

    def __str__(self) -> str:
        return f"{self.symb.name}.{self.method.value}({', '.join(map(str, self.args))})"


@dataclass
class FieldCallExpr(CallExpr):
    field_expr: FieldExpr

    def __str__(self) -> str:
        return f"{str(self.field_expr)}.{CallExpr.__str__(self)}"
