import ast
import sys
from copy import deepcopy
from warnings import warn

# from astpretty import pprint
from typing import Union, List
from inspect import getsource, ismodule, isbuiltin, isclass
from enum import Enum
from bamboo.lang.builtin_func import builtin_list, field_methods, hybrid_field_methods
from bamboo.lang.annot import NumAnnot
from bamboo.lang.dtype import HybridFieldT, FloatT, FieldT, IntT, UndefT
from bamboo.lang.ir import IRCallable, IRExternFunc, IRFunc, IRSpace, Var, FieldSlice
from bamboo.lang.ir.expr import (
    BoolOp,
    CallExpr,
    Expr,
    AttrExpr,
    ExternCallExpr,
    ExternCallMethod,
    IntExpr,
    FloatExpr,
    CastExpr,
    BinExpr,
    FieldExpr,
    FieldCallExpr,
    MemCtx,
    ShapeExpr,
    StrExpr,
    UniExpr,
    BinOp,
    CompOp,
    UniOp,
    IRStub,
)
from bamboo.lang.ir.stat import (
    ExprStat,
    IfStat,
    SpaceStat,
    Stat,
    RetStat,
    PassStat,
    AssignStat,
    ForStat,
)


class IRBuilder:
    def __call__(self, ctx: IRCallable):
        """parse source code and return a new AST using our intermediate representation"""
        if sys.version_info.major < 3:
            raise Exception("only supports python 3")
        else:
            assert sys.version_info.major == 3
            if sys.version_info.minor != 7:
                warn("only python 3.7 is tested", DeprecationWarning)
            ast_root = ast.parse(getsource(ctx.func))
        self.scopes = [ctx.body]
        self.visit(ctx, ast_root.body[0])
        return ctx

    def visit(self, ctx: IRCallable, node: ast.AST):
        ctx.lineno = node.lineno
        method = getattr(self, "visit_" + node.__class__.__name__, None)
        if method is None:
            ctx.syntax_error(f"invalid node type '{node.__class__.__name__}', unsupported")
        return method(ctx, node)

    def _append_stat(self, ctx: IRCallable, stat: Stat) -> None:
        if isinstance(stat, Stat):
            self.scopes[-1].append(stat)
        elif isinstance(stat, CallExpr):
            self.scopes[-1].append(ExprStat(stat.lineno, stat))
        else:
            ctx.syntax_error("please clean unused expression")

    def _append_stats(self, ctx: IRCallable, stats: Union[Stat, List[Stat]]) -> None:
        if isinstance(stats, list):
            for stat in stats:
                self._append_stat(ctx, stat)
        else:
            self._append_stat(ctx, stats)

    def _get_memctx(self, node) -> MemCtx:
        # del is not supported
        return MemCtx.Load if isinstance(node.ctx, ast.Load) else MemCtx.Store

    def _fexpr2fslice(self, fexpr: FieldExpr) -> FieldSlice:
        return FieldSlice(fexpr.lineno, fexpr.field, fexpr.ctx, fexpr.idx, fexpr.attrs)

    def _fslice2fexpr(self, fslice: FieldSlice) -> FieldExpr:
        return FieldExpr(fslice.lineno, fslice.field, fslice.ctx, fslice.idx, fslice.attrs)

    def _slice_flag(self, lineno: int) -> IntExpr:
        return IntExpr(lineno, -1)

    def _is_slice_flag(self, expr: Expr) -> bool:
        return isinstance(expr, IntExpr) and expr.val == -1

    def _get_slice_dim(self, slice: Union[FieldExpr, FieldSlice]) -> int:
        if isinstance(slice, FieldSlice):
            slice = self._fslice2fexpr(slice)
        dim = 0
        for expr in slice.idx:
            if self._is_slice_flag(expr):
                dim += 1
        return dim

    def _is_field(self, ctx: IRCallable, slice: Union[Expr, FieldSlice]) -> bool:
        if not (isinstance(slice, FieldExpr) or isinstance(slice, FieldSlice)):
            return False
        if isinstance(slice.field, HybridFieldT):
            try:
                field = self._get_field_member(ctx, slice)
                return not isinstance(field, HybridFieldT) and 0 < self._get_slice_dim(slice) <= 3
            except:
                return False
        elif isinstance(slice.field, FieldT):
            return len(slice.attrs) == 0 and 0 < self._get_slice_dim(slice) <= 3
        else:
            assert False

    def _is_field_slice(self, ctx: IRCallable, slice: Union[Expr, FieldSlice]) -> bool:
        return self._is_field(ctx, slice) and 0 < self._get_slice_dim(slice) < 3

    def _is_full_field(self, ctx: IRCallable, slice: Union[Expr, FieldSlice]) -> bool:
        return self._is_field(ctx, slice) and 0 < self._get_slice_dim(slice) == 3

    def _fill_in_slice_idx(self, ctx: IRCallable, idx: List[Expr], fill: List[Expr]) -> None:
        if len(fill) == 0:
            ctx.syntax_error("please fill in at least one dimension of a field (slice)")
        lineno = fill[0].lineno
        for id in range(len(idx)):
            if self._is_slice_flag(idx[id]):
                if len(fill) == 0:
                    fill.append(IntExpr(lineno, 0))
                    # ctx.syntax_error(
                    #     "please fill in all dimensions of a field (slice)")
                idx[id] = fill.pop(0)
        # To Check!!!
        # 为了拓展立方球的panel维，去掉了3维的检查
        if len(fill) > 0:
            pass
            # self._field_dim_exceed(ctx)

    def _field_op_guard(self, ctx: IRCallable, expr: Union[Expr, FieldSlice]):
        if self._is_field(ctx, expr):
            ctx.syntax_error("field can not be an operand")

    def _field_syntax_error(self, ctx: IRCallable):
        ctx.syntax_error("unrecongnized field pattern")

    def _field_dim_exceed(self, ctx: IRCallable):
        ctx.syntax_error("fields can only have 1, 2 or 3 dimensions")

    # def _get_slice_idx(self, ctx: IRCallable, node: ast.Index) -> List[Expr]:
    #     if isinstance(node.value, ast.Tuple):
    #         return self.visit(ctx, node.value)
    #     elif isinstance(node.value, ast.Num) or isinstance(node.value, ast.BinOp):
    #         return [self.visit(ctx, node.value)]
    #     else:
    #         self._field_syntax_error(ctx)

    def _new_fslice(self, ctx: IRCallable, name: str, slice: Union[FieldExpr, FieldSlice]) -> None:
        if isinstance(slice, FieldSlice):
            ctx.new_field_slice(name, slice)
        elif isinstance(slice, FieldExpr):
            ctx.new_field_slice(name, self._fexpr2fslice(slice))
        else:
            raise Exception("unknown error")

    def _get_field_member(self, ctx: IRCallable, fexpr: FieldExpr) -> FieldT:
        field = fexpr.field
        attrs = list(fexpr.attrs)
        if len(attrs) == 0:
            mangle_name = field.local_name
        else:
            mangle_name = field.local_name + "%" + "%".join(attrs)
        ptr = ctx.get_field(mangle_name)
        if ptr is None:
            name_to_print = mangle_name.replace("%", ".")
            ctx.resolve_error(f"no such field {name_to_print} (type must be Float, Int or Bool)")
        return ptr

    # ========= expressions ========
    def find_field(self, ctx: IRCallable, node: ast.Name) -> FieldExpr:
        field = ctx.get_field(node.id)
        if field is not None:
            return FieldExpr(
                node.lineno,
                field,
                self._get_memctx(node),
                [
                    self._slice_flag(node.lineno),
                    self._slice_flag(node.lineno),
                    self._slice_flag(node.lineno),
                ],
                (),
            )
        slice = ctx.get_field_slice(node.id)
        if slice is not None:
            return self._fslice2fexpr(slice)
        return None

    def find_or_create(self, ctx: IRCallable, node: ast.Name) -> Union[Var, FieldExpr]:
        obj = ctx.func.__globals__.get(node.id)
        try:
            mod_func_var = self._check_mod_func_var(ctx, node, obj)
            return mod_func_var
        except:
            field = self.find_field(ctx, node)
            if field is not None:
                return field
            var = ctx.get_var(node.id)
            if var is not None:
                return var
            else:
                return ctx.new_var(node.id, None)

    def visit_Name(self, ctx: IRCallable, node: ast.Name) -> Union[AttrExpr, FieldExpr]:
        obj = self.find_or_create(ctx, node)
        if isinstance(obj, FieldExpr):
            return self._fslice2fexpr(obj)
        elif isinstance(obj, Var):
            return AttrExpr(node.lineno, obj, self._get_memctx(node), ())
        else:
            return obj

    def visit_NameConstant(
        self, ctx: IRCallable, node: ast.NameConstant
    ) -> Union[IntExpr, FloatExpr]:
        # True -> 1, False -> 0
        if node.value == True:
            return IntExpr(node.lineno, 1, 1)
        elif node.value == False:
            return IntExpr(node.lineno, 0, 1)
        elif node.value == None:
            ctx.syntax_error("currently 'None' is not supported")
        else:
            ctx.syntax_error("unknown ast.NameConstant")

    def visit_Num(self, ctx: IRCallable, node: ast.Num) -> Union[IntExpr, FloatExpr]:
        literal = node.n
        if isinstance(literal, int):
            return IntExpr(node.lineno, literal)
        elif isinstance(literal, float):
            return FloatExpr(node.lineno, literal)
        else:
            ctx.syntax_error("impossible")

    def visit_Constant(self, ctx: IRCallable, node: ast.Constant):
        v = node.value
        if isinstance(v, bool):
            return IntExpr(node.lineno, int(v), 1)
        elif isinstance(v, int):
            return IntExpr(node.lineno, v)
        elif isinstance(v, float):
            return FloatExpr(node.lineno, v)
        else:
            ctx.syntax_error(f"unsupported constant '{v}'")

    def visit_Str(self, ctx: IRCallable, node: ast.Str):
        return StrExpr(node.lineno, node.s)

    class OperatorMapping:
        """
        binary operator transfromation (python->intermediate)
        class Add(operator): ... -> BinaryOp.Add
        class BitAnd(operator): ... -> BinaryOp.BitAnd
        class BitOr(operator): ... -> BinaryOp.BitOr
        class BitXor(operator): ... -> BinaryOp.BitXor
        class Div(operator): ... -> BinaryOp.Divide
        class FloorDiv(operator): ...
        class LShift(operator): ...
        class Mod(operator): ... -> BinaryOp.Modulo
        class Mult(operator): ... -> BinaryOp.Multiply
        class MatMult(operator): ...
        class Pow(operator): ... -> BinaryOp.Power
        class RShift(operator): ...
        class Sub(operator): ... -> BinaryOp.Subtract

        comparison operator transfromation (python->intermediate)
        class Eq(cmpop): ... -> CompOp.Eq
        class Gt(cmpop): ... -> CompOp.Gt
        class GtE(cmpop): ... ->CompOp.Ge
        class In(cmpop): ...
        class Is(cmpop): ...
        class IsNot(cmpop): ...
        class Lt(cmpop): ... -> CompOp.Lt
        class LtE(cmpop): ... -> CompOp.Le
        class NotEq(cmpop): ... -> CompOp.Ne
        class NotIn(cmpop): ...

        boolean operator transfromation (python->intermediate)
        class boolop(AST): ...
        class And(boolop): ... -> BoolOp.And
        class Or(boolop): ... -> BoolOp.Or

        unary operator transfromation (python->intermediate)
        class Invert(unaryop): ...
        class Not(unaryop): ... -> UnaryOp.Not
        class UAdd(unaryop): ...
        class USub(unaryop): ... -> UnaryOp.Neg
        """

        map = {
            # binary operator
            ast.Add: BinOp.Add,
            ast.Div: BinOp.Div,
            ast.Mod: BinOp.Mod,
            ast.Mult: BinOp.Mul,
            ast.Pow: BinOp.Pow,
            ast.Sub: BinOp.Sub,
            ast.BitAnd: BinOp.BitAnd,
            ast.BitOr: BinOp.BitOr,
            ast.BitXor: BinOp.BitXor,
            # comparison operator
            ast.Eq: CompOp.Eq,
            ast.Gt: CompOp.Gt,
            ast.GtE: CompOp.Ge,
            ast.Lt: CompOp.Lt,
            ast.LtE: CompOp.Le,
            ast.NotEq: CompOp.Ne,
            # boolean opeartor
            ast.Or: BoolOp.Or,
            ast.And: BoolOp.And,
            # unary operator
            ast.Not: UniOp.Not,
            ast.USub: UniOp.Neg,
        }

    def visit_Expr(self, ctx: IRCallable, node: ast.Expr) -> Expr:
        return self.visit(ctx, node.value)

    def visit_BinOp(self, ctx: IRCallable, node: ast.BinOp) -> BinExpr:
        try:
            op = self.OperatorMapping.map[node.op.__class__]
        except:
            ctx.syntax_error(f"unsupported binary operator {node.op.__class__}")
        lhs = self.visit(ctx, node.left)
        rhs = self.visit(ctx, node.right)
        self._field_op_guard(ctx, lhs)
        self._field_op_guard(ctx, rhs)
        return BinExpr(node.lineno, lhs, rhs, op)

    def visit_Compare(self, ctx: IRCallable, node: ast.Compare) -> List[BinExpr]:
        lhs = self.visit(ctx, node.left)
        self._field_op_guard(ctx, lhs)
        ret = None
        for id in range(len(node.ops)):
            try:
                op = self.OperatorMapping.map[node.ops[id].__class__]
            except:
                ctx.syntax_error(f"unsupported comparison operator {node.ops[id].__class__}")
            rhs = self.visit(ctx, node.comparators[id])
            self._field_op_guard(ctx, rhs)
            if ret is None:
                ret = BinExpr(node.lineno, lhs, rhs, op)
            else:
                ret = BinExpr(node.lineno, ret, BinExpr(node.lineno, lhs, rhs, op), BoolOp.And)
            lhs = rhs
        return ret

    def visit_BoolOp(self, ctx: IRCallable, node: ast.BoolOp) -> BinExpr:
        try:
            op = self.OperatorMapping.map[node.op.__class__]
        except:
            ctx.syntax_error(f"unsupported boolean operator {node.op.__class__}")
        lhs = self.visit(ctx, node.values[0])
        self._field_op_guard(ctx, lhs)
        for value in node.values[1:]:
            rhs = self.visit(ctx, value)
            self._field_op_guard(ctx, rhs)
            lhs = BinExpr(node.lineno, lhs, rhs, op)
        return lhs

    def visit_UnaryOp(self, ctx: IRCallable, node: ast.UnaryOp) -> UniExpr:
        try:
            op = self.OperatorMapping.map[node.op.__class__]
        except:
            ctx.syntax_error(f"unsupported unary operator {node.op.__class__}")
        rhs = self.visit(ctx, node.operand)
        self._field_op_guard(ctx, rhs)
        return UniExpr(node.lineno, rhs, op)

    def _is_IRCallable(self, obj):
        return hasattr(obj, "build")

    def _is_hybrid_class(self, obj):
        return isclass(obj) and hasattr(obj, "_hybrid")

    def _is_builtin(self, name):
        return name in builtin_list.keys()

    def _is_field_method(self, name):
        return name in field_methods.keys()

    def _check_mod_func_var(self, ctx: IRCallable, node: ast.AST, mod_func_var):
        if isinstance(node, ast.Name):
            attr = node.id
        elif isinstance(node, ast.Attribute):
            attr = node.attr
        else:
            assert False

        if isinstance(mod_func_var, int):  # global constants
            return IntExpr(node.lineno, mod_func_var, 32)
        elif isinstance(mod_func_var, float):
            return FloatExpr(node.lineno, mod_func_var, 64)
        elif isinstance(mod_func_var, str):
            return StrExpr(node.lineno, mod_func_var)
        elif isbuiltin(mod_func_var):  # builtins
            func_name = mod_func_var.__name__
            if self._is_builtin(func_name):
                return IRStub(func_name, None, None)
            else:
                ctx.resolve_error(f"{func_name} is not a builtin function: {builtin_list.keys()}")
        elif self._is_hybrid_class(mod_func_var) or (
            isclass(mod_func_var)
            and (issubclass(mod_func_var, NumAnnot) or issubclass(mod_func_var, Enum))
        ):
            return mod_func_var
        elif ismodule(mod_func_var) or self._is_IRCallable(mod_func_var):
            return mod_func_var
        else:
            ctx.syntax_error(f"unknown object '{mod_func_var}'")

    def visit_Attribute(
        self, ctx: IRCallable, node: ast.Attribute
    ) -> Union[AttrExpr, FieldExpr, ShapeExpr, IntExpr, FloatExpr]:
        def _append_attr(expr: Expr, attr: str):
            expr.attrs = tuple(list(expr.attrs) + [attr])
            return expr

        obj_or_expr = self.visit(ctx, node.value)
        if isinstance(obj_or_expr, AttrExpr):  # var
            return _append_attr(obj_or_expr, node.attr)
        elif isinstance(obj_or_expr, FieldExpr):  # field or field slice
            if node.attr in ["shape_x", "shape_y", "shape_z"]:
                field = self._get_field_member(ctx, obj_or_expr)
                return ShapeExpr(
                    node.lineno,
                    field,
                    ["shape_x", "shape_y", "shape_z"].index(node.attr),
                )
            elif self._is_field(ctx, obj_or_expr) and not self._is_field_method(node.attr):
                obj_or_expr.field = self._get_field_member(ctx, obj_or_expr)
                obj_or_expr.attrs = ()
                ctx.syntax_error(
                    f"the field(slice) {str(obj_or_expr)} has no attribute '{node.attr}'"
                )
            else:
                return _append_attr(obj_or_expr, node.attr)
        elif self._is_IRCallable(obj_or_expr):  # IRCallables
            func = obj_or_expr
            if not hasattr(func, "callable"):
                func.build()
            if isinstance(func.callable, IRExternFunc):
                if node.attr not in ["init", "run", "finalize"]:
                    ctx.resolve_error("external function only has init, run and finalize method")
                return IRStub(
                    [
                        ExternCallMethod.INIT,
                        ExternCallMethod.RUN,
                        ExternCallMethod.FINALIZE,
                    ][["init", "run", "finalize"].index(node.attr)],
                    None,
                    func,
                )
            else:
                assert isinstance(func.callable, IRSpace) or isinstance(func.callable, IRFunc)
                ctx.resolve_error(f"{func.callable.name} has no method {node.attr}")
        elif ismodule(obj_or_expr):
            mod_func_var = getattr(obj_or_expr, node.attr)
            return self._check_mod_func_var(ctx, node, mod_func_var)
        elif isclass(obj_or_expr) and issubclass(obj_or_expr, Enum):  #  get enum value
            return getattr(obj_or_expr, node.attr)
        elif isinstance(obj_or_expr, Enum):
            val = obj_or_expr.value
            if isinstance(val, int):
                return IntExpr(node.lineno, val)
            elif isinstance(val, float):
                return FloatExpr(node.lineno, val)
            elif isinstance(val, str):
                return StrExpr(node.lineno, val)
            else:
                ctx.syntax_error(
                    f"the field '{obj_or_expr.name}' of enum type {obj_or_expr.__class__} must a int/float/str instead of {val.__class__}"
                )
        else:
            ctx.resolve_error(f"{obj_or_expr} has no attribute {node.attr}")

    def visit_Tuple(self, ctx: IRCallable, node: ast.Tuple) -> List[AttrExpr]:
        exprs = list()
        for elt in node.elts:
            expr = self.visit(ctx, elt)
            exprs.append(expr)
        return exprs

    def _try_flatten_hybrid(self, args):
        flattened_args = list()
        for arg in args:
            if isinstance(arg, HybridFieldT):
                for field_name, field_type in arg.rec_iter("%"):
                    flattened_args.append(field_type)
            else:
                flattened_args.append(arg)
        return flattened_args

    def visit_Call(self, ctx: IRCallable, node: ast.Call) -> Union[CallExpr, SpaceStat]:
        args = list()
        for arg_node in node.args:
            arg = self.visit(ctx, arg_node)
            if self._is_field_slice(ctx, arg):
                ctx.syntax_error("field slice can not be an argument")
            elif self._is_full_field(ctx, arg):
                # resolve hybrid field member
                arg = self._get_field_member(ctx, arg)
            elif isinstance(arg, FieldExpr) and isinstance(arg.field, HybridFieldT):
                arg = arg.field
            args.append(arg)
        if not (isinstance(node.func, ast.Name) or isinstance(node.func, ast.Attribute)):
            ctx.resolve_error(f"unresolved function call")
        if isinstance(node.func, ast.Name) and self._is_builtin(node.func.id):  # sum = 2 vs sum()
            func_name = node.func.id
            obj_or_expr = IRStub(func_name, None, FloatT(64))
        else:
            obj_or_expr = self.visit(ctx, node.func)
        if self._is_IRCallable(obj_or_expr):
            if not hasattr(obj_or_expr, "callable"):
                obj_or_expr.build()
            ir_func = obj_or_expr.callable
            if isinstance(ir_func, IRSpace):
                # return SpaceStat(node.lineno, ir_func, self._try_flatten_hybrid(args))
                # use deepcopy to avoid bugs when inlining the same space op with different parameters
                return SpaceStat(node.lineno, deepcopy(ir_func), self._try_flatten_hybrid(args))

            elif isinstance(ir_func, IRFunc):
                return CallExpr(node.lineno, ir_func, args)
            elif isinstance(ir_func, IRExternFunc):
                return CallExpr(node.lineno, ir_func, args)
            else:
                assert False
        elif isinstance(obj_or_expr, IRStub):
            if isinstance(obj_or_expr.name, ExternCallMethod):  # IRExternFunc
                extern_func = obj_or_expr.dtype.callable
                call_method = obj_or_expr.name
                return ExternCallExpr(node.lineno, extern_func, args, call_method)
            else:  # builtins
                obj_or_expr.arg_type = builtin_list[obj_or_expr.name][0]
                obj_or_expr.dtype = builtin_list[obj_or_expr.name][1]
                return CallExpr(node.lineno, obj_or_expr, args)
        elif self._is_hybrid_class(obj_or_expr):  # hybrid class construction
            dtype = getattr(obj_or_expr, "_hybrid")
            stub = IRStub(obj_or_expr.__name__, dtype.items, dtype)
            return CallExpr(node.lineno, stub, args)
        elif isclass(obj_or_expr) and issubclass(obj_or_expr, NumAnnot):  # basic types
            assert len(args) == 1
            if (isinstance(args[0], FloatExpr) and isinstance(obj_or_expr.ANNOT_TYPE, FloatT)) or (
                isinstance(args[0], IntExpr) and isinstance(obj_or_expr.ANNOT_TYPE, IntT)
            ):
                args[0].length = obj_or_expr.ANNOT_TYPE.bits_width
                return args[0]
            else:
                return CastExpr(node.lineno, args[0], obj_or_expr.ANNOT_TYPE)
        elif isinstance(obj_or_expr, FieldExpr):
            method = obj_or_expr.attrs[-1]
            obj_or_expr.attrs = obj_or_expr.attrs[:-1]
            obj_or_expr.field = self._get_field_member(ctx, obj_or_expr)
            obj_or_expr.attrs = ()
            if isinstance(obj_or_expr.field, HybridFieldT):
                if not method in hybrid_field_methods.keys():
                    ctx.syntax_error("hybrid field is not callable")
                call_exprs = []
                for field_name, field_type in obj_or_expr.field.rec_iter("%"):
                    stub = IRStub(
                        method,
                        field_methods[method][0],
                        (
                            field_type.dtype
                            if field_methods[method][1] == UndefT()
                            else field_methods[method][1]
                        ),
                    )
                    call_exprs.append(
                        FieldCallExpr(
                            node.lineno,
                            stub,
                            args,
                            FieldExpr(
                                node.lineno,
                                field_type,
                                obj_or_expr.ctx,
                                obj_or_expr.idx,
                                (),
                            ),
                        )
                    )
                return call_exprs
            else:
                stub = IRStub(
                    method,
                    field_methods[method][0],
                    (
                        obj_or_expr.field.dtype
                        if field_methods[method][1] == UndefT()
                        else field_methods[method][1]
                    ),
                )
                return FieldCallExpr(node.lineno, stub, args, obj_or_expr)
        else:
            ctx.resolve_error(f"unresolved function call")

    def visit_Subscript(self, ctx: IRCallable, node: ast.Subscript) -> FieldExpr:
        if isinstance(node.value, ast.Name):
            field = self.find_field(ctx, node.value)
        elif isinstance(node.value, ast.Attribute):
            field = self.visit(ctx, node.value)
            assert isinstance(field, FieldSlice) or isinstance(field, FieldExpr)
            field.field = self._get_field_member(ctx, field)
            field.attrs = ()
        else:
            self._field_syntax_error(ctx)
        if field is None:
            ctx.syntax_error(f"unregistered field (slice) {node.value.id}")
        if not isinstance(field, FieldExpr):
            self._field_syntax_error(ctx)
        if isinstance(node.slice, ast.Index):
            # field load or store
            idx = list(field.idx)
            fill = self.visit(ctx, node.slice.value)
            if not isinstance(fill, list):
                fill = [fill]
            self._fill_in_slice_idx(ctx, idx, fill)
            return FieldExpr(node.lineno, field.field, self._get_memctx(node), idx, field.attrs)
        elif isinstance(node.slice, ast.Slice):
            if not (
                node.slice.lower is None and node.slice.upper is None and node.slice.step is None
            ):
                raise ctx.syntax_error("only fully slicing is supported")
            idx = list(field.idx)
            self._fill_in_slice_idx(ctx, idx, [self._slice_flag(node.lineno)])
            return FieldExpr(node.lineno, field.field, self._get_memctx(node), idx, field.attrs)
        elif isinstance(node.slice, ast.ExtSlice):
            idx = list(field.idx)
            fill = []
            for dim in node.slice.dims:
                if isinstance(dim, ast.Slice):
                    if not (dim.lower is None and dim.upper is None and dim.step is None):
                        raise ctx.syntax_error("only fully slicing is supported")
                    fill.append(self._slice_flag(node.lineno))
                else:
                    fill.append(self.visit(ctx, dim.value))
            self._fill_in_slice_idx(ctx, idx, fill)
            return FieldExpr(node.lineno, field.field, self._get_memctx(node), idx, field.attrs)
        else:
            self._field_syntax_error(ctx)

    # ========= statements =========
    def visit_FunctionDef(self, ctx: IRCallable, node: ast.FunctionDef) -> None:
        # params = tuple(map(lambda x: (x.arg, None), node.args.args))
        for sentence in node.body:
            stats = self.visit(ctx, sentence)
            self._append_stats(ctx, stats)

    def visit_Return(self, ctx: IRCallable, node: ast.Return) -> RetStat:
        expr = self.visit(ctx, node.value)
        return RetStat(node.lineno, expr)

    def visit_Pass(self, ctx: IRCallable, node: ast.Pass) -> PassStat:
        pass

    def _is_constexpr(self, val: Expr):
        return isinstance(val, IntExpr) or isinstance(val, FloatExpr) or isinstance(val, ShapeExpr)

    def _field_assign(
        self, ctx: IRCallable, lineno: int, val: Expr, fexpr: FieldExpr
    ) -> List[Union[AssignStat, ForStat]]:
        if isinstance(val, FieldExpr):
            ctx.syntax_error(f"can not assign field {val.field} to another field {fexpr.field}")
        stats = list()
        if not self._is_constexpr(val):
            tmp_var = ctx.new_var(None)
            # field slice aug assignment
            if isinstance(val, BinExpr) and isinstance(val.lhs, FieldExpr):
                if val.lhs.field != fexpr.field:
                    ctx.syntax_error(
                        f"only support aug-assign for a field, operations between {val.lhs.field} and {fexpr.field} are not allowed"
                    )
                stats.append(
                    AssignStat(lineno, val.rhs, AttrExpr(lineno, tmp_var, MemCtx.Store, ()))
                )
            else:
                stats.append(AssignStat(lineno, val, AttrExpr(lineno, tmp_var, MemCtx.Store, ())))
        # resolve hybrid field
        field = self._get_field_member(ctx, fexpr)
        for_stat = None
        new_idx = list()
        for i, id_expr in enumerate(fexpr.idx):
            if self._is_slice_flag(id_expr):
                loop_var = ctx.new_var(None)
                new_idx.append(AttrExpr(lineno, loop_var, MemCtx.Load, ()))
                if for_stat is None:
                    for_stat = ForStat(
                        lineno,
                        loop_var,
                        IntExpr(lineno, 0),
                        IntExpr(lineno, 1),
                        ShapeExpr(lineno, field, i),
                        [],
                    )
                    stats.append(for_stat)
                else:
                    next_for_stat = ForStat(
                        lineno,
                        loop_var,
                        IntExpr(lineno, 0),
                        IntExpr(lineno, 1),
                        ShapeExpr(lineno, field, i),
                        [],
                    )
                    for_stat.body.append(next_for_stat)
                    for_stat = next_for_stat
            else:
                new_idx.append(id_expr)
        dst = FieldExpr(lineno, field, MemCtx.Store, new_idx, ())
        if self._is_constexpr(val):
            for_stat.body.append(AssignStat(lineno, val, dst))
        elif isinstance(val, BinExpr) and isinstance(val.lhs, FieldExpr):
            # field slice aug assignment
            assert val.lhs.field == fexpr.field
            val.lhs = FieldExpr(lineno, field, MemCtx.Load, new_idx, ())
            val.rhs = AttrExpr(lineno, tmp_var, MemCtx.Load, ())
            for_stat.body.append(AssignStat(lineno, val, dst))
        else:
            for_stat.body.append(
                AssignStat(lineno, AttrExpr(lineno, tmp_var, MemCtx.Load, ()), dst)
            )
        return stats

    def _visit_single_val_Assign(
        self, ctx: IRCallable, lineno: int, val_expr: Expr, targets: List[ast.AST]
    ) -> List[AssignStat]:
        stats = list()
        for target in reversed(targets):
            if self._is_field_slice(ctx, val_expr):
                # do not visit ast.Name, it will create a new variable
                if not isinstance(target, ast.Name):
                    ctx.syntax_error("unrecongnized field slice assignment")
                self._new_fslice(ctx, target.id, val_expr)
            else:
                var_expr = self.visit(ctx, target)
                if self._is_field(ctx, var_expr):
                    stats.extend(self._field_assign(ctx, lineno, val_expr, var_expr))
                elif isinstance(var_expr, ShapeExpr):
                    ctx.syntax_error("field shape can not be a lvalue")
                else:
                    stats.append(AssignStat(lineno, val_expr, var_expr))
        return stats

    def visit_Assign(self, ctx: IRCallable, node: ast.Assign) -> List[Union[AssignStat, ForStat]]:
        # a = b = c.k = 2 <=> c.k = 2, b = 2, a = 2
        # a, b, c.k = 2, 3, 4 <=> a = 2, b = 3, c.k = 4
        # a, b = c, d= 2, 3 <=> a = c = 2, b = d = 3
        val_exprs = self.visit(ctx, node.value)
        if isinstance(val_exprs, List):
            stats = list()
            for id, val_expr in enumerate(val_exprs):
                targets = list()
                for target_tuple in node.targets:
                    targets.append(target_tuple.elts[id])
                stats.extend(self._visit_single_val_Assign(ctx, node.lineno, val_expr, targets))
            return stats
        else:
            val_expr = val_exprs
            return self._visit_single_val_Assign(ctx, node.lineno, val_expr, node.targets)

    def visit_AugAssign(
        self, ctx: IRCallable, node: ast.AugAssign
    ) -> List[Union[AssignStat, ForStat]]:
        try:
            op = self.OperatorMapping.map[node.op.__class__]
        except:
            ctx.syntax_error(f"unsupported binary operator {node.op.__class__}")
        value = self.visit(ctx, node.value)
        dst = self.visit(ctx, node.target)
        if isinstance(dst, AttrExpr):
            src = AttrExpr(dst.lineno, dst.var, MemCtx.Load, dst.attrs)
        elif isinstance(dst, FieldExpr):
            src = FieldExpr(dst.lineno, dst.field, MemCtx.Load, dst.idx, dst.attrs)
        else:
            ctx.syntax_error("unknown AugAssign error")
        self._field_op_guard(ctx, value)
        return self._visit_single_val_Assign(
            ctx, node.lineno, BinExpr(node.lineno, src, value, op), [node.target]
        )

    def visit_For(self, ctx: IRCallable, node: ast.For) -> ForStat:
        loop_var = self.visit(ctx, node.target).var
        # only support 'range'
        if not isinstance(node.iter, ast.Call) or node.iter.func.id != "range":
            ctx.syntax_error("only support 'range' in for loops")
        if len(node.iter.args) == 1:
            begin = IntExpr(node.lineno, 0)
            end = self.visit(ctx, node.iter.args[0])
            step = IntExpr(node.lineno, 1)
        elif len(node.iter.args) == 2:
            begin = self.visit(ctx, node.iter.args[0])
            end = self.visit(ctx, node.iter.args[1])
            step = IntExpr(node.lineno, 1)
        elif len(node.iter.args) == 3:
            begin = self.visit(ctx, node.iter.args[0])
            end = self.visit(ctx, node.iter.args[1])
            step = self.visit(ctx, node.iter.args[2])
        else:
            ctx.syntax_error("please specify begin, end and step in a range")

        body = list()
        self.scopes.append(body)
        for sentence in node.body:
            stats = self.visit(ctx, sentence)
            self._append_stats(ctx, stats)
        self.scopes.pop()

        return ForStat(node.lineno, loop_var, begin, step, end, body)

    def visit_If(self, ctx: IRCallable, node: ast.If) -> IfStat:
        test = self.visit(ctx, node.test)

        body = list()
        self.scopes.append(body)
        for sentence in node.body:
            stats = self.visit(ctx, sentence)
            self._append_stats(ctx, stats)
        self.scopes.pop()

        orelse = list()
        self.scopes.append(orelse)
        for sentence in node.orelse:
            stats = self.visit(ctx, sentence)
            self._append_stats(ctx, stats)
        self.scopes.pop()

        return IfStat(node.lineno, test, body, orelse)
