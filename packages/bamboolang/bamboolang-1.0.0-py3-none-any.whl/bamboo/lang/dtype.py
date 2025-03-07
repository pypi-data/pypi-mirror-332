from dataclasses import dataclass
from typing import Generator, Optional, Tuple, cast

from bamboo.lang.util import DictTuple


@dataclass
class DataT: ...


@dataclass
class ValT(DataT):
    """value type, a fixed size type that places on the stack or local memory"""

    def undef(self):
        return isinstance(self, UndefT)


@dataclass
class UndefT(ValT): ...


@dataclass
class VoidT(ValT):
    def __str__(self):
        return "void"


@dataclass
class NumT(ValT):
    """number type, a fixed size number that corresponding to number on platform"""

    bits_width: int

    @staticmethod
    def implicit_cast(a, b):
        """perform implicit cast judgement on two number type"""

        def bias(a):
            return (1 if isinstance(a, FloatT) else 0, a.bits_width)

        m = max(bias(a), bias(b))
        return [IntT, FloatT][m[0]](m[1])

    @staticmethod
    def compatible(src: "NumT", dst: "NumT"):
        def bias(x):
            return 1 if isinstance(x, FloatT) else 0

        return (bias(dst) >= bias(src)) and (dst.bits_width >= src.bits_width)


@dataclass
class IntT(NumT):
    """integer type"""

    def __str__(self) -> str:
        return f"Int{self.bits_width}"


@dataclass
class FloatT(NumT):
    """floating type"""

    def __str__(self) -> str:
        return f"Float{self.bits_width}"


@dataclass
class StrT(ValT):
    """string type"""

    def __str__(self) -> str:
        return f"Str"


@dataclass
class HybridT(ValT, DictTuple[ValT]):
    name: str

    def __str__(self) -> str:
        return self.name


class FieldDesc:
    def __init__(self, name: str) -> None:
        self.name = name


class FieldInfo:
    def __init__(self, dtype: ValT, desc: Optional[FieldDesc] = None) -> None:
        self.dtype = dtype
        self.desc = desc

    def __repr__(self) -> str:
        return str(self.dtype)

    def __eq__(self, f: "FieldInfo"):
        if f.desc is not None and self.desc is not None:
            desc_equ = f.desc == self.desc
        else:
            desc_equ = True
        return f.dtype == self.dtype and desc_equ

    def __ne__(self, f: "FieldInfo"):
        return not self == f


class ShapedFieldInfo(FieldInfo):
    def __init__(
        self, dtype: ValT, shape: Tuple[int, int, int], desc: Optional[FieldDesc] = None
    ) -> None:
        super().__init__(dtype, desc)
        self.shape = shape


class TimedFieldInfo(ShapedFieldInfo):
    def __init__(
        self,
        dtype: ValT,
        shape: Tuple[int, int, int],
        time: int,
        desc: Optional[FieldDesc] = None,
    ) -> None:
        super().__init__(dtype, shape, desc)
        self.time = time


class FieldRef:
    def __init__(self, info: FieldInfo) -> None:
        self.info = info
        self.local_name = ""


class AbsFieldT(DataT): ...


@dataclass
class FieldT(AbsFieldT):
    """field type, an arbitary physics field"""

    ref: FieldRef

    @property
    def info(self):
        return self.ref.info

    @property
    def local_name(self):
        return self.ref.local_name

    @property
    def dtype(self):
        return self.ref.info.dtype

    def __eq__(self, o):
        return isinstance(o, FieldT) and self.info == o.info

    def __ne__(self, o):
        return not self.__eq__(o)

    def __str__(self) -> str:
        field_name = "Field" if self.info.desc is None else self.info.desc.name
        return f"{field_name}[{self.dtype}]"

    def __hash__(self):
        return hash(id(self))


@dataclass
class HybridFieldT(AbsFieldT, DictTuple[AbsFieldT]):
    name: str
    local_name: str = ""

    def rec_iter(self, sep) -> Generator[Tuple[str, FieldT], None, None]:
        for name, value in self:
            if isinstance(value, FieldT):
                yield name, value
            else:
                for iname, ivalue in cast(HybridFieldT, value).rec_iter(sep):
                    yield f"{name}{sep}{iname}", ivalue

    def __str__(self) -> str:
        return self.name


def GetCType(inType) -> str:
    if isinstance(inType, VoidT):
        return "void"
    if isinstance(inType, IntT):
        if inType.bits_width == 1:
            return "bool"
        if inType.bits_width == 32:
            return "int"
        if inType.bits_width == 64:
            return "long long"
    if isinstance(inType, FloatT):
        if inType.bits_width == 32:
            return "float"
        if inType.bits_width == 64:
            return "double"
    if isinstance(inType, FieldT):
        res = GetCType(inType.dtype) + "***"
        return res
    if isinstance(inType, HybridFieldT) or isinstance(inType, HybridT):
        return "struct " + inType.name
