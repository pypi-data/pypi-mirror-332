import sys
import copy
from typing import List, cast, Dict, Tuple, Set
from bamboo.lang.ir import IRCallable
from bamboo.codegen.opvisit import OpVisitor
from bamboo.codegen.helper import ListToArray, DtypeToC, IntListToC, Lowercase
from bamboo.optim.proc.globalanalyse import UniqueProcASTInfo, Proc
from bamboo.configuration import GlobalConfiguration
from bamboo.lang.annot import Field, is_hybridfield, iter_hybridfield, is_hybrid, Annot
from bamboo.lang.dtype import FieldT, HybridFieldT, ShapedFieldInfo, HybridT, GetCType
from bamboo.configuration import GlobalConfiguration as gc, SWDesc


class TimeOpInfo:
    def __init__(self) -> None:
        self.name = ""
        self.args_obj = []
        self.args_name: List[str] = []
        self.args_code = ""
        self.sop_info: List[Tuple(str, str, bool)] = (
            []
        )  # name and param_lists of the space_ops in a timeOp #


class FieldCodeGenInfo:
    def __init__(
        self,
        index,
        hybridname: str,
        dtype: str,
        shape: Tuple[int, int, int],
        pos: Tuple[bool, bool, bool],
        const: bool,
    ):
        self.index = index
        self.hybridname = hybridname
        self.dtype = dtype
        self.shape = shape
        self.pos = pos
        self.const = const


class CodeGenerator:
    class IndentGuard:
        def __init__(self, codegen: "CodeGenerator", indentation: int) -> None:
            self.codegen = codegen
            self.indentation = indentation

        def __enter__(self):
            self.codegen.indent_in(self.indentation)

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.codegen.indent_out(self.indentation)

    def __init__(self) -> None:
        self._indent = 0
        self.lines: List[str] = []
        self.funcList: List[IRCallable] = []  # IRNode list for funcOp
        self.globalslavefunclist: List[str] = []
        self.globalslaveheader: List[str] = []
        self.externFuncList = []
        self.funcOpCode: OpVisitor = None
        self.spaceList: List[OpVisitor] = []  # Opvisitor list for spaceOps
        self.ProcInfoList: List[UniqueProcASTInfo] = []
        self.fieldList: Dict[str, List[tuple(str, str)]] = (
            {}
        )  # Hybridfieldname -> fieldDesc(List of (Fieldtype, Fieldname))
        self.fieldCode: Dict[str, str] = {}  # Hybridfieldname -> struct code in C
        self.fieldOrder: List[str] = []  # struct定义顺序,处理结构体嵌套时的情况
        self.GlobalVar: Dict[str, List[int, HybridFieldT, bool]] = {}  # 时间片维度,信息,是否为const
        self.GlobalFieldIndex: Dict[str, FieldCodeGenInfo] = (
            {}
        )  # 所有物理量排序,key为field变量名(不包括结构体名)
        self.TimeOpDict: Dict[str, TimeOpInfo] = {}
        self.ConstOpInfo: List[tuple] = []  # List[tuple(func_name, List[param_name, param_object])]
        self.ConstOpCP: List[str] = []
        self.MainTimeOpList: List[str] = []
        self.MainTimeOpArgs: List[str] = []
        self.spaceOpDict: Dict[str, List[str]] = (
            {}
        )  # (spaceOpName -> Code) avoid multi declare for const SpaceOp
        self.spaceOpDictSlaveStruct: Dict[str, List[str]] = {}
        self.spaceOpDictSlaveDeclare: Dict[str, List[str]] = {}
        self.SlaveDeclareMap: Dict[str, int] = {}
        self.spaceOpDictSlaveCode: Dict[str, List[str]] = {}
        self.MainTimeOpStep: List[Tuple[int, int]] = []
        self.fieldnum: int = 0  # 记录需要非阻通信的field数量
        self.PanelHalo: int = 0
        self.SlaveFuncName: List[str] = []
        self.ProfilingName: List[str] = []
        self.ExternHList: Set[str] = set()

    def append(self, line: str):
        self.lines.append(" " * self._indent + line)

    def indent_in(self, indentation: int = 2):
        self._indent += indentation

    def indent_out(self, indentation: int = 2):
        self._indent -= indentation

    def indent(self, indentation: int = 2):
        return CodeGenerator.IndentGuard(self, indentation)

    def functionOutput(self, file_name=-1):
        self.funcOpCode.output(file_name)

    def slavefunctionOutput(self, file_name=-1):
        f = open(file_name, "a")
        for key in self.funcOpCode.funcList:
            if key in self.SlaveFuncName:
                code = self.funcOpCode.funcList[key]
                code[0] = copy.deepcopy(code[0].replace(key, "slave_" + key))
                for item in code:
                    f.write(item + "\n")
                f.write("\n")
            else:
                code = self.funcOpCode.funcList[key]
                for item in code:
                    f.write(item + "\n")
                f.write("\n")
        f.close()
        self.funcOpCode.slave_output(file_name)

    def timeOutput(self, file_name=-1):
        pcs = len(self.ProcInfoList)
        for key in self.TimeOpDict:
            tinfo = self.TimeOpDict[key]
            if file_name == -1:
                for pid in range(0, pcs):
                    print("void " + tinfo.name + "_" + str(pid) + tinfo.args_code)
                    print("{")
                    self.indent_in()
                    for si in tinfo.sop_info:
                        if si[2] == True:  # const, no_proc_id
                            print(self._indent * " " + si[0] + si[1] + ";")
                        else:
                            print(self._indent * " " + si[0] + "_" + str(pid) + si[1] + ";")
                    self.indent_out()
                    print("}")
            else:
                f = open(file_name, "a")
                for pid in range(0, pcs):
                    f.write("void " + tinfo.name + "_" + str(pid) + tinfo.args_code + "\n")
                    f.write("{\n")
                    self.indent_in()
                    for si in tinfo.sop_info:
                        print(si)
                        if si[2] == True:  # const, no_proc_id
                            f.write(self._indent * " " + si[0] + si[1] + ";\n")
                        else:
                            f.write(self._indent * " " + si[0] + "_" + str(pid) + si[1] + ";\n")
                    self.indent_out()
                    f.write("}\n")
                    f.write("\n")
                f.close()

    def spaceOutput(self, file_name=-1):
        if file_name == -1:
            for key in self.spaceOpDict:
                code = self.spaceOpDict[key]
                for item in code:
                    print(item)
                print("\n")
        else:
            f = open(file_name, "a")
            for key in self.spaceOpDict:
                code = self.spaceOpDict[key]
                for item in code:
                    f.write(item + "\n")
                f.write("\n")
            f.close()

    def slavespaceOutput(self, file_name=-1):
        if file_name == -1:
            for key in self.spaceOpDictSlaveCode:
                code = self.spaceOpDictSlaveCode[key]
                for item in code:
                    print(item)
                print("\n")
        else:
            f = open(file_name, "a")
            for key in self.spaceOpDictSlaveCode:
                code = self.spaceOpDictSlaveCode[key]
                for item in code:
                    for slavecode in item:
                        f.write(slavecode + "\n")
                f.write("\n")
            f.close()

    def fieldAggregate(self):
        for item in self.spaceList:
            for key in item.fieldOrder:
                if not key in self.fieldCode:
                    self.fieldCode[key] = item.fieldCode[key]
                    self.fieldList[key] = []
                    for ls in item.fieldList[key]:
                        self.fieldList[key].append(ls)
                    self.fieldOrder.append(key)
        for key in self.funcOpCode.fieldOrder:
            if not key in self.fieldCode:
                self.fieldCode[key] = self.funcOpCode.fieldCode[key]
                self.fieldList[key] = []
                for ls in self.funcOpCode.fieldList[key]:
                    self.fieldList[key].append(ls)
                self.fieldOrder.append(key)
        # spaceOp Collect (remove redundant constOps)
        for item in self.spaceList:
            for key in item.funcList:
                if not key in self.spaceOpDict:
                    self.spaceOpDict[key] = []
                    self.spaceOpDictSlaveCode[key] = []
                    self.spaceOpDictSlaveStruct[key] = []
                    self.spaceOpDictSlaveDeclare[key] = []
                    for codeline in item.funcList[key]:
                        self.spaceOpDict[key].append(codeline)
                    for declarecode in item.slavefuncdeclareList[key]:
                        self.spaceOpDictSlaveDeclare[key].append(declarecode)
                        x = self.SlaveDeclareMap.get(declarecode, -1)
                        if x == -1:
                            self.SlaveDeclareMap[declarecode] = 1
                    for slavecode in item.slavefuncList[key]:
                        # 从核extern去重
                        self.spaceOpDictSlaveCode[key].append(slavecode)
                        pos = slavecode[0].find("(")
                        declarename = slavecode[0][5:pos]
                        x = self.SlaveDeclareMap.get(declarename, -1)
                        if x == 1:
                            self.SlaveDeclareMap[declarename] = 2
                    for structcode in item.slavestructList[key]:
                        self.spaceOpDictSlaveStruct[key].append(structcode)

    def VarProcess(self):
        for key in self.GlobalVar:
            item_lst = self.GlobalVar[key]
            # GlobalVar的value是一个tuple/List，第一项是数组长度，第二项是field本身信息，需要还可以再加东西
            var_length = item_lst[0]  # 数组长度
            item = item_lst[1]
            print(str(var_length))
            if isinstance(item, Field):
                print(key + ":field")
            elif is_hybridfield(item):
                hybridft = cast(HybridFieldT, getattr(item.__class__, "_hybrid", None))
                print(key + ":" + hybridft.name)
                for key, _ in hybridft.items:
                    # TODO: recursive hybrid field; 'field' is hybrid field and has no attribute 'info'
                    field = getattr(item, key)
                    print(type(field))
                    print(
                        key,
                        field.info.dtype,
                        field.info.shape,
                        field.info.desc.pos,
                        field.info.desc.const,
                    )
                print(str(item))
                # for fn, ft in hybridft.rec_iter('%'):
                #    print (fn)
                #    finfo = cast(ShapedFieldInfo, ft.info)
                #    print (type(ft.info))

            else:
                print(key + ":value")

                # print (fn, finfo.dtype, finfo.shape, finfo.desc.pos, finfo.desc.const)
                # for field in iter_hybridfield(item):
                #    print (field.info.dtype, field.info.shape, field.info.desc.pos)

    def fieldOutput(self, head_name=-1, file_name=-1):
        print("In fieldOutput!!!")
        print(self.fieldCode)
        print(self.GlobalVar)
        print(self.fieldList)

        # 生成头文件
        f = open(head_name, "a")
        f.write("#ifndef PHYSICAL_VARIABLE_H_INCLUDED\n")
        f.write("#define PHYSICAL_VARIABLE_H_INCLUDED 1\n")
        f.write("\n")

        f.write("#include<stdbool.h>\n")

        # field结构体声明
        for key in self.fieldOrder:
            code = self.fieldCode[key]
            f.write(code)
        f.write("\n")

        print("GlobalVar ", self.GlobalVar)
        # 结构体变量声明,全局field变量汇总
        for key in self.GlobalVar:
            item_lst = self.GlobalVar[key]
            var_length = item_lst[0]  # 数组长度
            item = item_lst[1]
            item_lst.append(False)
            if isinstance(item, Field):
                pass
            elif is_hybridfield(item):
                hybridft = cast(HybridFieldT, getattr(item.__class__, "_hybrid", None))

                for fieldname, _ in hybridft.items:
                    field = getattr(item, fieldname)
                    if field.info.desc.const:
                        self.GlobalFieldIndex[fieldname] = FieldCodeGenInfo(
                            -1,
                            key,
                            DtypeToC(field.info.dtype),
                            field.info.shape,
                            field.info.desc.pos,
                            field.info.desc.const,
                        )
                        item_lst[2] = True
                    else:
                        self.fieldnum += 1
                        self.GlobalFieldIndex[fieldname] = FieldCodeGenInfo(
                            self.fieldnum,
                            key,
                            DtypeToC(field.info.dtype),
                            field.info.shape,
                            field.info.desc.pos,
                            field.info.desc.const,
                        )

                if item_lst[2]:
                    # const
                    f.write("struct " + hybridft.name + " " + key + "[" + str(var_length) + "];\n")
                    f.write(
                        "struct "
                        + hybridft.name
                        + " global_"
                        + key
                        + "["
                        + str(var_length)
                        + "];\n"
                    )
                else:
                    f.write("struct " + hybridft.name + " " + key + "[" + str(var_length) + "];\n")
            elif is_hybrid(item):
                # value结构体
                hc = cast(HybridT, getattr(item.__class__, "_hybrid", None))
                f.write("struct " + hc.name + " " + key + ";\n")
            elif isinstance(item, Annot):
                hc = GetCType(item.ANNOT_TYPE)
                f.write(hc + " " + key + ";\n")

        f.write("\n")

        # #非阻塞变量序号宏定义
        for key, value in self.GlobalFieldIndex.items():
            if not value.const:
                f.write("#define async_" + key + " " + str(value.index) + "\n")
        f.write("\n")

        # Profiling_H
        if gc.Profiling:
            f.write("extern double TimeBeg;\n")
            f.write("extern double TimeEnd;\n")
            f.write("extern double CommTime;\n")
            f.write("extern double CompTime;\n")
            for name in self.ProfilingName:
                f.write("extern double " + name + "Time;\n")
            f.write("\n")
            f.write("void ProfilingOutPut(int id);\n\n")

        f.write("void PhysicalVariableInit();\n")
        f.write("void PhysicalVariableFinish();\n")

        f.write("\n")
        f.close()

        # 生成变量内存程序
        f = open(file_name, "a")
        f.write("#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n\n")
        f.write('#include"../LIB/Process.h"\n#include"../LIB/Memory.h"\n\n')
        f.write('#include"physical_variable.h"\n\n')

        # Profiling_C
        if gc.Profiling:
            f.write("double TimeBeg;\n")
            f.write("double TimeEnd;\n")
            f.write("double CommTime;\n")
            f.write("double CompTime;\n")
            for name in self.ProfilingName:
                f.write("double " + name + "Time;\n")
            f.write("\n")

        # Init
        f.write("void PhysicalVariableInit(){\n")
        f.write("  int lev,lat,lon;\n")
        f.write("  int plat,plon;\n")
        f.write("  int i,j,k,p;\n\n")

        # ToCheck LEV full half 是否影响gmcore
        for hybrid, list in self.GlobalVar.items():
            if list[2]:
                # const
                # global,大小不变
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")
                for key, value in self.GlobalFieldIndex.items():
                    if value.hybridname == hybrid:
                        if value.shape[0] == 1:
                            f.write("    lon = " + str(value.shape[0]) + ";\n")
                        else:
                            f.write("    lon = " + str(value.shape[0]) + " + 2*Proc.lon_hw;\n")
                        if value.shape[1] == 1:
                            f.write("    lat = " + str(value.shape[1]) + ";\n")
                        else:
                            f.write("    lat = " + str(value.shape[1]) + " + 2*Proc.lat_hw;\n")
                        if value.shape[2] == 1:
                            f.write("    lev = " + str(value.shape[2]) + ";\n")
                        else:
                            f.write("    lev = " + str(value.shape[2]) + " + 2*Proc.lev_hw;\n")

                        if value.dtype == "double":
                            f.write(
                                "    global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_D(lev, lat, lon);\n"
                            )
                        elif value.dtype == "float":
                            f.write(
                                "    global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_S(lev, lat, lon);\n"
                            )
                        elif value.dtype == "int":
                            f.write(
                                "    global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_I(lev, lat, lon);\n"
                            )
                        f.write("\n")

                f.write("  }\n")
                f.write("\n")

                # local,大小随动
                # Tocheck const不引入pos信息是否合理
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")
                for key, value in self.GlobalFieldIndex.items():
                    if value.hybridname == hybrid:
                        if value.shape[0] == 1:
                            f.write("    lon = " + str(value.shape[0]) + ";\n")
                        else:
                            if value.pos[0] == True:
                                f.write("    lon = Proc.full_nlon + 2*Proc.lon_hw;\n")
                            else:
                                f.write("    lon = Proc.half_nlon + 2*Proc.lon_hw;\n")
                        if value.shape[1] == 1:
                            f.write("    lat = " + str(value.shape[1]) + ";\n")
                        else:
                            if value.pos[1] == True:
                                f.write("    lat = Proc.full_nlat + 2*Proc.lat_hw;\n")
                            else:
                                f.write("    lat = Proc.half_nlat + 2*Proc.lat_hw;\n")
                        if value.shape[2] == 1:
                            f.write("    lev = " + str(value.shape[2]) + ";\n")
                        else:
                            f.write("    lev = " + str(value.shape[2]) + " + 2*Proc.lev_hw;\n")

                        if value.dtype == "double":
                            f.write(
                                "    "
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_D(lev, lat, lon);\n"
                            )
                        elif value.dtype == "float":
                            f.write(
                                "    "
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_S(lev, lat, lon);\n"
                            )
                        elif value.dtype == "int":
                            f.write(
                                "    "
                                + value.hybridname
                                + "[p]."
                                + key
                                + " = allocate_3d_array_I(lev, lat, lon);\n"
                            )
                        f.write("\n")

                f.write("  }\n")
            # 普通field
            else:
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")
                if is_hybridfield(list[1]):
                    for key, value in self.GlobalFieldIndex.items():
                        if value.hybridname == hybrid:
                            if value.shape[0] == 1:
                                f.write("    lon = " + str(value.shape[0]) + ";\n")
                            else:
                                if value.pos[0] == True:
                                    f.write("    lon = Proc.full_nlon + 2*Proc.lon_hw;\n")
                                else:
                                    f.write("    lon = Proc.half_nlon + 2*Proc.lon_hw;\n")
                                if gc.Grid.GridType == "CubedSphere":
                                    if value.pos[0] == True:
                                        f.write("    plon = Proc.full_nlon + 2*Proc.p_hw;\n")
                                    else:
                                        f.write("    plon = Proc.half_nlon + 2*Proc.p_hw;\n")
                            if value.shape[1] == 1:
                                f.write("    lat = " + str(value.shape[1]) + ";\n")
                            else:
                                if value.pos[1] == True:
                                    f.write("    lat = Proc.full_nlat + 2*Proc.lat_hw;\n")
                                else:
                                    f.write("    lat = Proc.half_nlat + 2*Proc.lat_hw;\n")
                                if gc.Grid.GridType == "CubedSphere":
                                    if value.pos[1] == True:
                                        f.write("    plon = Proc.full_nlat + 2*Proc.p_hw;\n")
                                    else:
                                        f.write("    plon = Proc.half_nlat + 2*Proc.p_hw;\n")
                            if value.shape[2] == 1:
                                f.write("    lev = " + str(value.shape[2]) + ";\n")
                            else:
                                if value.pos[2] == 1:
                                    f.write("    lev = Proc.full_nlev + 2*Proc.lev_hw;\n")
                                else:
                                    f.write("    lev = Proc.half_nlev + 2*Proc.lev_hw;\n")

                            if value.dtype == "double":
                                f.write(
                                    "    "
                                    + value.hybridname
                                    + "[p]."
                                    + key
                                    + " = allocate_3d_array_D(lev, lat, lon);\n"
                                )
                                # ToCheck 增加的接收halo的变量
                                # if (gc.Grid.GridType == "CubedSphere"):
                                #     f.write("    if (!Proc.at_east && !Proc.at_west)\n")
                                #     f.write("    "+value.hybridname + "[p]." + key + "_ax = allocate_3d_array_D(1, 1, 1);\n")
                                #     f.write("    if (Proc.at_west){\n")
                                #     f.write("      if (Proc.panel & 1) "+value.hybridname + "[p]." + key + "_ax = allocate_3d_array_D(lev, Proc.x_hw, plat);\n")
                                #     f.write("      else "+value.hybridname + "[p]." + key + "_ax = allocate_3d_array_D(lev, plat, Proc.x_hw);\n")
                                #     f.write("    }\n")
                                #     f.write("    if (Proc.at_east){\n")
                                #     f.write("      if (Proc.panel & 1) "+value.hybridname + "[p]." + key + "_ax = allocate_3d_array_D(lev, plat, Proc.x_hw);\n")
                                #     f.write("      else "+value.hybridname + "[p]." + key + "_ax = allocate_3d_array_D(lev, Proc.x_hw, plat);\n")
                                #     f.write("    }\n")

                                #     f.write("    if (!Proc.at_south && !Proc.at_north)\n")
                                #     f.write("    "+value.hybridname + "[p]." + key + "_ay = allocate_3d_array_D(1, 1, 1);\n")
                                #     f.write("    if (Proc.at_south){\n")
                                #     f.write("      if (Proc.panel & 1) "+value.hybridname + "[p]." + key + "_ay = allocate_3d_array_D(lev, Proc.y_hw, plon);\n")
                                #     f.write("      else "+value.hybridname + "[p]." + key + "_ay = allocate_3d_array_D(lev, plon, Proc.y_hw);\n")
                                #     f.write("    }\n")
                                #     f.write("    if (Proc.at_north){\n")
                                #     f.write("      if (Proc.panel & 1) "+value.hybridname + "[p]." + key + "_ay = allocate_3d_array_D(lev, plon, Proc.y_hw);\n")
                                #     f.write("      else "+value.hybridname + "[p]." + key + "_ay = allocate_3d_array_D(lev, Proc.y_hw, plon);\n")
                                #     f.write("    }\n")

                            elif value.dtype == "float":
                                f.write(
                                    "    "
                                    + value.hybridname
                                    + "[p]."
                                    + key
                                    + " = allocate_3d_array_S(lev, lat, lon);\n"
                                )
                                # CubedSphere
                            elif value.dtype == "int":
                                f.write(
                                    "    "
                                    + value.hybridname
                                    + "[p]."
                                    + key
                                    + " = allocate_3d_array_I(lev, lat, lon);\n"
                                )
                                # CubedSphere
                            f.write("\n")
                elif is_hybrid(list[1]):
                    hc = cast(HybridT, getattr(list[1].__class__, "_hybrid", None))
                    for var in vars(list[1]).items():
                        if var[0] != "_hybrid":
                            f.write(
                                "    "
                                + hybrid
                                + "."
                                + var[0]
                                + " = "
                                + Lowercase(str(var[1]))
                                + ";\n"
                            )
                elif isinstance(list[1], Annot):
                    for var in vars(list[1]).items():
                        if var[0] == "val":
                            f.write("    " + hybrid + " = " + str(var[1]) + ";\n")

                f.write("  }\n")

            f.write("\n")

        f.write("}\n")

        f.write("\n")

        # Finish
        f.write("void PhysicalVariableFinish(){\n")
        f.write("  int lev,lat,lon;\n")
        f.write("  int i,j,k,p;\n\n")

        for hybrid, list in self.GlobalVar.items():
            if list[2]:
                # const
                # global,大小不变
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")
                for key, value in self.GlobalFieldIndex.items():
                    if value.hybridname == hybrid:
                        if value.shape[0] == 1:
                            f.write("    lon = " + str(value.shape[0]) + ";\n")
                        else:
                            f.write("    lon = " + str(value.shape[0]) + " + 2*Proc.lon_hw;\n")
                        if value.shape[1] == 1:
                            f.write("    lat = " + str(value.shape[1]) + ";\n")
                        else:
                            f.write("    lat = " + str(value.shape[1]) + " + 2*Proc.lat_hw;\n")
                        if value.shape[2] == 1:
                            f.write("    lev = " + str(value.shape[2]) + ";\n")
                        else:
                            f.write("    lev = " + str(value.shape[2]) + " + 2*Proc.lev_hw;\n")

                        if value.dtype == "double":
                            f.write(
                                "    free_3d_array_D(global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "float":
                            f.write(
                                "    free_3d_array_S(global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "int":
                            f.write(
                                "    free_3d_array_I(global_"
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon)\n"
                            )
                        f.write("\n")

                f.write("  }\n")
                f.write("\n")

                # local,大小随动
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")
                for key, value in self.GlobalFieldIndex.items():
                    if value.hybridname == hybrid:
                        if value.shape[0] == 1:
                            f.write("    lon = " + str(value.shape[0]) + ";\n")
                        else:
                            if value.pos[0] == True:
                                f.write("    lon = Proc.full_nlon + 2*Proc.lon_hw;\n")
                            else:
                                f.write("    lon = Proc.half_nlon + 2*Proc.lon_hw;\n")
                        if value.shape[1] == 1:
                            f.write("    lat = " + str(value.shape[1]) + ";\n")
                        else:
                            if value.pos[1] == True:
                                f.write("    lat = Proc.full_nlat + 2*Proc.lat_hw;\n")
                            else:
                                f.write("    lat = Proc.half_nlat + 2*Proc.lat_hw;\n")
                        if value.shape[2] == 1:
                            f.write("    lev = " + str(value.shape[2]) + ";\n")
                        else:
                            f.write("    lev = " + str(value.shape[2]) + " + 2*Proc.lev_hw;\n")

                        if value.dtype == "double":
                            f.write(
                                "    free_3d_array_D("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "float":
                            f.write(
                                "    free_3d_array_S("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "int":
                            f.write(
                                "    free_3d_array_I("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon)\n"
                            )
                        f.write("\n")

                f.write("  }\n")
            else:
                f.write("  for (p = 0 ; p < " + str(list[0]) + " ; p++){\n")

                for key, value in self.GlobalFieldIndex.items():
                    if value.hybridname == hybrid:
                        if value.shape[0] == 1:
                            f.write("    lon = " + str(value.shape[0]) + ";\n")
                        else:
                            if value.pos[0] == True:
                                f.write("    lon = Proc.full_nlon + 2*Proc.lon_hw;\n")
                            else:
                                f.write("    lon = Proc.half_nlon + 2*Proc.lon_hw;\n")
                        if value.shape[1] == 1:
                            f.write("    lat = " + str(value.shape[1]) + ";\n")
                        else:
                            if value.pos[1] == True:
                                f.write("    lat = Proc.full_nlat + 2*Proc.lat_hw;\n")
                            else:
                                f.write("    lat = Proc.half_nlat + 2*Proc.lat_hw;\n")
                        if value.shape[2] == 1:
                            f.write("    lev = " + str(value.shape[2]) + ";\n")
                        else:
                            if value.pos[2] == 1:
                                f.write("    lev = Proc.full_nlev + 2*Proc.lev_hw;\n")
                            else:
                                f.write("    lev = Proc.half_nlev + 2*Proc.lev_hw;\n")

                        if value.dtype == "double":
                            f.write(
                                "    free_3d_array_D("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "float":
                            f.write(
                                "    free_3d_array_S("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        elif value.dtype == "int":
                            f.write(
                                "    free_3d_array_I("
                                + value.hybridname
                                + "[p]."
                                + key
                                + ", lev, lat, lon);\n"
                            )
                        f.write("\n")

                f.write("  }\n")

            f.write("\n")

        f.write("}\n")

        f.write("\n")

        # meshInit_cp
        print("ConstopInfo:" + str(self.ConstOpInfo))
        # TODO: ConstOpInfo may be empty
        if len(self.ConstOpInfo) != 0:
            (funcname, funcmesh) = self.ConstOpInfo[0]

            for funcname, funcmesh in self.ConstOpInfo:
                hybridname = funcmesh[0][0]
                hybridft = cast(HybridFieldT, getattr(funcmesh[0][1], "_hybrid"))
                funcnamestr = (
                    "void "
                    + funcname
                    + "_cp(struct "
                    + hybridft.name
                    + "* global_"
                    + hybridname
                    + ", struct "
                    + hybridft.name
                    + "* "
                    + hybridname
                    + ")"
                )
                f.write(funcnamestr + "{\n")
                self.ConstOpCP.append(funcnamestr)
                f.write("  int i,j,k,p;\n\n")
                print(hybridft.items)
                for fieldname, field in iter_hybridfield(funcmesh[0][1]):
                    # fieldname = 'debug'
                    # print ("hybridfts:"+str(field.ref))
                    if field.info.shape[2] == 1:
                        f.write("  for (k = 0 ; k < 1 ; k ++)\n")
                    else:
                        if field.info.desc.pos[2]:
                            f.write("  for (k = 0 ; k < Proc.full_nlev + 2*Proc.lev_hw ; k ++)\n")
                        else:
                            f.write("  for (k = 0 ; k < Proc.half_nlev + 2*Proc.lev_hw ; k ++)\n")
                    if field.info.shape[1] == 1:
                        f.write("    for (j = 0 ; j < 1 ; j ++)\n")
                    else:
                        if field.info.desc.pos[1]:
                            f.write("    for (j = 0 ; j < Proc.full_nlat + 2*Proc.lat_hw ; j ++)\n")
                        else:
                            f.write("    for (j = 0 ; j < Proc.half_nlat + 2*Proc.lat_hw ; j ++)\n")
                    if field.info.shape[0] == 1:
                        f.write("      for (i = 0 ; i < 1 ; i ++)\n")
                    else:
                        if field.info.desc.pos[0]:
                            f.write(
                                "      for (i = 0 ; i < Proc.full_nlon + 2*Proc.lon_hw ; i ++)\n"
                            )
                        else:
                            f.write(
                                "      for (i = 0 ; i < Proc.half_nlon + 2*Proc.lon_hw ; i ++)\n"
                            )

                    if field.info.shape[1] != 1:
                        f.write(
                            "        "
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j][i] = global_"
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j + Proc.lat_beg][i];\n"
                        )
                    elif field.info.shape[0] != 1:
                        f.write(
                            "        "
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j][i] = global_"
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j][i + Proc.lon_beg];\n"
                        )
                    else:
                        f.write(
                            "        "
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j][i] = global_"
                            + hybridname
                            + "->"
                            + fieldname
                            + "[k][j][i];\n"
                        )

                    f.write("\n")

            f.write("}\n")

        # Profiling OutPut
        if gc.Profiling:
            f.write("\n")
            f.write("void ProfilingOutPut(int id){\n")
            f.write('  char filename[30] = "Profiling_";\n')
            f.write('  char ts[10] = ".txt";\n')
            f.write("  char sid[10];\n\n")
            f.write('  sprintf(sid,"%d",id);\n')
            f.write("  strcat(filename,sid);\n")
            f.write("  strcat(filename,ts);\n")
            f.write('  freopen(filename, "w", stdout);\n')
            f.write('  printf("Total %.6f\\n", CommTime+CompTime);\n')
            f.write('  printf("Comp %.6f\\n", CompTime);\n')
            f.write('  printf("Comm %.6f\\n", CommTime);\n')
            for name in self.ProfilingName:
                f.write('  printf("' + name + 'Time %.6f\\n", ' + name + "Time);\n")
            f.write("  fclose(stdout);\n")
            f.write("}\n\n")

        f.close()

        # 头文件补生成cp函数与init finish函数
        f = open(head_name, "a")

        for declare in self.ConstOpCP:
            f.write(declare + ";\n")

        f.write("#endif\n")
        f.close()

        # for hybrid,list in self.GlobalVar.items():
        #     if list[2]:
        #         pass
        # print(self.ConstOpInfo)

    def mainIn(self):
        self.append("int main(int argc, char **argv)")
        self.append("{")
        self.indent_in()

    def MPI_Init(self):
        self.append("int size,rank;")
        self.append("double tottime_beg, tottime_end;")

        self.append("MPI_Init(&argc, &argv);")
        self.append("MPI_Comm_size(MPI_COMM_WORLD, &size);")
        self.append("MPI_Comm_rank(MPI_COMM_WORLD, &rank);")
        if gc.Grid.GridType == "LonLat":
            self.append(
                "ProcInit_LonLat_Domain(&Proc,MPI_COMM_WORLD,ProcLatNum,ProcLon,ProcLat,nlon,nlat,nlev);"
            )
        elif gc.Grid.GridType == "CubedSphere":
            self.append(
                "ProcInit_CubedSphere_Domain(&Proc,MPI_COMM_WORLD,size,rank,ProcLatNum,ProcLon,ProcLat,ncell,nlev);"
            )
        else:
            pass
        self.append("")

        self.append("//Proc Ngb Init")
        # 按不同进程的halo范围,预处理邻居关系
        for ProcHalo in Proc.HaloTileList:
            self.append(
                "if (Proc.lat_beg >= "
                + str(ProcHalo.range[0])
                + " && Proc.lat_end <= "
                + str(ProcHalo.range[1])
                + "){"
            )
            self.indent_in()
            if gc.Grid.GridType == "LonLat":
                # ToRemember Lonself
                self.append(
                    "ProcInit_LonLat_Ngb(&Proc,MPI_COMM_WORLD,ProcLatNum,ProcLon,ProcLat,nlon,nlat,nlev,"
                    + IntListToC(str(ProcHalo.hw))
                    + ", "
                    + str(gc.Grid.ExternHalo[0])
                    + ", 2, DTYPE_DOUBLE, "
                    + str(self.fieldnum + 10)
                    + ");"
                )
            elif gc.Grid.GridType == "CubedSphere":
                self.append(
                    "ProcInit_CubedSphere_Ngb(&Proc,MPI_COMM_WORLD,size,rank,ProcLon[0],ProcLat[0],ncell,nlev,"
                    + IntListToC(str(ProcHalo.hw))
                    + ", "
                    + str(self.PanelHalo)
                    + ", DTYPE_DOUBLE, "
                    + str(self.fieldnum + 10)
                    + ");"
                )
            else:
                pass
            self.indent_out()
            self.append("}")

        self.append("")
        self.append("PhysicalVariableInit();")
        self.append("")
        # Toremember Timeinit here
        self.append("TimeInit();")
        self.append("")

    def getUniqueProc(self):
        tid = 0
        for item in self.ProcInfoList:
            prange = item.ProcRange
            self.append(
                "if (Proc.lat_beg >= "
                + str(prange[0])
                + " && Proc.lat_end <= "
                + str(prange[1])
                + ")"
            )
            self.append("{")
            self.indent_in()

            # #邻居init
            # self.append("ProcInit_LonLat_Ngb(&Proc,MPI_COMM_WORLD,ProcLatNum,ProcLon,ProcLat,nlon,nlat,nlev," + IntListToC(str(item.ProcHaloRange)) +  ", " + str(gc.Grid.CornerHalo) + ", DTYPE_DOUBLE, "+ str(self.fieldnum + 10) + ");")

            # 变量malloc
            # self.append("PhysicalVariableInit();")

            for nid in range(len(self.MainTimeOpList)):
                tname = self.MainTimeOpList[nid]
                targs = self.MainTimeOpArgs[nid]
                tlength = self.MainTimeOpStep[nid][0]
                tstep = self.MainTimeOpStep[nid][1]
                if tlength == tstep:
                    self.append(tname + "_" + str(tid) + targs + ";")
                else:
                    self.append("tottime_beg = MPI_Wtime();")
                    self.append(
                        "for (int t = 0; t < " + str(tlength) + "; t += " + str(tstep) + "){"
                    )
                    self.indent_in()
                    self.append(tname + "_" + str(tid) + targs + ";")
                    self.indent_out()
                    self.append("}")
                    self.append("tottime_end = MPI_Wtime();")

            self.indent_out()
            self.append("}")
            self.append("")
            tid = tid + 1

    def mainOut(self):
        if gc.Profiling:
            self.append("ProfilingOutPut(Proc.id);")

        self.append('if (Proc.id == 0) printf("Time is %.8f\\n",tottime_end-tottime_beg);')
        # self.append("PhysicalVariableFinish();")
        self.indent_out()
        self.append("}")

    def mainOutput(self, file_name=-1):
        self.mainIn()
        self.MPI_Init()

        if isinstance(gc.Backend, SWDesc):
            self.append("athread_init();")
            self.append("")

            self.append("global_info gi;")
            self.append("gi.fnx = Proc.full_nlon;")
            self.append("gi.fny = Proc.full_nlat;")
            self.append("gi.fnz = Proc.full_nlev;")
            self.append("gi.hnx = Proc.half_nlon;")
            self.append("gi.hny = Proc.half_nlat;")
            self.append("gi.hnz = Proc.half_nlev;")
            self.append("gi.ghx = Proc.lon_hw;")
            self.append("gi.ghy = Proc.lat_hw;")
            self.append("gi.ghz = Proc.lev_hw;")
            self.append("athread_spawn(global_prepare, &gi);")
            self.append("athread_join();")
            self.append("")

        self.getUniqueProc()
        self.mainOut()

        if file_name == -1:
            print(str(self))
        else:
            f = open(file_name, "a")
            f.write(str(self))
            f.close()

    def x86InculdeOutput(self, file_name=-1):
        f = open(file_name, "a")
        f.write(
            "#include <stdio.h>\n#include <stdlib.h>\n#include<stdbool.h>\n#include<string.h>\n#include<math.h>\n\n"
        )

        for externH in self.ExternHList:
            f.write('#include"../ExternLIB/' + externH + '.h"\n')
        f.write("\n")

        f.write(
            '#include"../LIB/Process.h"\n#include"../LIB/Communicator.h"\n#include"../LIB/ParaParam.h"\n#include"../LIB/Async.h"\n#include"../LIB/NCop.h"\n#include"../LIB/Time.h"\n#include"../LIB/Memory.h"\n#include"../LIB/Diagnose.h"\n\n'
        )
        f.write('#include"namelist.h"\n#include"physical_variable.h"\n\n')

        f.write("#define MIN(a,b) ((a) < (b) ? (a) : (b))\n")
        f.write("#define MAX(a,b) ((a) > (b) ? (a) : (b))\n\n")

    def NamelistHeaderOutPut(self, file_name=-1):
        if file_name == -1:
            sys.exit("Input NamelistHeader filename")
        else:
            f = open(file_name, "a")
            f.write("#ifndef NAMELIST_H_INCLUDED\n")
            f.write("#define NAMELIST_H_INCLUDED 1\n")
            # grid
            f.write("int nlon = " + str(gc.Grid.NumLon) + ";\n")
            f.write("int nlat = " + str(gc.Grid.NumLat) + ";\n")
            f.write("int nlev = " + str(gc.Grid.NumLev) + ";\n")
            if gc.Grid.GridType == "CubedSphere":
                if gc.Grid.NumLat != gc.Grid.NumLon:
                    print("Wrong Grid! Lon != Lat\n")
                    exit()
                else:
                    f.write("int ncell = " + str(gc.Grid.NumLon) + ";\n")
            # proc
            f.write("int ProcNum = " + str(gc.ProcNum) + ";\n")
            f.write(
                "int ProcLatNum["
                + str(len(Proc.ProcPartition.TileLatNum))
                + "] = "
                + ListToArray(str(Proc.ProcPartition.TileLatNum))
                + ";\n"
            )
            f.write(
                "int ProcLon["
                + str(len(Proc.ProcPartition.TileProcLon))
                + "] = "
                + ListToArray(str(Proc.ProcPartition.TileProcLon))
                + ";\n"
            )
            f.write(
                "int ProcLat["
                + str(len(Proc.ProcPartition.TileProcLat))
                + "] = "
                + ListToArray(str(Proc.ProcPartition.TileProcLat))
                + ";\n"
            )
            f.write("#endif")
            f.close()

    def swMasterInculdeOutput(self, file_name=-1):
        if file_name == -1:
            sys.exit("Input swMaster filename")
        else:
            f = open(file_name, "a")
            f.write(
                "#include <stdio.h>\n#include <stdlib.h>\n#include <string.h>\n#include <math.h>\n#include <time.h>\n#include <sys/time.h>\n#include <crts.h>\n\n"
            )

            for externH in self.ExternHList:
                f.write('#include"../ExternLIB/' + externH + '.h"\n')
            f.write("\n")

            f.write(
                '#include"../LIB/Process.h"\n#include"../LIB/Communicator.h"\n#include"../LIB/ParaParam.h"\n#include"../LIB/Async.h"\n#include"../LIB/NCop.h"\n#include"../LIB/Time.h"\n#include"../LIB/Memory.h"\n#include"../LIB/Diagnose.h"\n\n'
            )
            f.write('#include"namelist.h"\n#include"physical_variable.h"\n\n')
            f.write('#include "slave_struct.h"\n\n')

            f.write("#define MIN(a,b) ((a) < (b) ? (a) : (b))\n")
            f.write("#define MAX(a,b) ((a) > (b) ? (a) : (b))\n\n")

            f.write("extern SLAVE_FUN(global_prepare)(void*);\n")

            # for key in self.spaceOpDictSlaveDeclare:
            #     code = self.spaceOpDictSlaveDeclare[key]
            #     for item in code:
            #         f.write("extern SLAVE_FUN(" + item + ")(void*);\n")
            #     f.write ('\n')

            for key, value in self.SlaveDeclareMap.items():
                if value == 2:
                    f.write("extern SLAVE_FUN(" + key + ")(void*);\n")
            f.write("\n")

    def swSlaveStructOutput(self, file_name=-1):
        if file_name == -1:
            sys.exit("Input swMaster filename")
        else:
            f = open(file_name, "a")

            f.write("typedef struct{\n")
            f.write("  int fnx,fny,fnz;\n")
            f.write("  int hnx,hny,hnz;\n")
            f.write("  int ghx,ghy,ghz;\n")
            f.write("}global_info;\n\n")

            # for line in self.globalslaveheader:
            #     f.write(line)

            for key in self.spaceOpDictSlaveStruct:
                code = self.spaceOpDictSlaveStruct[key]
                for item in code:
                    f.write(item)
                f.write("\n")
            f.close()

            f.close()

    def swSlaveIncludeOutput(self, file_name=-1):
        if file_name == -1:
            sys.exit("Input swSlave filename")
        else:
            f = open(file_name, "a")
            f.write(
                '#include <stdio.h>\n#include <stdlib.h>\n#include <simd.h>\n#include <math.h>\n#include "slave.h"\n\n'
            )
            f.write('#include "CPE.h"\n')
            f.write('#include "slave_struct.h"\n')
            f.write('#include "physical_variable.h"\n')

            f.write("#define MIN(a,b) ((a) < (b) ? (a) : (b))\n")
            f.write("#define MAX(a,b) ((a) > (b) ? (a) : (b))\n\n")

            # 全局参数
            f.write("__thread_local int fnx;\n")
            f.write("__thread_local int fny;\n")
            f.write("__thread_local int fnz;\n")
            f.write("__thread_local int hnx;\n")
            f.write("__thread_local int hny;\n")
            f.write("__thread_local int hnz;\n")
            f.write("__thread_local int ghx;\n")
            f.write("__thread_local int ghy;\n")
            f.write("__thread_local int ghz;\n\n")

            f.write("void global_prepare(void *_ptr){\n")
            f.write("  global_info *gi = (global_info*)(_ptr);\n")
            f.write("  fnx = gi->fnx;\n")
            f.write("  fny = gi->fny;\n")
            f.write("  fnz = gi->fnz;\n")
            f.write("  hnx = gi->hnx;\n")
            f.write("  hny = gi->hny;\n")
            f.write("  hnz = gi->hnz;\n")
            f.write("  ghx = gi->ghx;\n")
            f.write("  ghy = gi->ghy;\n")
            f.write("  ghz = gi->ghz;\n")
            f.write("}\n\n")

            # 头部函数
            f.write(
                "static void CalcID(int *id, int *rid, int *cid, int *w, int *e, int *s, int *n, int mx, int my){\n"
            )
            f.write("  *id = _MYID;\n")
            f.write("  *rid = ROW(_MYID);\n")
            f.write("  *cid = COL(_MYID);\n\n")
            f.write("  if ((*cid % mx) == 0) *w = -1;\n")
            f.write("  else *w = *id - 1;\n")
            f.write("  if ((*cid % mx) == (mx - 1)) *e = -1;\n")
            f.write("  else *e = *id + 1;\n")
            f.write("  if ((*rid % my) == 0) *s = -1;\n")
            f.write("  else *s = *id - 8;\n")
            f.write("  if ((*rid % my) == (my - 1)) *n = -1;\n")
            f.write("  else *n = *id + 8;\n")
            f.write("}\n\n")

            f.write(
                "static void RoundRobin(int n, int p, int size, int *beg, int *end, int *len){\n"
            )
            f.write("  int cur = 0;\n")
            f.write("  int i;\n")
            f.write("  int cursize;\n")
            f.write("  for (i = 0 ; i < p ; i++){\n")
            f.write("    if (size % (n - i) == 0) cursize = size / (n - i);\n")
            f.write("    else cursize = size / (n - i) + 1;\n")
            f.write("    size -= cursize;\n")
            f.write("    cur += cursize;\n")
            f.write("  }\n")
            f.write("  *beg = cur;\n")
            f.write("  if (size % (n - p) == 0) cursize = size / (n - p);\n")
            f.write("  else cursize = size / (n - p) + 1;\n")
            f.write("  *len = cursize;\n")
            f.write("  *end = *beg + cursize;\n")
            f.write("}\n\n")

            f.write(
                "static void CalcRange(int id ,int rid, int cid, int nx,int ny, int nz, int mx, int my, int mz, \\ \n"
            )
            f.write(
                "                      int *xbeg, int *xend, int *xlen, int *ybeg, int *yend, int *ylen, int *zbeg, int *zend, int *zlen){\n"
            )
            f.write("  int px,py,pz;\n")
            f.write("  pz = ((rid / my) * (8 / mx) + (cid / mx));\n")
            f.write("  RoundRobin(mz,pz,nz,zbeg,zend,zlen);\n")
            f.write("  py = rid % my;\n")
            f.write("  RoundRobin(my,py,ny,ybeg,yend,ylen);\n")
            f.write("  px = cid % mx;\n")
            f.write("  RoundRobin(mx,px,nx,xbeg,xend,xlen);\n")
            f.write("}\n\n")

    def x86Output(self, main_name=-1, field_name=-1, namelist_name=-1):
        # include_x86
        if main_name != -1:
            f = open(main_name, "w")
            f.close()
        else:
            sys.exit("Input Main filename")

        if field_name != -1:
            f = open(field_name + ".h", "w")
            f.close()
            f = open(field_name + ".c", "w")
            f.close()
        else:
            sys.exit("Input Field filename")

        if namelist_name != -1:
            f = open(namelist_name, "w")
            f.close()
        else:
            sys.exit("Input Namelist filename")

        self.fieldOutput(field_name + ".h", field_name + ".c")

        self.x86InculdeOutput(main_name)
        self.functionOutput(main_name)
        self.spaceOutput(main_name)
        self.timeOutput(main_name)
        self.NamelistHeaderOutPut(namelist_name)
        self.mainOutput(main_name)

    def swMasterOutput(self, main_name=-1, field_name=-1, namelist_name=-1):
        if main_name != -1:
            f = open(main_name, "w")
            f.close()
        else:
            sys.exit("Input Main filename")

        if field_name != -1:
            f = open(field_name + ".h", "w")
            f.close()
            f = open(field_name + ".c", "w")
            f.close()
        else:
            sys.exit("Input Field filename")

        if namelist_name != -1:
            f = open(namelist_name, "w")
            f.close()
        else:
            sys.exit("Input Namelist filename")
        # include_sw_master
        self.fieldOutput(field_name + ".h", field_name + ".c")
        self.swMasterInculdeOutput(main_name)
        self.functionOutput(main_name)
        self.spaceOutput(main_name)
        self.timeOutput(main_name)
        self.NamelistHeaderOutPut(namelist_name)
        self.mainOutput(main_name)

    def swSlaveOutput(self, file_name=-1, head_name=-1):
        if head_name != -1:
            f = open(head_name, "w")
            f.close()
        else:
            sys.exit("Input SlaveHead filename")

        if file_name != -1:
            f = open(file_name, "w")
            f.close()
        else:
            sys.exit("Input Slave filename")

        self.swSlaveStructOutput(head_name)
        self.swSlaveIncludeOutput(file_name)
        self.slavefunctionOutput(file_name)
        self.slavespaceOutput(file_name)

    def __str__(self) -> str:
        return "\n".join(self.lines)


CodeGenController = CodeGenerator()
