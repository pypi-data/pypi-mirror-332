import inspect
from copy import deepcopy
from typing import Generic, Optional, Tuple, TypeVar, cast
from typing_extensions import get_args, get_origin
from bamboo.lang.dtype import (
    AbsFieldT,
    FieldInfo,
    FieldDesc,
    FieldRef,
    FieldT,
    FloatT,
    IntT,
    NumT,
    StrT,
    HybridFieldT,
    HybridT,
    ShapedFieldInfo,
    TimedFieldInfo,
    ValT,
    VoidT,
)


class Annot:
    def __init__(self, any=None) -> None:
        self.val = any


class NumAnnot(Annot):
    ANNOT_TYPE: NumT


class Bool(NumAnnot):
    ANNOT_TYPE: NumT = IntT(1)


class Int8(NumAnnot):
    ANNOT_TYPE: NumT = IntT(8)


class Int16(NumAnnot):
    ANNOT_TYPE: NumT = IntT(16)


class Int32(NumAnnot):
    ANNOT_TYPE: NumT = IntT(32)


class Int64(NumAnnot):
    ANNOT_TYPE: NumT = IntT(64)


class Float16(NumAnnot):
    ANNOT_TYPE: NumT = FloatT(16)


class Float32(NumAnnot):
    ANNOT_TYPE: NumT = FloatT(32)


class Float64(NumAnnot):
    ANNOT_TYPE: NumT = FloatT(64)


class String(Annot):
    ANNOT_TYPE: StrT = StrT()


T = TypeVar("T")


class _FieldTimeSlice:
    def __init__(self, info) -> None:
        self.info = info


class Field(Annot, Generic[T]):
    # make compiler happier
    shape_x: Int32
    shape_y: Int32
    shape_z: Int32

    def __init__(self, dtype, shape: Tuple[int, ...], desc: Optional[FieldDesc] = None) -> None:
        super().__init__()
        lshape = list(shape)
        while len(lshape) < 3:
            lshape.append(1)

        if not inspect.isclass(dtype):
            raise TypeError(f"requires type annotation for data type")

        dd = extract_annot(dtype)
        if dd is None or not isinstance(dd, ValT):
            raise TypeError(f"invalid dtype '{dtype}' for field")

        self.info = ShapedFieldInfo(dd, tuple(lshape[:3]), desc)

    def __getitem__(self, time: int):
        return _FieldTimeSlice(
            TimedFieldInfo(self.info.dtype, self.info.shape, time, self.info.desc)
        )

    # make compiler happier
    def rearrange(self, idx: int, idy: int, idz: int, hx: int, hy: int, hz: int, inout: int):
        """
        Adds two integers.

        Args:
            idx (int): The first integer.

        Returns:
            int: The sum of a and b.

        Raises:
            TypeError: If a or b is not an integer.
        """
        pass

    def sum():
        pass

    def ncInit():
        pass

    def ncRead():
        pass

    def ncWrite():
        pass

    def boundary():
        pass


def _extract_annot_basic(a):
    if hasattr(a, "_hybrid"):
        # create a new hybridT
        hb = deepcopy(getattr(a, "_hybrid"))
        if not (isinstance(hb, HybridFieldT) or isinstance(hb, HybridT)):
            raise TypeError(f"invalid hybrid type '{hb}'")
        return hb

    if inspect.isclass(a):
        if issubclass(a, NumAnnot):
            return a.ANNOT_TYPE
        elif issubclass(a, String):
            return a.ANNOT_TYPE
        elif hasattr(a, "__orig_bases__"):
            # TODO: handle origin base classes
            pass

    return None


def extract_annot(a):
    if a is None:
        return VoidT()

    gorg = get_origin(a)
    if gorg != None and inspect.isclass(gorg) and issubclass(gorg, Field):
        args = get_args(a)
        if len(args) == 1 and inspect.isclass(args[0]):
            dtype = _extract_annot_basic(args[0])
            if dtype != None and isinstance(dtype, ValT):
                return FieldT(FieldRef(FieldInfo(dtype, None)))

    return _extract_annot_basic(a)


T = TypeVar("T")


def typecheck(t, v):
    if isinstance(t, IntT):
        if hasattr(v, "ANNOT_TYPE"):
            v = v.val
        return isinstance(v, int)
    elif isinstance(t, FloatT):
        if hasattr(v, "ANNOT_TYPE"):
            v = v.val
        return isinstance(v, float)
    elif isinstance(t, FieldT):
        return isinstance(v, Field) and t.info == v.info
    elif isinstance(t, (HybridT, HybridFieldT)):
        return hasattr(v.__class__, "_hybrid") and t == v.__class__._hybrid
    else:
        return False


def hybrid(cls: T) -> T:
    if not inspect.isclass(cls):
        raise Exception(f"unable to mark non-class type '{type(cls)}' hybrid")

    cls_annotations = cls.__dict__.get("__annotations__", {})
    fields = []
    for name, annot in cls_annotations.items():
        tt = extract_annot(annot)
        if tt is None:
            raise TypeError(f"field '{name}' is not a valid type '{annot.__dict__}'")
        fields.append((name, tt))

    def all(pred, iter):
        is_all = True
        for i in iter:
            is_all = is_all and pred(i)
        return is_all

    if all(lambda x: isinstance(x[1], ValT), fields):
        setattr(cls, "_hybrid", HybridT(tuple(fields), cls.__name__))
    elif all(lambda x: isinstance(x[1], AbsFieldT), fields):
        sf = HybridFieldT(tuple(fields), cls.__name__)
        setattr(cls, "_hybrid", sf)

        def gt(self, key):
            if not isinstance(key, int):
                raise TypeError(f"time slice could only be constant")
            return (key, self)

        setattr(cls, "__getitem__", gt)
    else:
        raise TypeError(f"unable to create hybrid type for '{cls.__name__}'")

    # create init function for hybrid type
    def init(self, *args):
        if len(args) != len(fields):
            raise TypeError(f"incompatiable length of fields to initialize hybrid type")
        for id, value in enumerate(args):
            fname, ftype = fields[id]
            if not typecheck(ftype, value):
                raise TypeError(f"incompatiable type '{ftype}' with '{value}'")
            setattr(self, fname, value)
        # IMPORTANT: create a new hybrid type whose fields are the same as its class
        # more consideraion(address info)
        setattr(self, "_hybrid", deepcopy(getattr(self, "_hybrid")))

    setattr(cls, "__init__", init)

    return cast(T, cls)


def is_hybrid(obj):
    return isinstance(getattr(obj, "_hybrid", None), HybridT)


def is_hybridfield(obj):
    return isinstance(getattr(obj, "_hybrid", None), HybridFieldT)


def iter_hybridfield(obj):
    assert is_hybridfield(obj), str(obj)

    hybridfield_info = cast(HybridFieldT, getattr(obj, "_hybrid"))

    for name, _ in hybridfield_info.items:
        value = getattr(obj, name)
        if isinstance(value, Field):
            yield (name, value)
        else:
            for sname, i in iter_hybridfield(value):
                yield (name + "." + sname, i)
