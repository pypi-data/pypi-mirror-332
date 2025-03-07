from bamboo.lang.annot import (
    Bool,
    Int8,
    Int16,
    Int32,
    Int64,
    Float16,
    Float32,
    Float64,
    String,
    Field,
    hybrid,
)
from bamboo.lang.op import FuncOp, SpaceOp, TimeOp, ExternFuncOp


def time_op(timelength, timestep):
    def inner(f):
        return TimeOp(f, timelength, timestep)

    return inner


def space_op(f):
    return SpaceOp(f)


def func(f):
    return FuncOp(f)


def extern_func(avg_malloc, avg_mem, avg_flops, parallel, name=""):
    def inner(f):
        return ExternFuncOp(f, avg_malloc, avg_mem, avg_flops, parallel, name)

    return inner


def const_init(f):
    setattr(f, "const", True)
    return f


__all__ = [
    "Bool",
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "Float16",
    "Float32",
    "Float64",
    "String",
    "Field",
    "time_op",
    "space_op",
    "func",
    "extern_func",
]
