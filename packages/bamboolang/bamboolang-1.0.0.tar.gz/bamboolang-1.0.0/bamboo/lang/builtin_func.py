# import builtins
# import math
from bamboo.lang.dtype import IntT, FloatT, NumT, StrT, VoidT, FieldT, UndefT

# builtin_dirs = [getattr(builtins, _) for _ in dir(builtins)]
# builtin_dirs.extend([getattr(math, _) for _ in dir(math)])
# builtin_namelist = [func.__name__ for func in list(filter(isbuiltin, builtin_dirs))]

# name : (args, ret), undef refs to dtype of a field
builtin_list = {
    # 'abs', 'hash', 'hex', 'max', 'min',
    # 'sum' 'acos', 'acosh', 'asin', 'asinh',
    # 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
    # 'cos', 'cosh', 'degrees', 'erf', 'erfc',
    # 'exp', 'expm1', 'fabs', 'factorial', 'floor',
    # 'fmod', 'frexp', 'fsum', 'gamma', 'gcd',
    # 'hypot', 'isclose', 'isfinite', 'isinf', 'isnan',
    # 'ldexp', 'lgamma', 'log', 'log10', 'log1p',
    # 'log2', 'modf', 'pow', 'radians', 'remainder',
    # 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc'
    "abs": ([("arg1", FloatT(64))], FloatT(64)),
    "min": ([("arg1", FloatT(64)), ("arg2", FloatT(64))], FloatT(64)),
    "max": ([("arg1", FloatT(64)), ("arg2", FloatT(64))], FloatT(64)),
    "sum": ([("arg1", FloatT(64)), ("arg2", FloatT(64))], FloatT(64)),
    "acos": ([("arg1", FloatT(64))], FloatT(64)),
    "acosh": ([("arg1", FloatT(64))], FloatT(64)),
    "asin": ([("arg1", FloatT(64))], FloatT(64)),
    "asinh": ([("arg1", FloatT(64))], FloatT(64)),
    "atan": ([("arg1", FloatT(64))], FloatT(64)),
    "atan2": ([("y", FloatT(64)), ("x", FloatT(64))], FloatT(64)),
    "atanh": ([("arg1", FloatT(64))], FloatT(64)),
    "cos": ([("arg1", FloatT(64))], FloatT(64)),
    "cosh": ([("arg1", FloatT(64))], FloatT(64)),
    "sin": ([("arg1", FloatT(64))], FloatT(64)),
    "sinh": ([("arg1", FloatT(64))], FloatT(64)),
    "tan": ([("arg1", FloatT(64))], FloatT(64)),
    "tanh": ([("arg1", FloatT(64))], FloatT(64)),
    "log": ([("arg1", FloatT(64))], FloatT(64)),
    "log2": ([("arg1", FloatT(64))], FloatT(64)),
    "log10": ([("arg1", FloatT(64))], FloatT(64)),
    "ceil": ([("arg1", FloatT(64))], IntT(32)),
    "floor": ([("arg1", FloatT(64))], IntT(32)),
    "trunc": ([("arg1", FloatT(64))], IntT(32)),
    "exp": ([("pow", FloatT(64))], FloatT(64)),
    "sqrt": ([("arg1", FloatT(64))], FloatT(64)),
    "fabs": ([("arg1", FloatT(64))], FloatT(64)),
    "isinf": ([("arg1", FloatT(64))], IntT(1)),
    "isnan": ([("arg1", FloatT(64))], IntT(1)),
}

# TODO: ret type of builtins
builtin_ret_type = {
    "isclose": IntT(1),
    "isfinite": IntT(1),
    "isinf": IntT(1),
    "isnan": IntT(1),
    "ceil": IntT(32),
    "floor": IntT(32),
    "trunc": IntT(32),
}

# name : (args, ret), undef refs to dtype of a field
field_methods = {
    "rearrange": (
        [
            ("idx", IntT(32)),
            ("idy", IntT(32)),
            ("idz", IntT(32)),
            ("hx", IntT(32)),
            ("hy", IntT(32)),
            ("hz", IntT(32)),
            ("inout", IntT(32)),
        ],
        VoidT(),
    ),
    "sum": (
        [
            ("lev", IntT(1)),
            ("lev_st", IntT(32)),
            ("lev_ed", IntT(32)),
            ("lat", IntT(1)),
            ("lat_st", IntT(32)),
            ("lat_ed", IntT(32)),
            ("lon", IntT(1)),
            ("lon_st", IntT(32)),
            ("lon_ed", IntT(32)),
        ],
        VoidT(),
    ),
    "ncInit": ([], VoidT()),
    "ncRead": ([("file_id", IntT(32))], VoidT()),
    "ncWrite": ([("file_id", IntT(32))], VoidT()),
}

hybrid_field_methods = {
    "ncInit": ([], VoidT()),
    "ncRead": ([("file_id", IntT(32))], VoidT()),
    "ncWrite": ([("file_id", IntT(32))], VoidT()),
}
