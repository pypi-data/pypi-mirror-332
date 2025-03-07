from dataclasses import dataclass, fields
import inspect
from enum import Enum
from typing import Dict, List, Optional, Tuple, Union, cast
from bamboo.lang.annot import extract_annot
from bamboo.lang.dtype import FieldT, HybridFieldT, UndefT, ValT, VoidT
from bamboo.lang.error import LangSyntaxError, LangTypeError, LangResolveError, Loc
from bamboo.lang.util import DictTuple


class IRPrinter:
    def __init__(self) -> None:
        self.ident = 0
        self.lines = []

    def writeln(self, line: str):
        self.lines.append(" " * self.ident + line)

    def __str__(self) -> str:
        return "\n".join(self.lines)


@dataclass
class IRNode:
    lineno: int

    def iter_fields(self):
        for field in fields(self):
            try:
                name = field.name
                yield name, getattr(self, name)
            except AttributeError:
                pass

    def print(self, printer: IRPrinter):
        pass


@dataclass
class Stat(IRNode):
    pass


@dataclass
class Expr(IRNode):
    def __post_init__(self):
        self.dtype: ValT = UndefT()


@dataclass
class Var:
    prefix: str
    name: str
    dtype: ValT

    def __str__(self) -> str:
        return f"{self.prefix}${self.name}"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Var) and __o.prefix == self.prefix and __o.name == self.name

    def __hash__(self) -> int:
        return (self.prefix, self.name).__hash__()


class MemCtx(Enum):
    Load = 0
    Store = 1


@dataclass
class FieldSlice:
    lineno: int
    field: FieldT
    ctx: MemCtx
    idx: List[Expr]
    attrs: Tuple[str, ...]


class IRCallable:
    __irtype__ = "ircallable"

    def __init__(self, func) -> None:
        self.func = func
        self.name = f"{func.__name__}<{self.__class__.__irtype__}>"

        src_fname = inspect.getsourcefile(func)
        self.file = "<unknown>" if src_fname is None else src_fname

        self._lineno_0 = inspect.getsourcelines(func)[1]
        self.lineno = 0

        self._tid = 0
        self._items: Dict[str, Union[Var, FieldT, HybridFieldT, FieldSlice]] = {}

        func_sig = inspect.signature(func)

        # extract return annotation to self.dtype
        ret_annot = func_sig.return_annotation
        if ret_annot == inspect.Signature.empty:
            ret_annot = None

        dtype = extract_annot(ret_annot)

        # check if return type is value
        if not isinstance(dtype, ValT):
            _tmsg = "Unknown" if dtype is None else dtype
            self.syntax_error(f"invalid return type '{_tmsg}', only value type is supported")

        self.dtype: ValT = dtype

        self.inline_fields: Dict[FieldT, List[FieldT]] = {}
        # extract function arguments into variables
        self.arg_vars: List[Tuple[str, Union[Var, FieldT]]] = []
        for farg_name, farg_param in func_sig.parameters.items():
            if farg_param.kind != inspect.Parameter.POSITIONAL_OR_KEYWORD:
                self.syntax_error(
                    f"invalid argument '{farg_name}', only positional or keyword is supported"
                )

            if farg_param.annotation == inspect.Parameter.empty:
                self.syntax_error(f"invalid argument '{farg_name}', only type annoted is supported")

            farg_type = extract_annot(farg_param.annotation)
            if farg_type is None or isinstance(farg_type, VoidT):
                _tmsg = "Unknown" if farg_type is None else farg_type
                self.syntax_error(
                    f"invalid argument type '{_tmsg}' for '{farg_name}', only concrete type is supported"
                )

            if isinstance(farg_type, HybridFieldT):
                # append arg name
                self._new_item(farg_name, farg_type)
                for field_name, field_type in farg_type.rec_iter("%"):
                    mangled_name = f"{farg_name}%{field_name}"
                    self.arg_vars.append(
                        (
                            mangled_name,
                            cast(
                                Union[Var, FieldT],
                                self._new_item(mangled_name, field_type),
                            ),
                        )
                    )
                    if isinstance(field_type, FieldT):
                        self.inline_fields[field_type] = [field_type]
            else:
                self.arg_vars.append(
                    (
                        farg_name,
                        cast(Union[Var, FieldT], self._new_item(farg_name, farg_type)),
                    )
                )
                if isinstance(farg_type, FieldT):
                    self.inline_fields[farg_type] = [farg_type]

        self.arg_type = DictTuple(
            tuple(
                map(
                    lambda x: (x[0], x[1].dtype if isinstance(x[1], Var) else x[1]),
                    self.arg_vars,
                )
            )
        )

        self.body: List[Stat] = []

    def _new_item(self, name: str, t: Union[ValT, FieldT, HybridFieldT]):
        if name in self._items:
            self.syntax_error(f"variable '{name}' is duplicated")
        if isinstance(t, ValT):
            v = Var(self.name, name, t)
            self._items[name] = v
            return v
        elif isinstance(t, FieldT):
            t.ref.local_name = name
            self._items[name] = t
            return t
        elif isinstance(t, HybridFieldT):
            self._items[name] = t
            t.local_name = name
            return t
        else:
            assert False

    def new_var(self, name: Optional[str] = None, t: Optional[ValT] = None):
        t = UndefT() if t is None else t

        temp = name is None

        if name is None:
            name = str(self._tid)
            self._tid += 1

        if name in self._items:
            self.syntax_error(f"variable '{name}' is duplicated")

        v = Var(self.name, name, t)

        # if not temporary item, then add it to items so that user could find it
        if not temp:
            self._items[name] = v

        return v

    def new_field_slice(self, name: str, t: FieldSlice):
        if name in self._items:
            self.syntax_error(f"field slice name '{name}' is duplicated")
        self._items[name] = t

    def get_var(self, name: str):
        if name in self._items:
            item = self._items[name]
            if isinstance(item, Var):
                return item
        return None

    def get_field_slice(self, name: str):
        if name in self._items:
            item = self._items[name]
            if isinstance(item, FieldSlice):
                return item
        return None

    def get_field(self, names: Union[Tuple[str, ...], str]):
        name = IRCallable._join_name(names)
        if name in self._items:
            item = self._items[name]
            if isinstance(item, FieldT) or isinstance(item, HybridFieldT):
                return item
        return None

    @staticmethod
    def _join_name(names: Union[Tuple[str, ...], str]):
        return "%".join(names) if isinstance(names, tuple) else names

    @property
    def loc(self):
        return Loc(self.file, self.name, self.lineno + self._lineno_0 - 1)

    def type_error(self, msg: str):
        raise LangTypeError(self.loc, msg)

    def syntax_error(self, msg: str):
        raise LangSyntaxError(self.loc, msg)

    def resolve_error(self, msg: str):
        raise LangResolveError(self.loc, msg)

    def new_stat(self, stat: Stat):
        self.body.append(stat)

    def __str__(self) -> str:
        printer = IRPrinter()

        printer.writeln(
            f"{self.dtype} {self.name}({', '.join(f'{t} {n}' for n, t in self.arg_type)}) {{"
        )
        printer.ident += 2
        for s in self.body:
            s.print(printer)
        printer.ident -= 2
        printer.writeln("}")

        return str(printer)


class IRSpace(IRCallable):
    __irtype__ = "space"

    def __init__(self, func) -> None:
        super().__init__(func)

        # check there's no return type
        if not isinstance(self.dtype, VoidT):
            self.syntax_error(
                f"invalid return type '{self.dtype}', only void is supported in space operator"
            )


class IRFunc(IRCallable):
    __irtype__ = "func"

    def __init__(self, func) -> None:
        super().__init__(func)

        # check there's no field type in arguments
        for arg_name, arg_type in self.arg_type:
            if isinstance(arg_type, FieldT):
                self.syntax_error(
                    f"invalid argument type '{arg_type}' for '{arg_name}', only value type is supported in func"
                )

        self.arg_type = cast(DictTuple[ValT], self.arg_type)


class IRExternFunc(IRCallable):
    __irtype__ = "extern_func"

    def __init__(self, func, avg_malloc, avg_mem, avg_flops, parallel, name) -> None:
        super().__init__(func)
        assert isinstance(avg_malloc, int)
        assert isinstance(avg_mem, int)
        assert isinstance(avg_flops, int)
        assert isinstance(parallel, bool)
        assert isinstance(name, str)
        self.avg_malloc = avg_malloc
        self.avg_mem = avg_mem
        self.avg_flops = avg_flops
        self.parallel = parallel
        self.name = name


class IRVisitor:
    def visit(self, ctx: IRCallable, ir: IRNode):
        ctx.lineno = ir.lineno
        visitor = getattr(self, "visit_" + ir.__class__.__name__, self.generic_visit)
        return visitor(ctx, ir)

    def generic_visit(self, ctx: IRCallable, ir: IRNode):
        for field, value in ir.iter_fields():
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, IRNode):
                        self.visit(ctx, item)
            elif isinstance(value, IRNode):
                self.visit(ctx, value)

    def __call__(self, ctx: IRCallable):
        for stat in ctx.body:
            self.visit(ctx, stat)


class IRTransformer(IRVisitor):
    def generic_visit(self, ctx: IRCallable, ir: IRNode):
        for field, old_value in ir.iter_fields():
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, IRNode):
                        value = self.visit(ctx, value)
                        if value is None:
                            continue
                        elif not isinstance(value, IRNode):
                            new_values.extend(value)
                            continue
                    if isinstance(value, list):
                        new_values.extend(value)
                    else:
                        new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, IRNode):
                new_node = self.visit(ctx, old_value)
                if new_node is None:
                    delattr(ir, field)
                else:
                    setattr(ir, field, new_node)
        return ir

    def __call__(self, ctx: IRCallable):
        new_stats = []
        for value in ctx.body:
            value = self.visit(ctx, value)
            if value is None:
                continue
            if isinstance(value, list):
                new_stats.extend(value)
            else:
                new_stats.append(value)
        ctx.body[:] = new_stats
