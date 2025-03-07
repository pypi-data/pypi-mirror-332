from bamboo.optim.proc.globalanalyse import Proc
from bamboo.codegen.opvisit import OpVisitor
from bamboo.codegen import CodeGenController
from bamboo.configuration import GlobalConfiguration, SWDesc
from typing import List
from copy import deepcopy
import os

# optimize & codegen


def ToBackend():
    Proc.GlobalAnalyse()

    FuncList = OpVisitor()
    for item in CodeGenController.funcList:
        FuncList(item)
    CodeGenController.funcOpCode = FuncList

    CodeGenController.ProcInfoList.extend(deepcopy(Proc.UniqueProcTimeOpList))
    CodeGenController.MainTimeOpList.extend(deepcopy(Proc.TimeOpNameList))
    CodeGenController.MainTimeOpArgs.extend(deepcopy(Proc.TimeOpArgList))
    CodeGenController.MainTimeOpStep.extend(deepcopy(Proc.TimeOpStepList))
    CodeGenController.PanelHalo = Proc.PanelHalo
    CodeGenController.ExternHList = Proc.ExternList

    # print ('timeOpList:')
    OpList: List[OpVisitor] = []
    Profiling: List[str] = []
    SlaveFuncName: List[str] = []
    id = 0
    for item in Proc.UniqueProcTimeOpList:
        timeOpList = item.TimeOpList
        OpVisit = OpVisitor()
        for timeOp in timeOpList:
            for spaceOp in timeOp:
                SlaveFuncName, Profiling = OpVisit(
                    spaceOp["op"], id, item.FieldHaloRange, item.ProcHaloRange
                )
                for name in SlaveFuncName:
                    if name not in CodeGenController.SlaveFuncName:
                        CodeGenController.SlaveFuncName.append(name)

                for name in Profiling:
                    if name not in CodeGenController.ProfilingName:
                        CodeGenController.ProfilingName.append(name)

                # globalslavefunclist, globalslaveheader = OpVisit(spaceOp['op'], id, item.FieldHaloRange, item.ProcHaloRange)
                # CodeGenController.globalslavefunclist.extend(globalslavefunclist)
                # CodeGenController.globalslaveheader.extend(globalslaveheader)
        OpList.append(OpVisit)
        id = id + 1

    CodeGenController.spaceList.extend(deepcopy(OpList))

    CodeGenController.fieldAggregate()  # Get all hybridfield info from spaceOps

    CodeGenController.VarProcess()

    if isinstance(GlobalConfiguration.Backend, SWDesc):
        # SW
        print("sw output")
        # print(CodeGenController.globalslavefunclist)
        CodeGenController.swMasterOutput(
            os.path.join("code", "src", "master.c"),
            os.path.join("code", "src", "physical_variable"),
            os.path.join("code", "src", "namelist.h"),
        )
        CodeGenController.swSlaveOutput(
            os.path.join("code", "src", "slave.c"),
            os.path.join("code", "src", "slave_struct.h"),
        )
    else:
        # x86
        print("x86 output")
        CodeGenController.x86Output(
            os.path.join("code", "src", "main.c"),
            os.path.join("code", "src", "physical_variable"),
            os.path.join("code", "src", "namelist.h"),
        )
