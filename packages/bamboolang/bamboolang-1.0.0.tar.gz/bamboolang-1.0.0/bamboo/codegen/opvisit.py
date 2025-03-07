from typing import List, Dict, Tuple
from copy import deepcopy
from itertools import chain
import sys

from bamboo.lang.ir import IRVisitor, IRCallable, Var
from bamboo.lang.ir.stat import (
    AssignStat,
    IfStat,
    ForStat,
    ExprStat,
    PassStat,
    RetStat,
    SpaceStat,
)
from bamboo.lang.ir.expr import (
    AttrExpr,
    FieldExpr,
    Expr,
    IntExpr,
    StrExpr,
    FloatExpr,
    BinExpr,
    UniExpr,
    CallExpr,
    ShapeExpr,
    FieldCallExpr,
    ExternCallExpr,
    IRExternFunc,
    CastExpr,
)
from bamboo.lang.ir.expr import UniOp, BoolOp, BinOp
from bamboo.lang.ir.expr import IRStub
from bamboo.lang.dtype import (
    VoidT,
    IntT,
    FloatT,
    FieldT,
    HybridFieldT,
    HybridT,
    ShapedFieldInfo,
)
from bamboo.optim.proc import OptForStat
from bamboo.optim.SW import SWOptForStat
from bamboo.optim.SW.helper import GetSpace
from bamboo.optim.trans.parallel import constexpr

from bamboo.codegen.helper import (
    CutFuncName,
    CutFieldName,
    ConnectFieldName,
    StructPtoC,
    AddSlidingWindowIndex,
    BoolListToC,
    BoolToC,
    FieldNametoAsync,
)
from bamboo.codegen.vardetect import LoopVarDetector

from bamboo.configuration import GlobalConfiguration as gc
from bamboo.optim.proc.globalanalyse import Proc


class OpVisitor(IRVisitor):
    def __init__(self) -> None:
        self._indent = 0
        self.lines: List[str] = []
        self._slave_indent = 0
        self.slave_lines: List[str] = []
        self.slave_lines_Op: List[str] = []
        self.funcList = {}
        self.slavefuncList = {}
        self.slavestructList = {}
        self.slavefuncdeclareList = {}
        self.slavefuncdeclare: List[str] = []
        self.slavestruct: List[List[str]] = []
        self.looplist = {}
        self.tempVarType = {}
        self.tempParamList = []
        self.pid = -1
        self.codetype = 0  # 0:master 1:slave
        self.FieldHaloRange: Dict[int, List]
        self.ProcHaloRange: List[int]
        self.fieldCode = {}  # field -> C_Code
        self.fieldList = {}  # field -> C_info
        self.fieldOrder = []  # field_order 处理struct嵌套时的struct定义顺序
        self.isConst = False
        self.SlaveFuncName: List[str] = []
        self.Profiling: List[str] = []

    def append(self, line: str):
        self.lines.append(" " * self._indent + line)

    def indent_in(self, indentation: int = 2):
        self._indent += indentation

    def indent_out(self, indentation: int = 2):
        self._indent -= indentation

    def slave_append(self, line: str):
        self.slave_lines.append(" " * self._slave_indent + line)

    def slave_indent_in(self, indentation: int = 2):
        self._slave_indent += indentation

    def slave_indent_out(self, indentation: int = 2):
        self._slave_indent -= indentation

    def GetType(self, inType) -> str:
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
            res = self.GetType(inType.dtype) + "***"
            return res
        if isinstance(inType, HybridFieldT) or isinstance(inType, HybridT):
            return "struct " + inType.name

    def __call__(
        self,
        ctx: IRCallable,
        pid: int = -1,
        FieldHaloRange: Dict[int, List] = {},
        ProcHaloRange: List = [0, 0, 0],
    ):
        self.ctx = ctx
        self.pid = pid
        self.FieldHaloRange = FieldHaloRange
        self.ProcHaloRange = ProcHaloRange
        self.globalslavefunclist = []
        self.slavestruct = []
        self.SlaveFuncName = []
        self.Profiling = []

        self.indent_in()
        # print ("Func:"+str(ctx.func.__name__))
        self.tempVarType = {}  # type -> name_lists
        self.tempParamList = []

        self.isConst = False
        if hasattr(ctx.func, "const"):
            self.isConst = True

        ret_type = self.GetType(ctx.dtype)
        if isinstance(ctx.dtype, HybridT):
            self.HybridInfoCollect(ctx.dtype)
        param_info = []
        pname_hash = []
        for item in ctx.arg_vars:
            param_name = item[0]
            pos = param_name.find("%")
            if pos == -1:
                self.tempParamList.append(param_name)
                if isinstance(item[1], Var):
                    param_type = self.GetType(item[1].dtype)
                    if isinstance(item[1].dtype, HybridT):
                        self.HybridInfoCollect(item[1].dtype)
                        param_type = param_type + "*"
                else:
                    param_type = self.GetType(item[1])
                    if isinstance(item[1], HybridT):
                        self.HybridInfoCollect(item[1])
                        param_type = param_type + "*"
                param_info.append(param_type + " " + param_name)
                pname_hash.append(param_name)
            else:  # Hybrid_field
                hb_name = param_name[:pos]
                ff = ctx._items[hb_name]
                hb_type = ff.name
                param_type = "struct " + hb_type + "*"
                param_name = hb_name
                if not param_name in pname_hash:
                    pname_hash.append(param_name)
                    param_info.append(param_type + " " + param_name)
                    if isinstance(ff, HybridFieldT):
                        Code = ""
                        Code = "struct " + hb_type + "{ \n"
                        fList = []
                        for fname, ft in ff.rec_iter("%"):
                            Code = Code + self._indent * " "
                            Code = Code + self.GetType(ft.dtype) + "*** "
                            Code = Code + fname + ";\n"
                            fList.append((self.GetType(ft.dtype) + "***", fname))
                        Code = Code + "};\n"
                        if not hb_type in self.fieldCode:
                            self.fieldCode[hb_type] = Code
                            self.fieldList[hb_type] = []
                            for item in fList:
                                self.fieldList[hb_type].append(item)
                            self.fieldOrder.append(hb_type)

        for stat in ctx.body:
            # print (str(type(stat)))
            self.visit(ctx, stat)
        self.indent_out()

        FuncName = ctx.func.__name__
        if pid != -1 and self.isConst == False:
            FuncName = FuncName + "_" + str(pid)

        FuncCode = list()
        # slaveFuncCode = list()

        # print("Func_Params:" + str(param_info))
        func_declare = ret_type + " " + FuncName + "(" + ", ".join(param_info) + ")"
        FuncCode.append(func_declare)
        FuncCode.append("{")
        # slaveFuncCode.append(func_declare)
        # slaveFuncCode.append('{')

        self.indent_in()
        for key in self.tempVarType:
            if len(self.tempVarType[key]) > 0:
                spos = key.find("*")
                if spos != -1:
                    tkey = key[:spos]
                    pt = key[spos:]
                    pointVars = []
                    for item in self.tempVarType[key]:
                        pointVars.append(pt + item)
                    var_dev = " " * self._indent + tkey + " " + ", ".join(pointVars) + ";"
                else:
                    var_dev = (
                        " " * self._indent + key + " " + ", ".join(self.tempVarType[key]) + ";"
                    )

                FuncCode.append(var_dev)
                # slaveFuncCode.append(var_dev)
        self.indent_out()

        FuncCode.extend(deepcopy(self.lines))
        FuncCode.append("}")
        # slaveFuncCode.extend(deepcopy(self.slave_lines))
        # slaveFuncCode.append('}')

        self.funcList[FuncName] = FuncCode
        self.slavefuncList[FuncName] = deepcopy(self.slave_lines_Op)
        self.slavefuncdeclareList[FuncName] = deepcopy(self.slavefuncdeclare)

        self.slavestructList[FuncName] = deepcopy(self.slavestruct)

        self._indent = 0
        self.lines = []
        self.slave_lines_Op = []

        return self.SlaveFuncName, self.Profiling

    def output(self, file_name=-1):
        if file_name == -1:
            for key in self.funcList:
                code = self.funcList[key]
                for item in code:
                    print(item)
                print("\n")
        else:
            f = open(file_name, "a")
            for key in self.funcList:
                code = self.funcList[key]
                for item in code:
                    f.write(item + "\n")
                f.write("\n")
            f.close()

    def slave_output(self, file_name=-1):
        if file_name == -1:
            for key in self.slavefuncList:
                code = self.slavefuncList[key]
                for item in code:
                    print(item)
                print("\n")
        else:
            f = open(file_name, "a")
            for key in self.slavefuncList:
                code = self.slavefuncList[key]
                for item in code:
                    f.write(item + "\n")
                f.write("\n")
            f.close()

    def LocalVarCollect(self, var_type: str, var_name: str):
        if var_type not in self.tempVarType:
            self.tempVarType[var_type] = []
        if (var_name not in self.tempVarType[var_type]) and (var_name not in self.tempParamList):
            self.tempVarType[var_type].append(var_name)

    def getExpr(self, ir: Expr):
        return str(self.visit(self.ctx, ir))

    def visit_AssignStat(self, ctx: IRCallable, ir: AssignStat):
        dst = self.visit(ctx, ir.dst)
        src = self.visit(ctx, ir.src)

        # To Remember 将pypanel转换成生成后的面号数据
        if dst == "pypanel":
            src = "Proc.panel"
        if self.codetype == 0:
            self.append(str(dst) + " = " + str(src) + ";")
        else:
            self.slave_append(str(dst) + " = " + str(src) + ";")

    def visit_RetStat(self, ctx: IRCallable, ir: RetStat):
        base = "return "
        ret_ex = self.visit(ctx, ir.expr)
        ret = base + str(ret_ex) + ";"
        if self.codetype == 0:
            self.append(ret)
        else:
            self.slave_append(ret)

    def visit_IfStat(self, ctx: IRCallable, ir: IfStat):
        cond = self.visit(ctx, ir.test)
        # #To Remember 立方球前端需要对每个面进行独立计算,目前暂未将field功能拓展至更高维,直接设置pypanel为指定面号的工具,并在生成时替换
        # if gc.Grid.GridType == "CubedSphere":
        #     condstr = str(cond)
        #     condstr = condstr.replace("pypanel","Proc.panel")

        if self.codetype == 0:
            self.append("if (" + str(cond) + ")")
            # self.append('if (' + condstr + ')')
            self.append("{")
            self.indent_in()
            for stat in ir.body:
                self.visit(ctx, stat)
            self.indent_out()
            self.append("}")
            if len(ir.orelse) > 0:
                self.append("else")
                self.append("{")
                self.indent_in()
                for stat in ir.orelse:
                    self.visit(ctx, stat)
                self.indent_out()
                self.append("}")
        else:
            self.slave_append("if (" + str(cond) + ")")
            # self.append('if (' + condstr + ')')
            self.slave_append("{")
            self.slave_indent_in()
            for stat in ir.body:
                self.visit(ctx, stat)
            self.slave_indent_out()
            self.slave_append("}")
            if len(ir.orelse) > 0:
                self.slave_append("else")
                self.slave_append("{")
                self.slave_indent_in()
                for stat in ir.orelse:
                    self.visit(ctx, stat)
                self.slave_indent_out()
                self.slave_append("}")

    def visit_ForStat(self, ctx: IRCallable, ir: ForStat):
        tpe = self.GetType(ir.var.dtype)
        var_name = ir.var.name
        self.LocalVarCollect(tpe, var_name)
        st = self.visit(ctx, ir.begin)
        ed = self.visit(ctx, ir.end)
        step = self.visit(ctx, ir.step)

        vard = LoopVarDetector(self.ctx)
        var_list = []
        var_list.append(ir.var.name)
        var_dim = vard.VarDimDetect(var_list, ir.body)
        id = -1
        if var_name in var_dim:
            id = var_dim[var_name]
        if id == 2:
            halowidth = "Proc.lev_hw"
        if id == 1:
            halowidth = "Proc.lat_hw"
        if id == 0:
            halowidth = "Proc.lon_hw"

        try:
            eval(str(st))
            st = st + "+" + halowidth
        except:
            pass

        try:
            eval(str(ed))
            ed = ed + "+" + halowidth
        except:
            pass

        if self.codetype == 0:
            for_code = (
                "for ("
                + var_name
                + "="
                + st
                + ";"
                + var_name
                + "<"
                + ed
                + ";"
                + var_name
                + "+="
                + step
                + "){"
            )
            self.append(for_code)
            self.indent_in()
            for stat in ir.body:
                self.visit(ctx, stat)
            self.indent_out()
            self.append("}")
        else:
            for_code = (
                "for ("
                + var_name
                + "="
                + st
                + ";"
                + var_name
                + "<"
                + ed
                + ";"
                + var_name
                + "+="
                + step
                + "){"
            )
            self.slave_append(for_code)
            self.slave_indent_in()
            for stat in ir.body:
                self.visit(ctx, stat)
            self.slave_indent_out()
            self.slave_append("}")

    def visit_OptForStat(self, ctx: IRCallable, ir: OptForStat):
        # optfor

        # HaloWait

        if gc.Profiling:
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        for field in ir.FieldIn:
            if field.UpdateHalo:
                asyncname = "async_" + CutFieldName(field.name)
                if gc.Grid.GridType == "LonLat":
                    self.append("HaloWait(Proc,&Proc.FieldReq[" + asyncname + "]);")
                elif gc.Grid.GridType == "CubedSphere":
                    waitstr = (
                        "HaloWaitCS(Proc,&Proc.FieldReq[" + asyncname + "], " + asyncname + ", "
                    )
                    waitstr += StructPtoC(field.name) + ", "
                    waitstr += (
                        BoolListToC(str(field.pos)) + ", " + BoolListToC(str(field.HaloOrient))
                    )
                    waitstr += ");"
                    self.append(waitstr)

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CommTime += (TimeEnd - TimeBeg);")
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        kbeg = 0
        kend = 0

        vard = LoopVarDetector(self.ctx)
        var_list = []
        for fv in ir.ranges:
            var_list.append(fv.var.name)
        var_dim = vard.VarDimDetect(var_list, ir.body)
        # print ("optfor_var:" + str(var_dim))

        # for stat in ir.body:
        #    if (isinstance(stat, AssignStat)):

        for fv in ir.ranges:
            fvar = fv.var.name
            if fvar.isdigit():
                fvar = "v" + fvar
            tpe = self.GetType(fv.var.dtype)
            self.LocalVarCollect(tpe, fvar)
            halowidth = ""
            id = -1
            if fvar in var_dim:
                id = var_dim[fvar]
            if id == 2:
                halowidth = "Proc.lev_hw"
            if id == 1:
                halowidth = "Proc.lat_hw"
            if id == 0:
                halowidth = "Proc.lon_hw"
            range_st = str(fv.begin)
            range_ed = str(fv.end)
            if self.isConst == False:
                if id == 1:
                    range_st = "MAX(Proc.lat_beg, " + range_st + ")-Proc.lat_beg"
                    range_ed = "MIN(Proc.lat_end+1, " + range_ed + ")-Proc.lat_beg"
                if id == 0:
                    range_st = "MAX(Proc.lon_beg, " + range_st + ")-Proc.lon_beg"
                    range_ed = "MIN(Proc.lon_end+1, " + range_ed + ")-Proc.lon_beg"

            if halowidth != "":
                range_st = range_st + "+" + halowidth
                range_ed = range_ed + "+" + halowidth
            if fv.begin == -1 and id != 2:
                range_st = "0"
                range_ed = str(fv.end) + "+2*" + halowidth
            if id == 2:
                kbeg = fv.begin
                kend = fv.end - 1

            ForCode = (
                "for("
                + fvar
                + "="
                + range_st
                + "; "
                + fvar
                + "<"
                + range_ed
                + "; "
                + fvar
                + "+="
                + str(fv.step)
                + "){"
            )
            self.append(ForCode)
            self.indent_in()
        for stat in ir.body:
            self.visit(ctx, stat)
        for fv in ir.ranges:
            self.indent_out()
            self.append("}")

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CompTime += (TimeEnd - TimeBeg);")
            FuncName = CutFuncName(ir.ranges[0].var.prefix)
            if len(ir.FieldOut) > 0:
                FuncName += CutFieldName(ir.FieldOut[0].name)

            if not FuncName in self.Profiling:
                self.Profiling.append(FuncName)
            self.append(FuncName + "Time += (TimeEnd - TimeBeg);")
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        # UpdateHalo
        loop3d = True
        field2d = False
        for field in ir.FieldOut:
            if field.UpdateHalo:
                asyncname = "async_" + CutFieldName(field.name)
                halostr = ""
                if gc.Grid.GridType == "LonLat":
                    halostr = "UpdateHalo_"
                elif gc.Grid.GridType == "CubedSphere":
                    halostr = "UpdateHaloCS_"
                print(halostr)
                if kbeg == kend or field.shape[2] == 1:
                    halostr += "2d_"
                    loop3d = False
                    if kbeg == 0 or field.shape[2] == 1:
                        field2d = True
                else:
                    halostr += "3d_"
                if field.dtype == "double":
                    halostr += "D(Proc, "
                elif field.dtype == "single":
                    halostr += "S(Proc, "
                elif field.dtype == "int":
                    halostr += "I(Proc, "
                if loop3d:
                    # 传3d,即传整个field
                    halostr += (
                        "&"
                        + StructPtoC(field.name)
                        + "[0][0][0], &Proc.FieldReq["
                        + asyncname
                        + "], "
                        + BoolListToC(str(field.pos))
                        + ", "
                        + BoolListToC(str(field.HaloOrient))
                        + ", "
                        + BoolToC(str(not field.UpdateHaloGlobal))
                        + ");"
                    )
                elif field2d:
                    if gc.Grid.GridType == "LonLat":
                        halostr += (
                            "&"
                            + StructPtoC(field.name)
                            + "[0][0][0], &Proc.FieldReq["
                            + asyncname
                            + "], "
                            + BoolListToC(str(field.pos[0:2]))
                            + ", "
                            + BoolListToC(str(field.HaloOrient))
                            + ", "
                            + BoolToC(str(not field.UpdateHaloGlobal))
                            + ");"
                        )
                    elif gc.Grid.GridType == "CubedSphere":
                        halostr += (
                            "&"
                            + StructPtoC(field.name)
                            + "[0][0][0], &Proc.FieldReq["
                            + asyncname
                            + "], "
                            + asyncname
                            + ", "
                            + BoolListToC(str(field.pos[0:2]))
                            + ", "
                            + BoolListToC(str(field.HaloOrient))
                            + ");"
                        )
                else:
                    halostr += (
                        "&"
                        + StructPtoC(field.name)
                        + "["
                        + str(kbeg)
                        + " + Proc.lev_hw][0][0], &Proc.FieldReq["
                        + asyncname
                        + "], "
                        + BoolListToC(str(field.pos[0:2]))
                        + ", "
                        + BoolListToC(str(field.HaloOrient))
                        + ", "
                        + BoolToC(str(not field.UpdateHaloGlobal))
                        + ");"
                    )
                self.append(halostr)

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CommTime += (TimeEnd - TimeBeg);")
            self.append("")

        self.append("")

    def visit_SWOptForStat(self, ctx: IRCallable, ir: SWOptForStat):
        # use slave_append, slave_indent_in, slave_indent_out to control code_gen on slave_function
        # slavefuncList is dic which maps the slave_function code onto the function name

        # slave_append add the code to slave_lines, set a slaveFuncCode to store the codes in slave_lines after all the appends
        # then use self.slavefuncList[funcName] = slaveFuncCode
        # see the example in __call__

        # 主核全局halo取所有变量halo宽度的最大值
        # 各变量维护自己的最大halo范围
        # 从核local数组大小按各变量自己halo宽度大小设置

        def IndexToStr(x: int, y: int, z: int = -1) -> str:
            if z == -1:
                return "[" + str(y) + "][" + str(x) + "]"
            else:
                return "[" + str(z) + "][" + str(y) + "][" + str(x) + "]"

        self._slave_indent = 0
        self.slave_lines = []

        slaveFuncCode = list()

        # funcname & FuncDeclare
        FuncName: str = ""
        FuncDeclare: str = ""

        FuncName = CutFuncName(ir.ranges[0].var.prefix)
        FuncName = FuncName + "_" + str(self.pid)

        if FuncName not in self.looplist:
            self.looplist[FuncName] = 0
            FuncName += "_0"
        else:
            self.looplist[FuncName] += 1
            FuncName = FuncName + "_" + str(self.looplist[FuncName])

        FuncDeclare = "void " + FuncName + "(void *_ptr){"
        slaveFuncCode.append(FuncDeclare)
        self.slavefuncdeclare.append(deepcopy(FuncName))
        self.slave_indent_in()

        # master paratype and spawn
        structcode: List[str] = []
        structcode.append("typedef struct{\n")
        structcode.append("  int lx, ly, lz;\n")
        structcode.append("  int ox, oy, oz;\n")
        structcode.append("  int hx, hy, hz;\n")
        structcode.append("  int bx, by, bz;\n")
        structcode.append("  int mx, my, mz;\n")

        for field in ir.FieldList:
            dtype = field.dtype
            fieldname = ConnectFieldName(field.name)
            # print("Struct var!", field, fieldname, dtype)
            structcode.append("  " + dtype + " *" + fieldname + ";\n")
        for field in ir.ConstField:
            dtype = field.dtype
            fieldname = CutFieldName(field.name)
            structcode.append("  " + dtype + " *" + fieldname + ";\n")
        for var in ir.VarList:
            dtype = var.dtype
            vname = CutFieldName(var.name)
            structcode.append("  " + dtype + " " + vname + ";\n")

        paratype = FuncName + "_info"
        structcode.append("} " + paratype + ";\n")
        structcode.append("\n")
        self.slavestruct.extend(structcode)

        # HaloWait

        if gc.Profiling:
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        for field in ir.FieldIn:
            if field.UpdateHalo:
                asyncname = "async_" + CutFieldName(field.name)
                if gc.Grid.GridType == "LonLat":
                    self.append("HaloWait(Proc,&Proc.FieldReq[" + asyncname + "]);")
                elif gc.Grid.GridType == "CubedSphere":
                    waitstr = (
                        "HaloWaitCS(Proc,&Proc.FieldReq[" + asyncname + "], " + asyncname + ", "
                    )
                    waitstr += StructPtoC(field.name) + ", "
                    waitstr += (
                        BoolListToC(str(field.pos)) + ", " + BoolListToC(str(field.HaloOrient))
                    )
                    waitstr += ");"
                    self.append(waitstr)

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CommTime += (TimeEnd - TimeBeg);")
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        para = FuncName + "_para"
        self.append(paratype + " " + para + ";")

        # 计算区域大小
        if len(ir.ranges) == 3:
            kst = ir.ranges[0].begin
            ked = ir.ranges[0].end
            jst = ir.ranges[1].begin
            jed = ir.ranges[1].end
            ist = ir.ranges[2].begin
            ied = ir.ranges[2].end
        else:
            kst = 0
            ked = 1
            jst = ir.ranges[0].begin
            jed = ir.ranges[0].end
            ist = ir.ranges[1].begin
            ied = ir.ranges[1].end

        self.append(para + ".lz = " + str(ked) + " - " + str(kst) + ";")
        self.append(
            para
            + ".ly = "
            + "MIN(Proc.lat_end+1, "
            + str(jed)
            + ") - MAX(Proc.lat_beg, "
            + str(jst)
            + ");"
        )
        self.append(
            para
            + ".lx = "
            + "MIN(Proc.lon_end+1, "
            + str(ied)
            + ") - MAX(Proc.lon_beg, "
            + str(ist)
            + ");"
        )

        # 偏移
        self.append(para + ".oz = " + str(kst) + ";")
        self.append(para + ".oy = " + "MAX(Proc.lat_beg, " + str(jst) + ") - Proc.lat_beg;")
        self.append(para + ".ox = " + "MAX(Proc.lon_beg, " + str(ist) + ") - Proc.lon_beg;")

        if GetSpace(ir.StencilType) == 1:
            # stencil XY hz=0

            hx = 0
            hy = 0
            hz = 0

            for field in chain(ir.FieldIn, ir.FieldOut):
                if self.FieldHaloRange.__contains__(field.id):
                    hx = max(
                        hx,
                        max(
                            -self.FieldHaloRange[field.id][0],
                            self.FieldHaloRange[field.id][1],
                        ),
                    )
                    hy = max(
                        hy,
                        max(
                            -self.FieldHaloRange[field.id][2],
                            self.FieldHaloRange[field.id][3],
                        ),
                    )
                    hz = max(
                        hz,
                        max(
                            -self.FieldHaloRange[field.id][4],
                            self.FieldHaloRange[field.id][5],
                        ),
                    )

            hz = 0
            if ir.UseGlobalHalo:
                self.append(para + ".hx = Proc.lon_hw;")
                self.append(para + ".hy = Proc.lat_hw;")
            else:
                self.append(para + ".hx = " + str(hx) + ";")
                self.append(para + ".hy = " + str(hy) + ";")
            self.append(para + ".hz = " + str(hz) + ";")

            self.append(para + ".bx = " + str(ir.Blocking[0]) + ";")
            self.append(para + ".by = " + str(ir.Blocking[1]) + ";")
            self.append(para + ".bz = " + str(ir.Blocking[2]) + ";")

            self.append(para + ".mx = " + str(ir.Mapping[0]) + ";")
            self.append(para + ".my = " + str(ir.Mapping[1]) + ";")
            self.append(para + ".mz = " + str(ir.Mapping[2]) + ";")

            for field in ir.FieldList:
                fieldname = ConnectFieldName(field.name)
                # xb = self.ProcHaloRange[0] - hx
                # yb = self.ProcHaloRange[1] - hy
                # zb = self.ProcHaloRange[2] - hz
                if field.shape[2] > 1:
                    if ir.UseGlobalHalo:
                        self.append(
                            para
                            + "."
                            + fieldname
                            + " = &"
                            + StructPtoC(field.name)
                            + "[Proc.lev_hw - "
                            + str(hz)
                            + "+"
                            + para
                            + ".oz][Proc.lat_hw -"
                            + para
                            + ".hy +"
                            + para
                            + ".oy][Proc.lon_hw -"
                            + para
                            + ".hx +"
                            + para
                            + ".ox];"
                        )
                    else:
                        self.append(
                            para
                            + "."
                            + fieldname
                            + " = &"
                            + StructPtoC(field.name)
                            + "[Proc.lev_hw - "
                            + str(hz)
                            + "+"
                            + para
                            + ".oz][Proc.lat_hw -"
                            + str(hy)
                            + "+"
                            + para
                            + ".oy][Proc.lon_hw -"
                            + str(hx)
                            + "+"
                            + para
                            + ".ox];"
                        )
                else:
                    if ir.UseGlobalHalo:
                        self.append(
                            para
                            + "."
                            + fieldname
                            + " = &"
                            + StructPtoC(field.name)
                            + "[0][Proc.lat_hw -"
                            + para
                            + ".hy +"
                            + para
                            + ".oy][Proc.lon_hw -"
                            + para
                            + ".hx +"
                            + para
                            + ".ox];"
                        )
                    else:
                        self.append(
                            para
                            + "."
                            + fieldname
                            + " = &"
                            + StructPtoC(field.name)
                            + "[0][Proc.lat_hw -"
                            + str(hy)
                            + "+"
                            + para
                            + ".oy][Proc.lon_hw -"
                            + str(hx)
                            + "+"
                            + para
                            + ".ox];"
                        )

            for field in ir.ConstField:
                fieldname = CutFieldName(field.name)
                self.append(para + "." + fieldname + " = &" + StructPtoC(field.name) + "[0][0][0];")

            for var in ir.VarList:
                vname = CutFieldName(var.name)
                self.append(para + "." + vname + " = " + var.name + ";")

            # 不同优化级别不同生成方式
            if ir.OptLevel == 1:
                self.globalslavefunclist.append(FuncName)
                self.append("")
                self.append("athread_spawn(" + FuncName + ", &" + para + ");")
                self.append("athread_join();")
                self.append("")

                print("=?=" * 10)
                print(FuncDeclare)

                # slave funccode
                self.codetype = 1

                self.slave_append("")
                self.slave_append("volatile int reply = 0;")
                self.slave_append("volatile int COUNT = 0;")
                self.slave_append("")

                self.slave_append(paratype + " *data = (" + paratype + "*)(_ptr);")
                self.slave_append("")

                # 参数处理
                for field in chain(ir.FieldIn, ir.FieldOut):
                    # 声明远程和local变量.分水平或垂面
                    fieldname = CutFieldName(field.name)
                    romatename = "_" + fieldname

                    self.slave_append("")
                    self.slave_append("double *" + romatename + " = data->" + fieldname + ";")
                    if GetSpace(ir.StencilType) == 1:
                        nx = ir.Blocking[0] + 2 * hx
                        ny = ir.Blocking[1] + 2 * hy
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double "
                            + fieldname
                            + IndexToStr(nx, ny)
                            + ";"
                        )
                    else:
                        pass
                self.slave_append("")

                # 声明计算和分块大小
                self.slave_append("int nx = data->nx;")
                self.slave_append("int ny = data->ny;")
                self.slave_append("int nz = data->nz;")
                self.slave_append("const int ghx = " + str(self.ProcHaloRange[0]) + ";")
                self.slave_append("const int ghy = " + str(self.ProcHaloRange[1]) + ";")
                self.slave_append("const int ghz = " + str(self.ProcHaloRange[2]) + ";")
                self.slave_append("const int hx = " + str(hx) + ";")
                self.slave_append("const int hy = " + str(hy) + ";")
                self.slave_append("const int hz = " + str(hz) + ";")
                self.slave_append("const int bx = " + str(ir.Blocking[0]) + ";")
                self.slave_append("const int by = " + str(ir.Blocking[1]) + ";")
                self.slave_append("const int bz = " + str(ir.Blocking[2]) + ";")
                self.slave_append("const int mx = " + str(ir.Mapping[0]) + ";")
                self.slave_append("const int my = " + str(ir.Mapping[1]) + ";")
                self.slave_append("const int mz = " + str(ir.Mapping[2]) + ";")
                self.slave_append("")

                self.slave_append("int zbeg,zend,zlen,ybeg,yend,ylen,xbeg,xend,xlen;")
                self.slave_append("int irange,jrange;")
                self.slave_append("int numx = nx + 2*ghx;")
                self.slave_append("int numy = ny + 2*ghy;")
                self.slave_append("")

                self.slave_append("int id,rid,cid,wid,eid,sid,nid;")
                self.slave_append("int ib,jb,kb,i,j;")
                self.slave_append("int dmasize;")
                self.slave_append("")

                self.slave_append("CalcID(&id, &rid, &cid, &wid, &eid, &sid, &nid, mx, my);")
                self.slave_append(
                    "CalcRange(id,rid,cid,nx,ny,nz,mx,my,mz,&xbeg,&xend,&xlen,&ybeg,&yend,&ylen,&zbeg,&zend,&zlen);"
                )
                self.slave_append("")

                self.slave_append("DMA_DECL_DESC(READ_WRITE);")
                self.slave_append("CRTS_ssync_array();")
                self.slave_append("")

                self.slave_append("for (kb = zbeg; kb < zend; kb++)")
                self.slave_indent_in()
                self.slave_append("for (jb= ybeg; jb < yend ; jb+= by)")
                self.slave_indent_in()
                self.slave_append("for (ib = xbeg; ib < xend; ib+= bx){")
                self.slave_indent_in()
                self.slave_append("irange = MIN(ib+bx,xend) - ib;")
                self.slave_append("jrange = MIN(jb+by,yend) - jb;")
                self.slave_append("dmasize = (irange + 2*hx);")
                self.slave_append("")

                # 读入
                self.slave_append("for (j = jb ; j < MIN(jb + by, yend) + 2 * hy ; j++){")
                self.slave_indent_in()
                for field in ir.FieldIn:
                    fieldname = CutFieldName(field.name)
                    romatename = "_" + fieldname
                    self.slave_append(
                        "DMA_IREAD("
                        + romatename
                        + "+(kb*numy*numx+j*numx+ib), &"
                        + fieldname
                        + "[j - jb][0], dmasize* sizeof(double));"
                    )
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_append("")
                self.slave_append("DMA_WAIT_ALL;")
                self.slave_append("")

                # 计算
                self.slave_append("for (j = hy ; j < hy + jrange ; j++)")
                self.slave_indent_in()
                self.slave_append("for (i = hx ; i < hx + irange ; i++){")
                self.slave_indent_in()
                for stat in ir.body:
                    self.visit(ctx, stat)

                    # 替换变量，同样分不同面
                    for field in chain(ir.FieldIn, ir.FieldOut, ir.ConstField):
                        # 避免有变量名是其他变量名的子集，替换出现错误，故将变量名+[作为替换主体
                        self.slave_lines[lineid] = deepcopy(
                            self.slave_lines[lineid].replace(
                                field.name + "[", CutFieldName(field.name) + "["
                            )
                        )
                    self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace("[k]", ""))
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_indent_out()
                self.slave_append("")

                # 写回
                self.slave_append("for (j = jb + hy  ; j < MIN(jb+ by, yend) + hy ; j++){")
                self.slave_indent_in()
                for field in ir.FieldOut:
                    fieldname = CutFieldName(field.name)
                    romatename = "_" + fieldname
                    self.slave_append(
                        "DMA_IWRITE("
                        + romatename
                        + "+(kb*numy*numx+j*numx+ib+hx), &"
                        + fieldname
                        + "[j - jb ][hx], (dmasize - 2*hx) * sizeof(double));"
                    )
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_append("")

                self.slave_indent_out()
                self.slave_append("}")
            elif ir.OptLevel == 2:
                self.globalslavefunclist.append(FuncName)
                self.append("")
                self.append("athread_spawn(" + FuncName + ", &" + para + ");")
                self.append("athread_join();")
                self.append("")

                print("=?=" * 10)
                print(FuncDeclare)

                # slave funccode
                self.codetype = 1

                self.slave_append("")
                self.slave_append("volatile int reply = 0;")
                self.slave_append("volatile int COUNT = 0;")
                self.slave_append("")

                self.slave_append(paratype + " *data = (" + paratype + "*)(_ptr);")
                self.slave_append("")

                # 声明计算和分块大小
                self.slave_append("int lx = data->lx;")
                self.slave_append("int ly = data->ly;")
                self.slave_append("int lz = data->lz;")
                self.slave_append("int hx = data->hx;")
                self.slave_append("int hy = data->hy;")
                self.slave_append("int hz = data->hz;")
                self.slave_append("int ox = data->ox;")
                self.slave_append("int oy = data->oy;")
                self.slave_append("int oz = data->oz;")
                self.slave_append("int bx = data->bx;")
                self.slave_append("int by = data->by;")
                self.slave_append("int bz = data->bz;")
                self.slave_append("int mx = data->mx;")
                self.slave_append("int my = data->my;")
                self.slave_append("int mz = data->mz;")

                # self.slave_append("const int ghx = " + str(self.ProcHaloRange[0]) + ";")
                # self.slave_append("const int ghy = " + str(self.ProcHaloRange[1]) + ";")
                # self.slave_append("const int ghz = " + str(self.ProcHaloRange[2]) + ";")
                # self.slave_append("const int hx = " + str(hx) + ";")
                # self.slave_append("const int hy = " + str(hy) + ";")
                # self.slave_append("const int hz = " + str(hz) + ";")
                # self.slave_append("const int bx = " + str(ir.Blocking[0]) + ";")
                # self.slave_append("const int by = " + str(ir.Blocking[1]) + ";")
                # self.slave_append("const int bz = " + str(ir.Blocking[2]) + ";")
                # self.slave_append("const int mx = " + str(ir.Mapping[0]) + ";")
                # self.slave_append("const int my = " + str(ir.Mapping[1]) + ";")
                # self.slave_append("const int mz = " + str(ir.Mapping[2]) + ";")
                self.slave_append("")

                # 参数处理
                for field in ir.FieldList:
                    # 声明远程和local变量.分水平或垂面
                    fieldname = ConnectFieldName(field.name)
                    romatename = "_" + fieldname

                    self.slave_append("")
                    self.slave_append("double *" + romatename + " = data->" + fieldname + ";")
                    print(ir.StencilType, GetSpace(ir.StencilType))
                    if GetSpace(ir.StencilType) == 1:
                        if ir.UseGlobalHalo:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double "
                                + fieldname
                                + "[by+2*hy][bx+2*hx];"
                            )
                        else:
                            nx = ir.Blocking[0] + 2 * hx
                            ny = ir.Blocking[1] + 2 * hy
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double "
                                + fieldname
                                + IndexToStr(nx, ny)
                                + ";"
                            )
                    else:
                        pass

                # const
                for field in ir.ConstField:
                    fieldname = CutFieldName(field.name)
                    romatename = "_" + fieldname
                    self.slave_append("")
                    self.slave_append("double *" + romatename + " = data->" + fieldname + ";")
                    if field.shape[0] != 1:
                        if field.pos[0]:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[fnx+2*hx];"
                            )
                        else:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[hnx+2*hx];"
                            )
                    elif field.shape[1] != 1:
                        if field.pos[1]:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[fny+2*hy];"
                            )
                        else:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[hny+2*hy];"
                            )
                    elif field.shape[2] != 1:
                        if field.pos[2]:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[fnz+2*hz];"
                            )
                        else:
                            self.slave_append(
                                "__attribute__ ((aligned (32))) double " + fieldname + "[hnz+2*hz];"
                            )

                # var
                self.slave_append("")
                for var in ir.VarDeclare:
                    if var.Isstruct:
                        self.slave_append("struct " + var.dtype + " " + var.name + ";")
                    else:
                        self.slave_append(var.dtype + " " + var.name + ";")

                self.slave_append("")
                for var in ir.VarList:
                    vname = CutFieldName(var.name)
                    self.slave_append(var.dtype + " " + vname + " = data->" + vname + ";")

                self.slave_append("")

                self.slave_append("int zbeg,zend,zlen,ybeg,yend,ylen,xbeg,xend,xlen;")
                self.slave_append("int irange,jrange;")
                self.slave_append("int fnumx = fnx + 2*ghx;")
                self.slave_append("int fnumy = fny + 2*ghy;")
                self.slave_append("int hnumx = hnx + 2*ghx;")
                self.slave_append("int hnumy = hny + 2*ghy;")
                self.slave_append("")

                self.slave_append("int swindex[by+2*hy];")
                self.slave_append("const int ws  = by+2*hy;")
                self.slave_append("")

                self.slave_append("int id,rid,cid,wid,eid,sid,nid;")
                self.slave_append("int ib,jb,kb,i,j;")
                self.slave_append("int dmasize;")
                self.slave_append("")

                self.slave_append("CalcID(&id, &rid, &cid, &wid, &eid, &sid, &nid, mx, my);")
                self.slave_append(
                    "CalcRange(id,rid,cid,lx,ly,lz,mx,my,mz,&xbeg,&xend,&xlen,&ybeg,&yend,&ylen,&zbeg,&zend,&zlen);"
                )
                self.slave_append("")

                self.slave_append("DMA_DECL_DESC(READ_WRITE);")
                self.slave_append("CRTS_ssync_array();")
                self.slave_append("")

                # DMA const
                for field in ir.ConstField:
                    fieldname = CutFieldName(field.name)
                    romatename = "_" + fieldname
                    if field.shape[0] != 1:
                        if field.pos[0]:
                            self.slave_append("dmasize = fnx + 2*hx;")
                        else:
                            self.slave_append("dmasize = hnx + 2*hx;")
                        self.slave_append(
                            "DMA_READ("
                            + romatename
                            + "+(ghx-hx), &"
                            + fieldname
                            + "[0], dmasize* sizeof(double));"
                        )
                    elif field.shape[1] != 1:
                        if field.pos[1]:
                            self.slave_append("dmasize = fny + 2*hy;")
                        else:
                            self.slave_append("dmasize = hny + 2*hy;")
                        self.slave_append(
                            "DMA_READ("
                            + romatename
                            + "+(ghy-hy), &"
                            + fieldname
                            + "[0], dmasize* sizeof(double));"
                        )
                    elif field.shape[2] != 1:
                        if field.pos[2]:
                            self.slave_append("dmasize = fnz + 2*hz;")
                        else:
                            self.slave_append("dmasize = hnz + 2*hz;")
                        self.slave_append(
                            "DMA_READ("
                            + romatename
                            + "+(ghz-hz), &"
                            + fieldname
                            + "[0], dmasize* sizeof(double));"
                        )
                self.slave_append("")

                self.slave_append("for (kb = zbeg; kb < zend; kb++){")
                self.slave_indent_in()
                self.slave_append("for (i = 0; i < ws; i++) swindex[i] = i;")
                self.slave_append("")
                self.slave_append("for (jb= ybeg; jb < yend ; jb+= by)")
                self.slave_indent_in()
                self.slave_append("for (ib = xbeg; ib < xend; ib+= bx){")
                self.slave_indent_in()
                self.slave_append("irange = MIN(ib+bx,xend) - ib;")
                self.slave_append("jrange = MIN(jb+by,yend) - jb;")
                self.slave_append("dmasize = (irange + 2*hx);")
                self.slave_append("")

                # 读入
                self.slave_append("if (jb == ybeg){")
                self.slave_indent_in()
                self.slave_append("for (j = jb ; j < MIN(jb + by, yend) + 2 * hy ; j++){")
                self.slave_indent_in()
                for field in ir.FieldIn:
                    fieldname = ConnectFieldName(field.name)
                    romatename = "_" + fieldname
                    if field.shape[2] > 1:
                        if field.pos[1]:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(kb*fnumy*fnumx+j*fnumx+ib), &"
                                + fieldname
                                + "[j - jb][0], dmasize* sizeof(double));"
                            )
                        else:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(kb*hnumy*hnumx+j*hnumx+ib), &"
                                + fieldname
                                + "[j - jb][0], dmasize* sizeof(double));"
                            )
                    else:
                        if field.pos[1]:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(j*fnumx+ib), &"
                                + fieldname
                                + "[j - jb][0], dmasize* sizeof(double));"
                            )
                        else:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(j*hnumx+ib), &"
                                + fieldname
                                + "[j - jb][0], dmasize* sizeof(double));"
                            )

                self.slave_indent_out()
                self.slave_append("}")
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_append("else{")
                self.slave_indent_in()
                self.slave_append("for (i = 0; i < ws; i++)")
                self.slave_append("  swindex[i] = (swindex[i] + by) % ws;")
                self.slave_append("for (j = jb + hy; j < MIN(jb + by, yend) + 2 * hy ; j++){")
                self.slave_indent_in()
                self.slave_append("int pos = swindex[j - jb];")
                for field in ir.FieldIn:
                    fieldname = ConnectFieldName(field.name)
                    romatename = "_" + fieldname
                    if field.shape[2] > 1:
                        if field.pos[1]:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(kb*fnumy*fnumx+j*fnumx+ib), &"
                                + fieldname
                                + "[pos][0], dmasize* sizeof(double));"
                            )
                        else:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(kb*hnumy*hnumx+j*hnumx+ib), &"
                                + fieldname
                                + "[pos][0], dmasize* sizeof(double));"
                            )
                    else:
                        if field.pos[1]:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(j*fnumx+ib), &"
                                + fieldname
                                + "[pos][0], dmasize* sizeof(double));"
                            )
                        else:
                            self.slave_append(
                                "DMA_IREAD("
                                + romatename
                                + "+(j*hnumx+ib), &"
                                + fieldname
                                + "[pos][0], dmasize* sizeof(double));"
                            )
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_indent_out()
                self.slave_append("}")
                self.slave_append("")
                self.slave_append("DMA_WAIT_ALL;")
                self.slave_append("")

                # 计算
                self.slave_append("for (j = hy ; j < hy + jrange ; j++)")
                self.slave_indent_in()
                self.slave_append("for (i = hx ; i < hx + irange ; i++){")
                self.slave_indent_in()
                for stat in ir.body:
                    linebeg = len(self.slave_lines)

                    self.visit(ctx, stat)

                    lineend = len(self.slave_lines)

                    for lineid in range(linebeg, lineend):
                        for field in ir.ConstField:
                            if field.shape[2] != 1:
                                # old = StructPtoC(field.name) + "[0][0][i"
                                # if self.slave_lines[lineid].find(old) != -1:
                                #     new = CutFieldName(field.name) + "[0][i+ib+ox"
                                # else:
                                #     old = StructPtoC(field.name) + "[0][0][(i"
                                #     new = CutFieldName(field.name) + "[0][(i+ib+ox"
                                # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(old,new))
                                old = StructPtoC(field.name) + "[k"
                                new = CutFieldName(field.name) + "[kb+oz"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                                old = StructPtoC(field.name) + "[(k"
                                new = CutFieldName(field.name) + "[(kb+oz"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                            elif field.shape[1] != 1:
                                # old = StructPtoC(field.name) + "[0][j"
                                # if self.slave_lines[lineid].find(old) != -1:
                                #     new = CutFieldName(field.name) + "[j+jb+oy"
                                # else:
                                #     old = StructPtoC(field.name) + "[0][(j"
                                #     new = CutFieldName(field.name) + "[(j+jb+oy"
                                # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(old,new))
                                old = StructPtoC(field.name) + "[0][j"
                                new = CutFieldName(field.name) + "[j+jb+oy"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                                old = StructPtoC(field.name) + "[0][(j"
                                new = CutFieldName(field.name) + "[(j+jb+oy"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                                old = StructPtoC(field.name) + "[0][0][j"
                                new = CutFieldName(field.name) + "[0][j+jb+oy"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                                old = StructPtoC(field.name) + "[0][0][(j"
                                new = CutFieldName(field.name) + "[0][(j+jb+oy"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                            elif field.shape[0] != 1:
                                # old = StructPtoC(field.name) + "[0][0][i"
                                # if self.slave_lines[lineid].find(old) != -1:
                                #     new = CutFieldName(field.name) + "[0][i+ib+ox"
                                # else:
                                #     old = StructPtoC(field.name) + "[0][0][(i"
                                #     new = CutFieldName(field.name) + "[0][(i+ib+ox"
                                # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(old,new))
                                old = StructPtoC(field.name) + "[0][0][i"
                                new = CutFieldName(field.name) + "[i+ib+ox"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )
                                old = StructPtoC(field.name) + "[0][0][(i"
                                new = CutFieldName(field.name) + "[(i+ib+ox"
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(old, new)
                                )

                        self.slave_lines[lineid] = deepcopy(
                            self.slave_lines[lineid].replace("[0]", "")
                        )
                        self.slave_lines[lineid] = deepcopy(
                            self.slave_lines[lineid].replace("[k]", "")
                        )

                        # 替换变量，同样分不同面
                        for field in ir.FieldOut:
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(
                                    StructPtoC(field.name), ConnectFieldName(field.name)
                                )
                            )

                        for field in ir.FieldIn:
                            # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(field.name,CutFieldName(field.name)))

                            self.slave_lines[lineid] = deepcopy(
                                AddSlidingWindowIndex(
                                    self.slave_lines[lineid],
                                    StructPtoC(field.name) + "[",
                                    ConnectFieldName(field.name) + "[",
                                )
                            )

                        for var in ir.VarList:
                            old = var.name
                            new = CutFieldName(var.name)
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )

                        for FuncName in ir.FuncCall:
                            if isinstance(FuncName, str):
                                self.slave_lines[lineid] = deepcopy(
                                    self.slave_lines[lineid].replace(FuncName, "slave_" + FuncName)
                                )

                            if not FuncName in self.SlaveFuncName:
                                self.SlaveFuncName.append(FuncName)

                self.slave_indent_out()
                self.slave_append("}")
                self.slave_indent_out()
                self.slave_append("")

                # 写回
                self.slave_append("for (j = jb + hy  ; j < MIN(jb+ by, yend) + hy ; j++){")
                self.slave_indent_in()
                for field in ir.FieldOut:
                    fieldname = ConnectFieldName(field.name)
                    romatename = "_" + fieldname
                    if field.pos[1]:
                        self.slave_append(
                            "DMA_IWRITE("
                            + romatename
                            + "+(kb*fnumy*fnumx+j*fnumx+ib+hx), &"
                            + fieldname
                            + "[j - jb ][hx], (dmasize - 2*hx) * sizeof(double));"
                        )
                    else:
                        self.slave_append(
                            "DMA_IWRITE("
                            + romatename
                            + "+(kb*hnumy*hnumx+j*hnumx+ib+hx), &"
                            + fieldname
                            + "[j - jb ][hx], (dmasize - 2*hx) * sizeof(double));"
                        )
                self.slave_indent_out()

                self.slave_append("}")
                self.slave_indent_out()
                self.slave_append("}")

                self.slave_indent_out()
                self.slave_indent_out()
                self.slave_append("}")
            elif ir.OptLevel == 3:
                pass
            else:
                sys.exit("Wrong SWOPT IR: Wrong OptLevel !")

        elif GetSpace(ir.StencilType) == 2:
            ##stencil Z XZ hy=0
            print("Stencil XZ", FuncName)
            hx = 0
            hy = 0
            hz = 0

            for field in chain(ir.FieldIn, ir.FieldOut):
                if self.FieldHaloRange.__contains__(field.id):
                    hx = max(
                        hx,
                        max(
                            -self.FieldHaloRange[field.id][0],
                            self.FieldHaloRange[field.id][1],
                        ),
                    )
                    # hy = max(hy,max(-self.FieldHaloRange[field.id][2], self.FieldHaloRange[field.id][3]))
                    hz = max(
                        hz,
                        max(
                            -self.FieldHaloRange[field.id][4],
                            self.FieldHaloRange[field.id][5],
                        ),
                    )

            self.append(para + ".hx = " + str(hx) + ";")
            self.append(para + ".hy = " + str(hy) + ";")

            if ir.UseGlobalHalo:
                self.append(para + ".hz = Proc.lev_hw;")
            else:
                self.append(para + ".hz = " + str(hz) + ";")

            self.append(para + ".bx = " + str(ir.Blocking[0]) + ";")
            self.append(para + ".by = " + str(ir.Blocking[1]) + ";")
            self.append(para + ".bz = " + str(ir.Blocking[2]) + ";")

            self.append(para + ".mx = " + str(ir.Mapping[0]) + ";")
            self.append(para + ".my = " + str(ir.Mapping[1]) + ";")
            self.append(para + ".mz = " + str(ir.Mapping[2]) + ";")

            for field in ir.FieldList:
                fieldname = ConnectFieldName(field.name)
                # xb = self.ProcHaloRange[0] - hx
                # yb = self.ProcHaloRange[1] - hy
                # zb = self.ProcHaloRange[2] - hz
                if field.shape[2] > 1 and ir.UseGlobalHalo:
                    self.append(
                        para
                        + "."
                        + fieldname
                        + " = &"
                        + StructPtoC(field.name)
                        + "[Proc.lev_hw - "
                        + para
                        + ".hz+"
                        + para
                        + ".oz][Proc.lat_hw -"
                        + str(hy)
                        + "+"
                        + para
                        + ".oy][Proc.lon_hw -"
                        + str(hx)
                        + "+"
                        + para
                        + ".ox];"
                    )
                elif field.shape[2] == 1:
                    self.append(
                        para
                        + "."
                        + fieldname
                        + " = &"
                        + StructPtoC(field.name)
                        + "[0][Proc.lat_hw -"
                        + str(hy)
                        + "+"
                        + para
                        + ".oy][Proc.lon_hw -"
                        + str(hx)
                        + "+"
                        + para
                        + ".ox];"
                    )
                else:
                    self.append(
                        para
                        + "."
                        + fieldname
                        + " = &"
                        + StructPtoC(field.name)
                        + "[Proc.lev_hw - "
                        + str(hz)
                        + "+"
                        + para
                        + ".oz][Proc.lat_hw -"
                        + str(hy)
                        + "+"
                        + para
                        + ".oy][Proc.lon_hw -"
                        + str(hx)
                        + "+"
                        + para
                        + ".ox];"
                    )

            for field in ir.ConstField:
                fieldname = CutFieldName(field.name)
                self.append(para + "." + fieldname + " = &" + StructPtoC(field.name) + "[0][0][0];")

            for var in ir.VarList:
                vname = CutFieldName(var.name)
                self.append(para + "." + vname + " = " + var.name + ";")

            self.globalslavefunclist.append(FuncName)
            self.append("")
            self.append("athread_spawn(" + FuncName + ", &" + para + ");")
            self.append("athread_join();")
            self.append("")

            print("=?=" * 10)
            print(FuncDeclare)

            # slave funccode
            self.codetype = 1

            self.slave_append("")
            self.slave_append("volatile int reply = 0;")
            self.slave_append("volatile int COUNT = 0;")
            self.slave_append("")

            self.slave_append(paratype + " *data = (" + paratype + "*)(_ptr);")
            self.slave_append("")

            # 声明计算和分块大小
            self.slave_append("int lx = data->lx;")
            self.slave_append("int ly = data->ly;")
            self.slave_append("int lz = data->lz;")
            self.slave_append("int hx = data->hx;")
            self.slave_append("int hy = data->hy;")
            self.slave_append("int hz = data->hz;")
            self.slave_append("int ox = data->ox;")
            self.slave_append("int oy = data->oy;")
            self.slave_append("int oz = data->oz;")
            self.slave_append("int bx = data->bx;")
            self.slave_append("int by = data->by;")
            self.slave_append("int bz = data->bz;")
            self.slave_append("int mx = data->mx;")
            self.slave_append("int my = data->my;")
            self.slave_append("int mz = data->mz;")

            self.slave_append("")

            # 参数处理
            for field in ir.FieldList:
                # 声明远程和local变量.分水平或垂面
                fieldname = ConnectFieldName(field.name)
                romatename = "_" + fieldname

                self.slave_append("")
                self.slave_append("double *" + romatename + " = data->" + fieldname + ";")
                if ir.UseGlobalHalo:
                    self.slave_append(
                        "__attribute__ ((aligned (32))) double " + fieldname + "[bz+2*hz][bx+2*hx];"
                    )
                    # self.slave_append("__attribute__ ((aligned (32))) double " + fieldname + "[bz+2*hz][bx+2*hx];")
                else:
                    nx = ir.Blocking[0] + 2 * hx
                    nz = ir.Blocking[2] + 2 * hz
                    self.slave_append(
                        "__attribute__ ((aligned (32))) double "
                        + fieldname
                        + IndexToStr(nx, nz)
                        + ";"
                    )

            # const
            for field in ir.ConstField:
                fieldname = CutFieldName(field.name)
                romatename = "_" + fieldname
                self.slave_append("")
                self.slave_append("double *" + romatename + " = data->" + fieldname + ";")
                if field.shape[0] != 1:
                    if field.pos[0]:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[fnx+2*hx];"
                        )
                    else:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[hnx+2*hx];"
                        )
                elif field.shape[1] != 1:
                    if field.pos[1]:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[fny+2*hy];"
                        )
                    else:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[hny+2*hy];"
                        )
                elif field.shape[2] != 1:
                    if field.pos[2]:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[fnz+2*hz];"
                        )
                    else:
                        self.slave_append(
                            "__attribute__ ((aligned (32))) double " + fieldname + "[hnz+2*hz];"
                        )

            # var
            self.slave_append("")
            for var in ir.VarDeclare:
                if var.Isstruct:
                    self.slave_append("struct " + var.dtype + " " + var.name + ";")
                else:
                    self.slave_append(var.dtype + " " + var.name + ";")

            self.slave_append("")
            for var in ir.VarList:
                vname = CutFieldName(var.name)
                self.slave_append(var.dtype + " " + vname + " = data->" + vname + ";")

            self.slave_append("")

            self.slave_append("int zbeg,zend,zlen,ybeg,yend,ylen,xbeg,xend,xlen;")
            self.slave_append("int irange,jrange,krange;")
            self.slave_append("int fnumx = fnx + 2*ghx;")
            self.slave_append("int fnumy = fny + 2*ghy;")
            self.slave_append("int hnumx = hnx + 2*ghx;")
            self.slave_append("int hnumy = hny + 2*ghy;")
            self.slave_append("")

            self.slave_append("int swindex[bz+2*hz];")
            self.slave_append("const int ws  = bz+2*hz;")
            self.slave_append("")

            self.slave_append("int id,rid,cid,wid,eid,sid,nid;")
            self.slave_append("int ib,jb,kb,i,j,k;")
            self.slave_append("int dmasize;")
            self.slave_append("")

            self.slave_append("CalcID(&id, &rid, &cid, &wid, &eid, &sid, &nid, mx, my);")
            self.slave_append(
                "CalcRange(id,rid,cid,lx,ly,lz,mx,my,mz,&xbeg,&xend,&xlen,&ybeg,&yend,&ylen,&zbeg,&zend,&zlen);"
            )
            self.slave_append("")

            self.slave_append("DMA_DECL_DESC(READ_WRITE);")
            self.slave_append("CRTS_ssync_array();")
            self.slave_append("")

            # DMA const
            for field in ir.ConstField:
                fieldname = CutFieldName(field.name)
                romatename = "_" + fieldname
                if field.shape[0] != 1 and field.shape[2] == 1:
                    if field.pos[0]:
                        self.slave_append("dmasize = fnx + 2*hx;")
                    else:
                        self.slave_append("dmasize = hnx + 2*hx;")
                    self.slave_append(
                        "DMA_READ("
                        + romatename
                        + "+(ghx-hx), &"
                        + fieldname
                        + "[0], dmasize* sizeof(double));"
                    )
                elif field.shape[1] != 1 and field.shape[2] == 1:
                    if field.pos[1]:
                        self.slave_append("dmasize = fny + 2*hy;")
                    else:
                        self.slave_append("dmasize = hny + 2*hy;")
                    self.slave_append(
                        "DMA_READ("
                        + romatename
                        + "+(ghy-hy), &"
                        + fieldname
                        + "[0], dmasize* sizeof(double));"
                    )
                elif field.shape[1] == 1 and field.shape[2] != 1:
                    if field.pos[1]:
                        self.slave_append("dmasize = fnz + 2*hz;")
                    else:
                        self.slave_append("dmasize = hnz + 2*hz;")
                    self.slave_append(
                        "DMA_READ("
                        + romatename
                        + "+(ghz-hz), &"
                        + fieldname
                        + "[0], dmasize* sizeof(double));"
                    )
            self.slave_append("")

            self.slave_append("for (jb = ybeg; jb < yend; jb++){")
            self.slave_indent_in()
            self.slave_append("for (i = 0; i < ws; i++) swindex[i] = i;")
            self.slave_append("")
            self.slave_append("for (kb= zbeg; kb < zend ; kb+= bz)")
            self.slave_indent_in()
            self.slave_append("for (ib = xbeg; ib < xend; ib+= bx){")
            self.slave_indent_in()
            self.slave_append("irange = MIN(ib+bx,xend) - ib;")
            self.slave_append("krange = MIN(kb+bz,zend) - kb;")
            self.slave_append("dmasize = (irange + 2*hx);")
            self.slave_append("")

            # 读入
            self.slave_append("if (kb == zbeg){")
            self.slave_indent_in()
            self.slave_append("for (k = kb ; k < MIN(kb + bz, zend) + 2 * hz ; k++){")
            self.slave_indent_in()
            for field in ir.FieldIn:
                fieldname = ConnectFieldName(field.name)
                romatename = "_" + fieldname
                if field.shape[2] > 1:
                    if field.pos[1]:
                        self.slave_append(
                            "DMA_IREAD("
                            + romatename
                            + "+(k*fnumy*fnumx+jb*fnumx+ib), &"
                            + fieldname
                            + "[k - kb][0], dmasize* sizeof(double));"
                        )
                    else:
                        self.slave_append(
                            "DMA_IREAD("
                            + romatename
                            + "+(k*hnumy*hnumx+jb*hnumx+ib), &"
                            + fieldname
                            + "[k - kb][0], dmasize* sizeof(double));"
                        )
                else:
                    if field.pos[1]:
                        self.slave_append(
                            "DMA_IREAD("
                            + romatename
                            + "+(jb*fnumx+ib), &"
                            + fieldname
                            + "[k - kb][0], dmasize* sizeof(double));"
                        )
                    else:
                        self.slave_append(
                            "DMA_IREAD("
                            + romatename
                            + "+(jb*hnumx+ib), &"
                            + fieldname
                            + "[k - kb][0], dmasize* sizeof(double));"
                        )
            self.slave_indent_out()
            self.slave_append("}")
            self.slave_indent_out()
            self.slave_append("}")
            self.slave_append("else{")
            self.slave_indent_in()
            self.slave_append("for (i = 0; i < ws; i++)")
            self.slave_append("  swindex[i] = (swindex[i] + bz) % ws;")
            self.slave_append("for (k = kb + hz; k < MIN(kb + bz, zend) + 2 * hz ; k++){")
            self.slave_indent_in()
            self.slave_append("int pos = swindex[k - kb];")
            for field in ir.FieldIn:
                fieldname = ConnectFieldName(field.name)
                romatename = "_" + fieldname
                if field.pos[1]:
                    self.slave_append(
                        "DMA_IREAD("
                        + romatename
                        + "+(k*fnumy*fnumx+jb*fnumx+ib), &"
                        + fieldname
                        + "[pos][0], dmasize* sizeof(double));"
                    )
                else:
                    self.slave_append(
                        "DMA_IREAD("
                        + romatename
                        + "+(k*hnumy*hnumx+jb*hnumx+ib), &"
                        + fieldname
                        + "[pos][0], dmasize* sizeof(double));"
                    )
            self.slave_indent_out()
            self.slave_append("}")
            self.slave_indent_out()
            self.slave_append("}")
            self.slave_append("")
            self.slave_append("DMA_WAIT_ALL;")
            self.slave_append("")

            # 计算
            self.slave_append("for (k = hz ; k < hz + krange ; k++)")
            self.slave_indent_in()
            self.slave_append("for (i = hx ; i < hx + irange ; i++){")
            self.slave_indent_in()
            for stat in ir.body:
                linebeg = len(self.slave_lines)

                self.visit(ctx, stat)

                lineend = len(self.slave_lines)

                for lineid in range(linebeg, lineend):
                    old = "Proc.lev_hw"
                    new = "ghz"
                    self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(old, new))

                    # 替换变量，同样分不同面
                    for field in ir.FieldOut:
                        self.slave_lines[lineid] = deepcopy(
                            self.slave_lines[lineid].replace(
                                StructPtoC(field.name), ConnectFieldName(field.name)
                            )
                        )

                    for field in ir.FieldIn:
                        # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(field.name,CutFieldName(field.name)))

                        self.slave_lines[lineid] = deepcopy(
                            AddSlidingWindowIndex(
                                self.slave_lines[lineid],
                                StructPtoC(field.name) + "[",
                                ConnectFieldName(field.name) + "[",
                            )
                        )

                    # ToCheck 修改两类
                    for field in ir.ConstField:
                        if field.shape[0] != 1:
                            # old = StructPtoC(field.name) + "[0][0][i"
                            # if self.slave_lines[lineid].find(old) != -1:
                            #     new = CutFieldName(field.name) + "[0][i+ib+ox"
                            # else:
                            #     old = StructPtoC(field.name) + "[0][0][(i"
                            #     new = CutFieldName(field.name) + "[0][(i+ib+ox"
                            # self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace(old,new))
                            old = StructPtoC(field.name) + "[0][0][i"
                            new = CutFieldName(field.name) + "[i+ib+ox"
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                            old = StructPtoC(field.name) + "[0][0][(i"
                            new = CutFieldName(field.name) + "[(i+ib+ox"
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                        elif field.shape[1] != 1:
                            old = StructPtoC(field.name) + "[0][j"
                            if self.slave_lines[lineid].find(old) != -1:
                                new = CutFieldName(field.name) + "[jb+oy"
                            else:
                                old = StructPtoC(field.name) + "[0][(j"
                                new = CutFieldName(field.name) + "[(jb+oy"
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                            old = "[0]"
                            new = ""
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                        elif field.shape[2] != 1:
                            old = StructPtoC(field.name) + "[k"
                            new = CutFieldName(field.name) + "[k+kb+oz"
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                            old = StructPtoC(field.name) + "[(k"
                            new = CutFieldName(field.name) + "[(k+kb+oz"
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )
                            old = "[0][0]"
                            new = ""
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(old, new)
                            )

                    for var in ir.VarList:
                        old = var.name
                        new = CutFieldName(var.name)
                        self.slave_lines[lineid] = deepcopy(
                            self.slave_lines[lineid].replace(old, new)
                        )

                    for FuncName in ir.FuncCall:
                        if isinstance(FuncName, str):
                            self.slave_lines[lineid] = deepcopy(
                                self.slave_lines[lineid].replace(FuncName, "slave_" + FuncName)
                            )

                        if not FuncName in self.SlaveFuncName:
                            self.SlaveFuncName.append(FuncName)

                    self.slave_lines[lineid] = deepcopy(self.slave_lines[lineid].replace("[j]", ""))

            self.slave_indent_out()
            self.slave_append("}")
            self.slave_indent_out()
            self.slave_append("")

            # 写回
            self.slave_append("for (k = kb + hz  ; k < MIN(kb+ bz, zend) + hz ; k++){")
            self.slave_indent_in()
            for field in ir.FieldOut:
                fieldname = ConnectFieldName(field.name)
                romatename = "_" + fieldname
                if field.pos[1]:
                    self.slave_append(
                        "DMA_IWRITE("
                        + romatename
                        + "+(k*fnumy*fnumx+jb*fnumx+ib+hx), &"
                        + fieldname
                        + "[k - kb][hx], (dmasize - 2*hx) * sizeof(double));"
                    )
                else:
                    self.slave_append(
                        "DMA_IWRITE("
                        + romatename
                        + "+(k*hnumy*hnumx+jb*hnumx+ib+hx), &"
                        + fieldname
                        + "[k - kb][hx], (dmasize - 2*hx) * sizeof(double));"
                    )
            self.slave_indent_out()

            self.slave_append("}")
            self.slave_indent_out()
            self.slave_append("}")

            self.slave_indent_out()
            self.slave_indent_out()
            self.slave_append("}")

        else:
            pass

        slaveFuncCode.extend(deepcopy(self.slave_lines))

        self.slave_indent_out()

        slaveFuncCode.append("}")

        # self.slavefuncList[FuncName] = slaveFuncCode
        self.slave_lines_Op.append(deepcopy(slaveFuncCode))

        self._slave_indent = 0
        self.slave_lines = []

        self.codetype = 0

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CompTime += (TimeEnd - TimeBeg);")
            FuncNameShort = CutFuncName(ir.ranges[0].var.prefix)
            if len(ir.FieldOut) > 0:
                print(ir.FieldOut[0], ir.FieldOut[0].name)
                FuncNameShort += CutFieldName(ir.FieldOut[0].name)
            if not FuncNameShort in self.Profiling:
                self.Profiling.append(FuncNameShort)
            self.append(FuncNameShort + "Time += (TimeEnd - TimeBeg);")
            self.append("TimeBeg = MPI_Wtime();")
            self.append("")

        # UpdateHalo
        loop3d = True
        field2d = False
        for field in ir.FieldOut:
            if field.UpdateHalo:
                asyncname = "async_" + CutFieldName(field.name)
                halostr = ""
                if gc.Grid.GridType == "LonLat":
                    halostr = "UpdateHalo_"
                elif gc.Grid.GridType == "CubedSphere":
                    halostr = "UpdateHaloCS_"
                print(halostr)
                if kst == ked or field.shape[2] == 1:
                    halostr += "2d_"
                    loop3d = False
                    if kst == 0 or field.shape[2] == 1:
                        field2d = True
                else:
                    halostr += "3d_"
                if field.dtype == "double":
                    halostr += "D(Proc, "
                elif field.dtype == "single":
                    halostr += "S(Proc, "
                elif field.dtype == "int":
                    halostr += "I(Proc, "
                if loop3d:
                    # 传3d,即传整个field
                    halostr += (
                        "&"
                        + StructPtoC(field.name)
                        + "[0][0][0], &Proc.FieldReq["
                        + asyncname
                        + "], "
                        + BoolListToC(str(field.pos))
                        + ", "
                        + BoolListToC(str(field.HaloOrient))
                        + ", "
                        + BoolToC(str(not field.UpdateHaloGlobal))
                        + ");"
                    )
                elif field2d:
                    if gc.Grid.GridType == "LonLat":
                        halostr += (
                            "&"
                            + StructPtoC(field.name)
                            + "[0][0][0], &Proc.FieldReq["
                            + asyncname
                            + "], "
                            + BoolListToC(str(field.pos[0:2]))
                            + ", "
                            + BoolListToC(str(field.HaloOrient))
                            + ", "
                            + BoolToC(str(not field.UpdateHaloGlobal))
                            + ");"
                        )
                    elif gc.Grid.GridType == "CubedSphere":
                        halostr += (
                            "&"
                            + StructPtoC(field.name)
                            + "[0][0][0], &Proc.FieldReq["
                            + asyncname
                            + "], "
                            + asyncname
                            + ", "
                            + BoolListToC(str(field.pos[0:2]))
                            + ", "
                            + BoolListToC(str(field.HaloOrient))
                            + ");"
                        )
                else:
                    halostr += (
                        "&"
                        + StructPtoC(field.name)
                        + "["
                        + str(kst)
                        + " + Proc.lev_hw][0][0], &Proc.FieldReq["
                        + asyncname
                        + "], "
                        + BoolListToC(str(field.pos[0:2]))
                        + ", "
                        + BoolListToC(str(field.HaloOrient))
                        + ", "
                        + BoolToC(str(not field.UpdateHaloGlobal))
                        + ");"
                    )
                self.append(halostr)

        # ToCheck old_LonLat
        # #UpdateHalo
        # if (ir.ranges) == 3:
        #     kbeg = ir.ranges[2].begin
        #     kend = ir.ranges[2].end
        # else:
        #     kbeg = 0
        #     kend = 0
        # loop3d = True
        # field2d = False
        # for field in ir.FieldOut:
        #     if field.UpdateHalo:
        #         asyncname = "async_" + CutFieldName(field.name)
        #         halostr = "UpdateHalo_"
        #         if kbeg == kend or field.shape[2] == 1:
        #             halostr += "2d_"
        #             loop3d = False
        #             if kbeg == 0 or field.shape[2] == 1:
        #                 field2d = True
        #         else:
        #             halostr += "3d_"
        #         if field.dtype == "double":
        #             halostr += "D(Proc, "
        #         elif field.dtype == "single":
        #             halostr += "S(Proc, "
        #         elif field.dtype == "int":
        #             halostr += "I(Proc, "
        #         if loop3d:
        #             #传3d,即传整个field
        #             halostr += "&" + StructPtoC(field.name) + "[0][0][0], &Proc.FieldReq[" + asyncname + "], " + BoolListToC(str(field.pos)) + ", " + BoolListToC(str(field.HaloOrient))+ ", " + BoolToC(str(not field.UpdateHaloGlobal)) + ");"
        #         elif field2d:
        #             halostr += "&" + StructPtoC(field.name) + "[0][0][0], &Proc.FieldReq[" + asyncname + "], " + BoolListToC(str(field.pos[0:2])) + ", " + BoolListToC(str(field.HaloOrient)) + ", " + BoolToC(str(not field.UpdateHaloGlobal))+ ");"
        #         else:
        #             halostr += "&" + StructPtoC(field.name) + "[" + str(kbeg) + " + Proc.lev_hw][0][0], &Proc.FieldReq[" + asyncname + "], " + BoolListToC(str(field.pos[0:2])) + ", " + BoolListToC(str(field.HaloOrient)) + ", " + BoolToC(str(not field.UpdateHaloGlobal))+ ");"
        #         self.append(halostr)

        if gc.Profiling:
            self.append("TimeEnd = MPI_Wtime();")
            self.append("CommTime += (TimeEnd - TimeBeg);")
            self.append("")

        self.append("")

        # print("Finish SWOPT" , self.globalslavefunclist)

        return "SW"

    def visit_ExprStat(self, ctx: IRCallable, ir: ExprStat):
        ret = self.visit(ctx, ir.expr)
        if ret != "":
            ret = ret + ";"
        if self.codetype == 0:
            self.append(ret)
        else:
            self.slave_append(ret)

    def HybridInfoCollect(self, dd: HybridT):
        sname = dd.name
        sCode = "struct " + sname + "{\n"
        sList = []
        for item in dd.items:
            sCode = sCode + self._indent * " " + self.GetType(item[1]) + " " + item[0] + ";\n"
            sList.append((self.GetType(item[1]), item[0]))
            if isinstance(item[1], HybridT):
                self.HybridInfoCollect(item[1])
        sCode = sCode + "};\n"
        if not sname in self.fieldCode:
            self.fieldCode[sname] = sCode
            self.fieldList[sname] = []
            for item in sList:
                self.fieldList[sname].append(item)
            self.fieldOrder.append(sname)

        # Collect info
        # CallExpr & RetExpr

    def visit_AttrExpr(self, ctx: IRCallable, ir: AttrExpr) -> str:
        AttrName = ir.var.name
        if AttrName.isdigit():
            AttrName = "v" + AttrName
        tpe = self.GetType(ir.var.dtype)
        if isinstance(ir.var.dtype, HybridT):
            self.HybridInfoCollect(ir.var.dtype)
        self.LocalVarCollect(tpe, AttrName)
        if len(ir.attrs) == 0:
            ret = AttrName
        else:
            if AttrName in self.tempParamList:
                ret = "(" + AttrName + "->" + ".".join(ir.attrs) + ")"
            else:
                ret = AttrName + "." + ".".join(ir.attrs)
        return ret

    def visit_FieldExpr(self, ctx: IRCallable, ir: FieldExpr):
        field_name = ir.field.local_name
        # Hybridfield_check
        field_name = field_name.replace("%", "->")

        indx = "["
        for i in range(len(ir.idx)):
            indx = indx + self.getExpr(ir.idx[len(ir.idx) - i - 1]) + "]["
        indx = indx[:-1]

        ret = field_name + indx
        # ret = str(type(ir.field.info)) + ':' + field_name + indx
        return ret

    # def visit_FieldArgExpr(self, ctx: IRCallable, ir: FieldArgExpr):
    #    ret = str(ir)
    #    return ret

    def visit_ShapeExpr(self, ctx: IRCallable, ir: ShapeExpr):
        num = -1
        if isinstance(ir.field.ref.info, ShapedFieldInfo):
            num = ir.field.ref.info.shape[ir.idx]
        ret = str(num)
        return ret

    def visit_IntExpr(self, ctx: IRCallable, ir: IntExpr):
        val = ir.val
        if val == 0:
            return "0"
        elif val == 1:
            return "1"
        else:
            return str(val)

    def visit_StrExpr(self, ctx: IRCallable, ir: StrExpr):
        val = ir.val
        return '"' + str(val) + '"'

    def visit_FloatExpr(self, ctx: IRCallable, ir: FloatExpr):
        return str(ir.val)

    def visit_BinExpr(self, ctx: IRCallable, ir: BinExpr):
        lhs = self.visit(ctx, ir.lhs)
        if isinstance(ir.op, BoolOp):
            if ir.op == BoolOp.And:
                op = "&&"
            else:
                op = "||"
        else:
            op = str(ir.op.value)
        rhs = self.visit(ctx, ir.rhs)
        if ir.op == BinOp.Pow:
            ret = "pow(" + str(lhs) + "," + str(rhs) + ")"
        else:
            ret = "(" + str(lhs) + " " + op + " " + str(rhs) + ")"
        return ret

    def visit_UniExpr(self, ctx: IRCallable, ir: UniExpr):
        rhs = self.visit(ctx, ir.rhs)
        if ir.op == UniOp.Not:
            op = "!"
        else:
            op = "-"
        ret = op + str(rhs)
        return ret

    def visit_CallExpr(self, ctx: IRCallable, ir: CallExpr):
        if isinstance(ir.symb, IRStub):
            # struct call
            func_name = ir.symb.name
        else:
            func_name = ir.symb.func.__name__

        if isinstance(ir.symb, IRExternFunc):
            # print("In visit_CallExpr!!!!!")
            pass

        args = []
        for item in ir.args:
            if isinstance(ir.symb, IRExternFunc):
                pass
            if isinstance(item, Expr):
                ree = self.visit(ctx, item)
                if isinstance(item, AttrExpr):
                    if isinstance(item.var.dtype, HybridT):
                        if not item.var.name in self.tempParamList:
                            ree = "&" + ree
                args.append(ree)
            elif isinstance(item, FieldT) and isinstance(ir.symb, IRExternFunc):
                if gc.Profiling:
                    self.append("TimeBeg = MPI_Wtime();")
                    self.append("")
                asyncname = "async_" + CutFieldName(item.local_name)
                self.append("HaloWait(Proc,&Proc.FieldReq[" + asyncname + "]);")
                if gc.Profiling:
                    self.append("TimeEnd = MPI_Wtime();")
                    self.append("CommTime += (TimeEnd - TimeBeg);")
                    self.append("TimeBeg = MPI_Wtime();")
                    self.append("")

                ree = "&" + StructPtoC(item.local_name) + "[0][0][0]"
                args.append(ree)
            else:
                args.append(str(item.local_name))

        if isinstance(ir.symb, IRStub) and func_name == "MeshVector6":
            # -1 halo_width
            ip = 2
            for i in range(3, 6, 1):
                if ip == 2:
                    halowidth = "Proc.lev_hw"
                if ip == 1:
                    halowidth = "Proc.lat_hw"
                if ip == 0:
                    halowidth = "Proc.lon_hw"
                if args[i] == "-1":
                    args[i] = "-" + halowidth + " + 1"
                    args[i - 3] = args[i - 3] + "+2*" + halowidth
                ip = ip - 1

        params = ",".join(args)

        if isinstance(ir.symb, IRStub):
            if not func_name in self.fieldCode:
                if func_name == "max":
                    func_name = "MAX"
                if func_name == "min":
                    func_name = "MIN"
                if func_name == "trunc":
                    func_name = "(int)"
                ret = func_name + "(" + params + ")"
            else:
                ret = "(struct " + func_name + "){" + params + "}"
        else:
            ret = func_name + "(" + params + ")"

        # Tofix
        if isinstance(ir.symb, IRExternFunc) and func_name != "ncOpenFile":
            ret += ";"
            self.append(ret)
            ret = ""

            if gc.Profiling:
                self.append("TimeEnd = MPI_Wtime();")
                self.append("CompTime += (TimeEnd - TimeBeg);")
                if not func_name in self.Profiling:
                    self.Profiling.append(func_name)
                self.append(func_name + "Time += (TimeEnd - TimeBeg);")
                self.append("TimeBeg = MPI_Wtime();")
                self.append("")

            for item in ir.args:
                if isinstance(item, FieldT):
                    fid = id(item.info.desc)
                    if self.FieldHaloRange.__contains__(fid):
                        # UpdateHalo
                        halostr = "UpdateHalo_"
                        asyncname = "async_" + CutFieldName(item.local_name)
                        if item.info.shape[2] == 1:
                            halostr += (
                                "2d_D(Proc, "
                                + "&"
                                + StructPtoC(item.local_name)
                                + "[0][0][0], &Proc.FieldReq["
                                + asyncname
                                + "], "
                                + BoolListToC(str(item.info.desc.pos[0:2]))
                                + ", "
                                + BoolListToC(str([True, True, True, True]))
                                + ", false);"
                            )
                        else:
                            halostr += (
                                "3d_D(Proc, "
                                + "&"
                                + StructPtoC(item.local_name)
                                + "[0][0][0], &Proc.FieldReq["
                                + asyncname
                                + "], "
                                + BoolListToC(str(item.info.desc.pos))
                                + ", "
                                + BoolListToC(str([True, True, True, True]))
                                + ", false);"
                            )
                        self.append(halostr)

            if gc.Profiling:
                self.append("TimeEnd = MPI_Wtime();")
                self.append("CommTime += (TimeEnd - TimeBeg);")
                self.append("")

        return ret

    def visit_FieldCallExpr(self, ctx: IRCallable, ir: FieldCallExpr):
        newExp = CallExpr(ir.lineno, ir.symb, ir.args)
        field_name = self.visit(ctx, ir.field_expr)
        call_expr = self.visit(ctx, newExp)
        ret = ""

        func_name = ir.symb.name
        if isinstance(ir.symb, IRStub) and func_name == "sum":
            # sum -> reduce
            field_name = ir.field_expr.field.local_name
            field_name = field_name.replace("%", "->")
            tmp_field_name = "tmp_" + field_name.replace("->", "_")
            sum_args = []
            for item in ir.args:
                if isinstance(item, BinExpr):
                    if item.op == BinOp.Add:
                        sum_args.append(item.lhs.val + item.rhs.val)
                    elif item.op == BinOp.Sub:
                        sum_args.append(item.lhs.val - item.rhs.val)
                else:
                    sum_args.append(item.val)

            ret = "// SumCall:" + field_name + "." + str(sum_args)
            self.append(ret)
            ret = ""

            sum_op = [sum_args[0], sum_args[3], sum_args[6]]
            loop_st = [sum_args[1], sum_args[4], sum_args[7]]
            loop_ed = [sum_args[2], sum_args[5], sum_args[8]]
            loop_var = ["k", "j", "i"]
            halowidth = ["Proc.lev_hw", "Proc.lat_hw", "Proc.lon_hw"]

            # deal with dimension with a magnitude of 1
            tmp_dim = 0
            for i in range(0, 3):
                if loop_ed[i] - loop_st[i] == 1:
                    sum_op[i] = 1
                if sum_op[i] == 0:
                    tmp_dim = tmp_dim + 1

            for i in range(0, 3):
                self.LocalVarCollect("int", loop_var[i])

            tpe = "double" + tmp_dim * "*"
            self.LocalVarCollect(tpe, tmp_field_name)

            # tmp_field_alloc
            alloc_func = "allocate_" + str(tmp_dim) + "d_array_D"
            alloc_code = tmp_field_name + " = " + alloc_func + "("
            for i in range(0, 3):
                if sum_op[i] == 0:
                    alloc_code = alloc_code + str(loop_ed[i] - loop_st[i]) + ","
            alloc_code = alloc_code[:-1] + ");"
            self.append(alloc_code)
            for i in range(0, 3):
                range_st = str(loop_st[i])
                range_ed = str(loop_ed[i])
                if i == 1:
                    range_st = "MAX(Proc.lat_beg, " + range_st + ")-Proc.lat_beg"
                    range_ed = "MIN(Proc.lat_end+1, " + range_ed + ")-Proc.lat_beg"
                if i == 2:
                    range_st = "MAX(Proc.lon_beg, " + range_st + ")-Proc.lon_beg"
                    range_ed = "MIN(Proc.lon_end+1, " + range_ed + ")-Proc.lon_beg"
                range_st = range_st + "+" + halowidth[i]
                range_ed = range_ed + "+" + halowidth[i]
                fvar = loop_var[i]
                ForCode = (
                    "for("
                    + fvar
                    + "="
                    + range_st
                    + "; "
                    + fvar
                    + "<"
                    + range_ed
                    + "; "
                    + fvar
                    + "+=1){"
                )
                self.append(ForCode)
                self.indent_in()
            tmp_obj = tmp_field_name
            ## tmp no halo
            for i in range(0, 3):
                if sum_op[i] == 0:
                    tmp_obj = tmp_obj + "[" + loop_var[i] + "-" + halowidth[i] + "]"
            ToTmp = tmp_obj + "=" + tmp_obj + "+" + field_name + "[k][j][i];"
            self.append(ToTmp)
            for i in range(0, 3):
                self.indent_out()
                self.append("}")

            # Todo 看field的数据类型
            reduce_func = "Zonal_Sum_" + str(tmp_dim) + "d_D"
            reduce_code = reduce_func + "(Proc, &" + tmp_field_name
            for i in range(0, 3):
                if sum_op[i] == 0:
                    reduce_code = reduce_code + "," + str(loop_ed[i] - loop_st[i])
            reduce_code = reduce_code + ");"
            self.append(reduce_code)

            # self.append('reduce(' + tmp_field_name + ');')

            for i in range(0, 3):
                range_st = str(loop_st[i])
                range_ed = str(loop_ed[i])
                if i == 1:
                    range_st = "MAX(Proc.lat_beg, " + range_st + ")-Proc.lat_beg"
                    range_ed = "MIN(Proc.lat_end+1, " + range_ed + ")-Proc.lat_beg"
                if i == 2:
                    range_st = "MAX(Proc.lon_beg, " + range_st + ")-Proc.lon_beg"
                    range_ed = "MIN(Proc.lon_end+1, " + range_ed + ")-Proc.lon_beg"
                range_st = range_st + "+" + halowidth[i]
                range_ed = range_ed + "+" + halowidth[i]
                fvar = loop_var[i]
                ForCode = (
                    "for("
                    + fvar
                    + "="
                    + range_st
                    + "; "
                    + fvar
                    + "<"
                    + range_ed
                    + "; "
                    + fvar
                    + "+=1){"
                )
                self.append(ForCode)
                self.indent_in()
            FromTmp = field_name + "[k][j][i]" + "=" + tmp_obj + ";"
            self.append(FromTmp)
            for i in range(0, 3):
                self.indent_out()
                self.append("}")

            free_func = "free_" + str(tmp_dim) + "d_array_D"
            free_code = free_func + "(" + tmp_field_name
            for i in range(0, 3):
                if sum_op[i] == 0:
                    free_code = free_code + "," + str(loop_ed[i] - loop_st[i])
            free_code = free_code + ");"
            self.append(free_code)
        if isinstance(ir.symb, IRStub) and func_name == "ncRead":
            field_name = ir.field_expr.field.local_name
            pos = field_name.find("%")
            var_name = field_name[pos + 1 :]
            field_name = field_name.replace("%", "->")

            fs = ir.field_expr.field.info.shape
            fp = ir.field_expr.field.info.desc.pos

            nid = self.visit(ctx, ir.args[0])
            code = "ncGetVar("
            code = code + nid + ", "
            code = code + '"' + var_name + '", '
            if fs[2] == 1:
                code = code + "0, 1, 0, "
            else:
                code = code + "0, " + str(fs[2]) + ", Proc.lev_hw, "

            if fp[1]:
                code = code + "Proc.lat_beg, Proc.full_nlat, Proc.lat_hw, "
            else:
                code = code + "Proc.lat_beg, Proc.half_nlat, Proc.lat_hw, "

            if fp[0]:
                code = code + "Proc.lon_beg, Proc.full_nlon, Proc.lon_hw, "
            else:
                code = code + "Proc.lon_beg, Proc.half_nlon, Proc.lon_hw, "
            code = code + "&(" + field_name + "[0][0][0]));"
            self.append(code)

            # UpdateHalo
            halostr = "UpdateHalo_"
            asyncname = "async_" + CutFieldName(ir.field_expr.field.local_name)
            flag3d = True
            if ir.field_expr.field.info.shape[2] == 1:
                halostr += "2d_"
                flag3d = False
            else:
                halostr += "3d_"
            if (
                isinstance(ir.field_expr.field.dtype, FloatT)
                and ir.field_expr.field.dtype.bits_width == 64
            ):
                halostr += "D(Proc, "
            elif (
                isinstance(ir.field_expr.field.dtype, FloatT)
                and ir.field_expr.field.dtype.bits_width == 32
            ):
                halostr += "S(Proc, "
            elif (
                isinstance(ir.field_expr.field.dtype, IntT)
                and ir.field_expr.field.dtype.bits_width == 32
            ):
                halostr += "I(Proc, "
            else:
                sys.exit("Wrong ncIO field dtype!")

            if flag3d:
                halostr += (
                    "&"
                    + StructPtoC(ir.field_expr.field.local_name)
                    + "[0][0][0], &Proc.FieldReq["
                    + asyncname
                    + "], "
                    + BoolListToC(str(ir.field_expr.field.info.desc.pos))
                    + ", "
                    + BoolListToC(str([True, True, True, True]))
                    + ", false);"
                )
            else:
                halostr += (
                    "&"
                    + StructPtoC(ir.field_expr.field.local_name)
                    + "[0][0][0], &Proc.FieldReq["
                    + asyncname
                    + "], "
                    + BoolListToC(str(ir.field_expr.field.info.desc.pos[0:2]))
                    + ", "
                    + BoolListToC(str([True, True, True, True]))
                    + ", false);"
                )

            self.append(halostr)
        if isinstance(ir.symb, IRStub) and func_name == "ncWrite":
            ###halo?

            field_name = ir.field_expr.field.local_name
            pos = field_name.find("%")
            var_name = field_name[pos + 1 :]
            field_name = field_name.replace("%", "->")

            fs = ir.field_expr.field.info.shape
            fp = ir.field_expr.field.info.desc.pos

            nid = self.visit(ctx, ir.args[0])

            code = "ncDefVar("
            code = code + nid + ", "
            code = code + '"' + var_name + '", '
            # has_lev
            if fs[2] == 1:
                code = code + "0, "
            else:
                code = code + "1, "
            # full_lat
            if fp[1]:
                code = code + "1, "
            else:
                code = code + "0, "
            # full_lon
            if fp[0]:
                code = code + "1"
            else:
                code = code + "0"
            code = code + ");"
            self.append(code)

            code = "ncPutVar("
            code = code + nid + ", "
            code = code + '"' + var_name + '", '
            if fs[2] == 1:
                code = code + "0, 1, 0, "
            else:
                code = code + "0, " + str(fs[2]) + ", Proc.lev_hw, "

            if fp[1]:
                code = code + "Proc.lat_beg, Proc.full_nlat, Proc.lat_hw, "
            else:
                code = code + "Proc.lat_beg, Proc.half_nlat, Proc.lat_hw, "

            if fp[0]:
                code = code + "Proc.lon_beg, Proc.full_nlon, Proc.lon_hw, "
            else:
                code = code + "Proc.lon_beg, Proc.half_nlon, Proc.lon_hw, "
            code = code + "&(" + field_name + "[0][0][0]));"
            self.append(code)

        return ret

    def visit_ExternCallExpr(self, ctx: IRCallable, ir: ExternCallExpr):
        if isinstance(ir.symb, IRStub):
            func_name = ir.symb.name
        else:
            func_name = ir.symb.func.__name__
        args = []
        for item in ir.args:
            if isinstance(item, Expr):
                args.append(str(self.visit(ctx, item)))
            else:
                args.append(str(item.local_name))
        params = "(" + ",".join(args) + ")"
        ret = func_name + "." + ir.method.value + params
        return ret

    def visit_CastExpr(self, ctx: IRCallable, ir: CastExpr):
        CastType = self.GetType(ir.cast_type)
        CastObj = self.visit(ctx, ir.src)
        ret = "(" + CastType + ")(" + CastObj + ")"
        return ret
