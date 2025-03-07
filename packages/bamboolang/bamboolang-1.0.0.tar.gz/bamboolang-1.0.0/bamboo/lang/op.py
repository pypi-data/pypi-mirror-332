from typing import Any, List, Optional, Tuple, cast
from copy import deepcopy

from bamboo.lang.annot import Field, is_hybridfield, iter_hybridfield, is_hybrid, Annot
from bamboo.lang.dtype import FieldT, HybridFieldT, TimedFieldInfo, HybridT, GetCType
from bamboo.lang.ir import IRExternFunc, IRFunc, IRSpace
from bamboo.lang.ir.build import IRBuilder
from bamboo.optim.trans.const import ConstPropagator
from bamboo.optim.trans.parallel import Parallelizer
from bamboo.optim.trans.typecheck import TypeChecker
from bamboo.optim.trans.inline import Inliner
from bamboo.optim.trans.predict import Predictor
from bamboo.optim.trans.update import Updater
from bamboo.optim.proc.globalanalyse import ProcInfoMain
from bamboo.codegen import CodeGenController, TimeOpInfo

import inspect


class OpError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TimeOp:
    ACTIVE_OP: Optional[Tuple[str, List[Any]]] = None
    USE_PREVIOUS_ARGS = False

    class _OpCollector:
        def __init__(self, op: "TimeOp") -> None:
            self.op = op

        def __enter__(self):
            assert TimeOp.ACTIVE_OP is None

            opseq = []
            TimeOp.ACTIVE_OP = (self.op.full_name, opseq)
            return opseq

        def __exit__(self, exc_type, exc_value, exc_traceback):
            TimeOp.ACTIVE_OP = None

    def __init__(self, opfunc, timelength, timestep) -> None:
        self.opfunc = opfunc
        self.timelength = timelength
        self.timestep = timestep
        self.full_name = f"{opfunc.__name__}<time>"

    def _op_collector(self):
        return TimeOp._OpCollector(self)

    def __call__(self, *args, use_previous_args=False, **kwds):
        if TimeOp.ACTIVE_OP is not None:
            raise OpError(f"invalid call from '{TimeOp.ACTIVE_OP[0]}' to '{self.full_name}'")

        TimeOp.USE_PREVIOUS_ARGS = use_previous_args

        with self._op_collector() as seq:
            self.opfunc(*args, **kwds)
            seq = TimeOp.ACTIVE_OP[1]

        print("annot:" + str(self.opfunc.__annotations__))
        args_type = self.opfunc.__annotations__
        args_name = self.opfunc.__code__.co_varnames
        print(args_name)
        print(seq)
        # name: self.opfunc.__name__
        # params: args(object), args_name:(name)
        # spaceOpList:
        constTop = False
        if hasattr(self.opfunc, "const"):
            constTop = True
            print("const_time_op:" + self.opfunc.__name__)
        top = TimeOpInfo()
        top.name = self.opfunc.__name__
        top.args_obj = args
        top.args_name = args_name

        targs = "("
        tid = 0
        for item in args:
            if is_hybridfield(item):
                hybridft = cast(HybridFieldT, getattr(item.__class__, "_hybrid", None))
                constHB = False
                for _, ft in iter_hybridfield(item):
                    if ft.info.desc is not None and ft.info.desc.const == True:
                        constHB = True
                if constTop and constHB:  # mesh -> global_mesh, mesh
                    targs = targs + "struct " + hybridft.name + "* global_" + args_name[tid] + ", "
                targs = targs + "struct " + hybridft.name + "* " + args_name[tid] + ", "
            elif is_hybrid(item):
                hc = cast(HybridT, getattr(item, "_hybrid"))
                targs = targs + "struct " + hc.name + "* " + args_name[tid] + ", "
            elif isinstance(item, Annot):
                # hc = getattr(item.__class__)
                hc = item.ANNOT_TYPE
                ht = GetCType(hc)
                targs = targs + str(ht) + " " + args_name[tid] + ", "
            else:  ##Normal_Value
                val_i = args_type[args_name[tid]]
                hc = val_i.ANNOT_TYPE
                ht = GetCType(hc)
                targs = targs + str(ht) + " " + args_name[tid] + ", "

            tid = tid + 1
        targs = targs[:-2] + ")"
        top.args_code = targs

        top.sop_info = []

        var_lth = []
        for i in range(len(args)):
            var_lth.append([100, -100])

        func_list = seq
        for item in func_list:
            sargs = item["args"]
            for sarg in sargs:
                if isinstance(sarg, Tuple):
                    inx = args.index(sarg[1])
                    if sarg[0] > var_lth[inx][1]:
                        var_lth[inx][1] = sarg[0]
                    if sarg[0] < var_lth[inx][0]:
                        var_lth[inx][0] = sarg[0]

        for item in func_list:
            fc = item["op"]
            constSpace = False
            if hasattr(fc.func, "const"):
                constSpace = True
                print("const op:" + fc.func.__name__)
            sargs = item["args"]
            sparams = "("
            constParamList = []  # List of Const ParamField [(name, object)]
            for sarg in sargs:
                if isinstance(sarg, Tuple):
                    paramObj = sarg[1]
                    inx = args.index(paramObj)
                    timeInx = sarg[0] - var_lth[inx][0]
                else:
                    paramObj = sarg
                    inx = args.index(paramObj)
                    timeInx = 0
                if is_hybridfield(paramObj):
                    hybridft = cast(HybridFieldT, getattr(paramObj.__class__, "_hybrid", None))
                    constHB = False
                    for _, ft in iter_hybridfield(paramObj):
                        # for _, ft in hybridft.rec_iter('%'):
                        # print ("spaceopinfo:"+str(type(ft.info)))
                        if ft.info.desc is not None and ft.info.desc.const == True:
                            constHB = True
                    if constSpace and constHB and constTop:  ##global_mesh
                        sparams = sparams + "&global_" + args_name[inx] + "[" + str(timeInx) + "]"
                        constParamList.append((args_name[inx], paramObj))
                    else:
                        # ToCheck 把时间维下标改写成new old
                        if timeInx == 0 and sarg[0] == 0:
                            sparams = sparams + "&" + args_name[inx] + "[Timeinfo.oldt]"
                        elif timeInx == 1 and sarg[0] == 1:
                            sparams = sparams + "&" + args_name[inx] + "[Timeinfo.newt]"
                        else:
                            sparams = sparams + "&" + args_name[inx] + "[" + str(timeInx) + "]"
                else:
                    sparams = sparams + args_name[inx]
                sparams = sparams + ", "
            # ToCheck 无参数spaceop调用生成
            if sparams == "(":
                sparams = sparams + ")"
            else:
                sparams = sparams[:-2] + ")"
            top.sop_info.append((fc.func.__name__, sparams, constSpace))
            if constSpace and constTop:
                cp_name = fc.func.__name__ + "_cp"
                sparams = "("
                for item in constParamList:
                    sparams = sparams + "&global_" + item[0] + "[0], "
                    sparams = sparams + "&" + item[0] + "[0], "
                sparams = sparams[:-2] + ")"
                top.sop_info.append((cp_name, sparams, constSpace))
                CodeGenController.ConstOpInfo.append((fc.func.__name__, constParamList))

        CodeGenController.TimeOpDict[self.opfunc.__name__] = top

        func_sig = inspect.currentframe().f_back.f_locals.items()

        rargs = []

        for i in range(len(args_name)):
            rargs.append("")

        for fname, fobj in func_sig:
            if fobj in args:
                inx = args.index(fobj)
                CodeGenController.GlobalVar[fname] = []
                var_l = var_lth[inx][1] - var_lth[inx][0] + 1
                if var_l < 0:
                    var_l = 1
                CodeGenController.GlobalVar[fname].append(var_l)
                CodeGenController.GlobalVar[fname].append(fobj)
                if is_hybridfield(fobj):
                    hybridft = cast(HybridFieldT, getattr(fobj.__class__, "_hybrid", None))
                    constHB = False
                    for _, ft in iter_hybridfield(fobj):
                        if ft.info.desc is not None and ft.info.desc.const == True:
                            constHB = True
                    if constTop and constHB:  # mesh -> global_mesh, mesh
                        global_v = "global_" + fname
                        rargs[inx] = global_v + ", "
                        # CodeGenController.GlobalVar[global_v] = []
                        # CodeGenController.GlobalVar[global_v].append(var_l)
                        # CodeGenController.GlobalVar[global_v].append(fobj)
                elif is_hybrid(fobj):
                    rargs[inx] = rargs[inx] + "&"
                else:
                    rargs[inx] = rargs[inx] + str(fobj)

                rargs[inx] = rargs[inx] + fname
        inx = 0
        for item in args:  ##const normal value
            if isinstance(item, int) or isinstance(item, float):
                rargs[inx] = rargs[inx] + str(item)
            inx = inx + 1

        rargCode = "("
        for item in rargs:
            rargCode = rargCode + item + ", "
        rargCode = rargCode[:-2] + ")"

        # arg_dict即为实参名，收集顶层time_op的实参信息
        for opt in [ProcInfoMain()]:
            seq = (
                self.opfunc.__name__,
                rargCode,
                seq,
                [self.timelength, self.timestep],
            )
            seq = opt(seq)

        return seq


class FuncOp:
    def __init__(self, func) -> None:
        self.func = func
        self.callable = IRFunc(self.func)
        self.ctx = IRBuilder()(self.callable)
        print(self.ctx)
        for trans in [TypeChecker(), ConstPropagator(), Predictor()]:
            trans(self.ctx)
        CodeGenController.funcList.append(self.ctx)

    def build(self) -> None:
        pass

    def __call__(self, *args, **kwds):
        return self.func(*args, **kwds)


class ExternFuncOp:
    def __init__(self, func, avg_malloc, avg_mem, avg_flops, parallel, name) -> None:
        self.func = func
        self.callable = IRExternFunc(self.func, avg_malloc, avg_mem, avg_flops, parallel, name)
        # TODO: load libs

    def build(self) -> None:
        pass

    def init(self):
        print(f"[  init  ] external function {self.func.__name__}")

    def run(self):
        print(f"[   run  ] external function {self.func.__name__}")

    def finalize(self):
        print(f"[finalize] external function {self.func.__name__}")

    def __call__(self, *args, **kwds):
        raise OpError(f"invalid call to '{self.func.__name__}' from outside of space operator")


class SpaceOp:
    def __init__(self, func) -> None:
        self.func = func
        self.ctx_copy = None

    def build(self) -> None:
        self.callable = IRSpace(self.func)
        self.ctx = IRBuilder()(self.callable)
        # do not change its order
        for build_trans in [TypeChecker(), Inliner(), ConstPropagator(), Predictor()]:
            build_trans(self.ctx)

    def __call__(self, *args, **kwds):
        if len(kwds) != 0:
            raise OpError(f"'{self.func.__name__}<space>' does not support keyword arguments")

        if not hasattr(self, "ctx"):
            self.build()

        print(self.ctx)

        if TimeOp.ACTIVE_OP is None:
            raise OpError(f"invalid call to '{self.ctx.name}' from outside of time operator")

        # do not apply trans again
        if TimeOp.USE_PREVIOUS_ARGS and self.ctx_copy is not None:
            TimeOp.ACTIVE_OP[1].append(
                {
                    "type": "space",
                    "args": args,
                    "op": self.ctx_copy,
                    # no deepcopy
                    #            args                        : op
                    # 1.st call with arg1                    : A
                    # 1.st call with arg2(use previous args) : B
                    # 2.nd call with arg2(use previous args) : B
                    # 3.rd call with arg2(use previous args) : B
                }
            )
        else:
            # use deepcopy to free current abstract syntax tree(field ref might change)
            self.ctx_copy = deepcopy(self.ctx)
            idx = 0
            for arg in args:
                if isinstance(arg, Field):
                    cast(FieldT, self.ctx_copy.arg_vars[idx][1]).ref.info = TimedFieldInfo(
                        arg.info.dtype, arg.info.shape, 0, arg.info.desc
                    )
                    idx += 1
                elif is_hybridfield(arg):
                    for _, field in iter_hybridfield(arg):
                        # print ("spaceopinfo In Sp:"+str(type(field.info)))
                        cast(FieldT, self.ctx_copy.arg_vars[idx][1]).ref.info = TimedFieldInfo(
                            field.info.dtype, field.info.shape, 0, field.info.desc
                        )
                        idx += 1
                elif isinstance(arg, tuple) and is_hybridfield(arg[1]):
                    for _, field in iter_hybridfield(arg[1]):
                        cast(FieldT, self.ctx_copy.arg_vars[idx][1]).ref.info = TimedFieldInfo(
                            field.info.dtype, field.info.shape, arg[0], field.info.desc
                        )
                        idx += 1
                else:
                    setattr(self.ctx_copy.arg_vars[idx][1], "_value", arg)
                    idx += 1

            for trans in [Updater(), Parallelizer()]:
                trans(self.ctx_copy)
            # print(str(self.ctx_copy) + "\n")
            TimeOp.ACTIVE_OP[1].append({"type": "space", "args": args, "op": self.ctx_copy})
