from typing import Any, List, Optional, Tuple, cast, Dict, Set
import copy
from dataclasses import dataclass
from collections import Counter

from bamboo.lang.dtype import FieldInfo, FieldRef
from bamboo.lang.ir import IRCallable, IRSpace, IRTransformer, Stat, IRVisitor
from bamboo.lang.ir.expr import FieldExpr, AttrExpr, IntExpr
from bamboo.lang.ir.stat import ForStat, AssignStat

from bamboo.optim.trans import ParForStat

from bamboo.optim.proc import OptForStat, UniqueProcASTInfo, FieldVarInfo
from bamboo.optim.proc.haloanalyzer import HaloAnalyzer
from bamboo.optim.proc.partition import (
    ProcessPartition,
    PartitionConfiguration,
    ProcessTile,
)
from bamboo.optim.proc.OptForTransformer import OptForTransformer
from bamboo.optim.proc.ProcASTClassify import ProcASTClassify
from bamboo.optim.proc.graph import FieldGraph
from bamboo.optim.proc.conditionanalyzer import LonHaloPreLatCondition, HaloProcTileInfo

from bamboo.optim.SW.swOptMain import swOptMain
from bamboo.optim.SW.singlekernel import SWOptForTransformerSingle

from bamboo.configuration import GlobalConfiguration as gc, SWDesc


# 输入完整OPList,包含Time_OP中所有Space_OP
class ProcInfoMain:
    TimeOpNameList: List[str] = []
    TimeOpArgList: List[str] = []
    TimeOpList: List[List[Tuple[str, List[Any]]]] = []
    TimeOpStepList: List[Tuple[int, int]] = []
    UniqueProcTimeOpList: List[UniqueProcASTInfo] = []  # 不同类AST的副本
    GlobalParaZone: List = [True, True, True]
    FieldHaloRange: Dict[int, List] = {}
    GlobalHaloRange: List[int] = [0, 0, 0]  # 全局halo宽度大小，HaloLon,HaloLat,HaloLev
    GlobalConst: List[FieldVarInfo] = []
    HaloTileList: List[HaloProcTileInfo]
    PanelHalo: int = 0  # 立方球中panel边界处halo宽度,由所用插值决定
    ExternList: Set[int] = set()  # 存放外部库头文件列表

    # 进程划分
    ProcPartition: PartitionConfiguration

    # 同类进程列表
    GlobalInvolvedProcList: List[List[int]] = []

    def __call__(self, OP_info: tuple):
        self.TimeOpNameList.append(OP_info[0])
        self.TimeOpArgList.append(OP_info[1])
        self.TimeOpList.append(OP_info[2])  # spaceOpList
        self.TimeOpStepList.append(OP_info[3])  # timelength, timestep

        return OP_info

    def isAssignField(self, ir: Stat) -> bool:
        if not isinstance(ir, AssignStat):
            return False

        return isinstance(ir.dst, FieldExpr)

    # Diss 是否可以不管普通For? 目前结论 普通for将影响全局并行域
    def AnalysisForZone(self, ir: ForStat):
        noParaVar: List = []
        current_body: List = []
        noParaDim: List = [True, True, True]

        current_body.append(ir)

        depth = 0

        while depth < 3 and len(current_body) == 1 and isinstance(current_body[0], ForStat):
            for_stat = cast(ForStat, current_body[0])
            noParaVar.append(for_stat.var)
            current_body = for_stat.body
            depth += 1

        while isinstance(current_body[0], ForStat):
            for_stat = cast(ForStat, current_body[0])
            current_body = for_stat.body

        for stat in current_body:
            if self.isAssignField(stat):
                fieldVar = cast(FieldExpr, stat.dst)
                for id, expr in enumerate(fieldVar.idx):
                    idxvar = expr.var
                    if idxvar in noParaVar:
                        noParaDim[id] = False
                break

        for i in range(0, 3):
            self.GlobalParaZone[i] = self.GlobalParaZone[i] & noParaDim[i]

    def AnalysisParaForZone(self, ir: ParForStat):
        paraVar: List = []
        noParaVar: List = []
        current_body: List = []
        noParaDim: List = [True, True, True]

        depth = len(ir.ranges)
        for ParForRange in ir.ranges:
            paraVar.append(ParForRange.var)

        current_body = ir.body

        while depth < 3 and len(current_body) == 1 and isinstance(current_body[0], ParForStat):
            for_stat = cast(ParForStat, current_body[0])
            noParaVar.append(for_stat.var)
            current_body = for_stat.body
            depth += 1

        while isinstance(current_body[0], ForStat):
            for_stat = cast(ForStat, current_body[0])
            current_body = for_stat.body

        for stat in current_body:
            if self.isAssignField(stat):
                fieldVar = cast(FieldExpr, stat.dst)
                for id, expr in enumerate(fieldVar.idx):
                    # Fix: 常量坐标可能影响并行域?
                    if isinstance(expr, IntExpr):
                        continue
                    idxvar = expr.var
                    if idxvar in noParaVar:
                        noParaDim[id] = False
                break

    def AnalysisGlobalParaZone(self, ctx: IRCallable):
        for stat in ctx.body:
            if isinstance(stat, ForStat):
                self.AnalysisForZone(stat)

            if isinstance(stat, ParForStat):
                self.AnalysisParaForZone(stat)

    def UpdateGlobalHaloRange(
        self, spaceDict: Dict[FieldInfo, List], ProcAstInfo: UniqueProcASTInfo = None
    ):
        if ProcAstInfo == None:
            for key in spaceDict:
                if key in self.FieldHaloRange:
                    for i in range(0, 6):
                        if i & 1:
                            self.FieldHaloRange[key][i] = max(
                                self.FieldHaloRange[key][i], spaceDict[key][i]
                            )
                        else:
                            self.FieldHaloRange[key][i] = min(
                                self.FieldHaloRange[key][i], spaceDict[key][i]
                            )
                else:
                    self.FieldHaloRange[key] = spaceDict[key]

                self.GlobalHaloRange[0] = max(
                    self.GlobalHaloRange[0],
                    max(abs(self.FieldHaloRange[key][0]), self.FieldHaloRange[key][1]),
                )
                self.GlobalHaloRange[1] = max(
                    self.GlobalHaloRange[1],
                    max(abs(self.FieldHaloRange[key][2]), self.FieldHaloRange[key][3]),
                )
                self.GlobalHaloRange[2] = max(
                    self.GlobalHaloRange[2],
                    max(abs(self.FieldHaloRange[key][4]), self.FieldHaloRange[key][5]),
                )
        else:
            # print("Why~!!!" , spaceDict)
            for key in spaceDict:
                if key in ProcAstInfo.FieldHaloRange:
                    for i in range(0, 6):
                        if i & 1:
                            ProcAstInfo.FieldHaloRange[key][i] = max(
                                ProcAstInfo.FieldHaloRange[key][i], spaceDict[key][i]
                            )
                        else:
                            ProcAstInfo.FieldHaloRange[key][i] = min(
                                ProcAstInfo.FieldHaloRange[key][i], spaceDict[key][i]
                            )
                else:
                    ProcAstInfo.FieldHaloRange[key] = spaceDict[key]
                ProcAstInfo.ProcHaloRange[0] = max(
                    ProcAstInfo.ProcHaloRange[0],
                    max(
                        abs(ProcAstInfo.FieldHaloRange[key][0]),
                        ProcAstInfo.FieldHaloRange[key][1],
                    ),
                )
                ProcAstInfo.ProcHaloRange[1] = max(
                    ProcAstInfo.ProcHaloRange[1],
                    max(
                        abs(ProcAstInfo.FieldHaloRange[key][2]),
                        ProcAstInfo.FieldHaloRange[key][3],
                    ),
                )
                ProcAstInfo.ProcHaloRange[2] = max(
                    ProcAstInfo.ProcHaloRange[2],
                    max(
                        abs(ProcAstInfo.FieldHaloRange[key][4]),
                        ProcAstInfo.FieldHaloRange[key][5],
                    ),
                )

    def UpdateInvolvedProcList(self, InvolvedList: List[List[int]]):
        for listnew in InvolvedList:
            flag = True
            for listold in self.GlobalInvolvedProcList:
                ta = Counter(listnew)
                tb = Counter(listold)
                if ta == tb:
                    flag = False
                    break
            if flag:
                self.GlobalInvolvedProcList.append(listnew)

    def UpdateGolbalConst(self, ConstField: List[FieldVarInfo]):
        for field in ConstField:
            if field not in self.GlobalConst:
                self.GlobalConst.append(field)

    def AnalyseInvolvedProcList(self, ProcNum: int):
        InvolvedList: List[List[int]] = [None] * len(self.GlobalInvolvedProcList)
        Involved: List[List[int]] = [None] * len(self.GlobalInvolvedProcList)  # return List
        minlist: List[List[int]] = []
        ProcDict: Dict[int, bool] = {}

        pl = 0
        pr = len(self.GlobalInvolvedProcList) - 1

        print(self.GlobalInvolvedProcList)

        # **默认已知gmcore的负载规律
        while len(self.GlobalInvolvedProcList):
            minlist.clear()
            for list in self.GlobalInvolvedProcList:
                if len(minlist) == 0:
                    minlist.append(list)
                elif len(list) < len(minlist[0]):
                    minlist.clear()
                    minlist.append(list)
                elif len(list) == len(minlist[0]):
                    minlist.append(list)

            if len(minlist) == 1:
                InvolvedList[pl] = minlist[0]
                pl += 1
            elif len(minlist) == 2:
                if minlist[0][0] < minlist[1][0]:
                    InvolvedList[pl] = minlist[0]
                    InvolvedList[pr] = minlist[1]
                else:
                    InvolvedList[pl] = minlist[1]
                    InvolvedList[pr] = minlist[0]
                pl += 1
                pr -= 1

            for list in minlist:
                self.GlobalInvolvedProcList.remove(list)
        print(InvolvedList)
        for x in range(0, ProcNum):
            ProcDict[x] = False

        pl = 0
        pr = len(InvolvedList) - 1
        while pl <= pr:
            tmp = []
            if len(InvolvedList[pl]) <= len(InvolvedList[pr]):
                p = pl
                pl += 1
            else:
                p = pr
                pr -= 1
            for x in InvolvedList[p]:
                if ProcDict[x]:
                    pass
                else:
                    ProcDict[x] = True
                    tmp.append(x)
            Involved[p] = copy.deepcopy(tmp)

        for list in Involved:
            if list != []:
                self.GlobalInvolvedProcList.append(copy.deepcopy(list))

    def TimeOPListCloner(self):
        # 按进程组依次备份
        for ProcList in self.GlobalInvolvedProcList:
            Range: Tuple[int, int] = (
                self.ProcPartition.TileProcList[ProcList[0]].range[0],
                self.ProcPartition.TileProcList[ProcList[-1]].range[1],
            )
            newASTInfo = UniqueProcASTInfo(ProcList, Range, self.TimeOpList)
            # 只保留本进程组会计算到的AST
            for timeOP in newASTInfo.TimeOpList:
                for spaceOP in timeOP:
                    ProcASTClassify()(spaceOP["op"], ProcList, Range)
                    spaceDict, GHDict, ExternL = HaloAnalyzer()(spaceOP["op"])
                    self.UpdateGlobalHaloRange(spaceDict, newASTInfo)

                    # ToDo处理不同optfor间额外update的情况,删除多余语句,增加kernel信息后删除此段
                    curkernel: Dict[int, str] = {}  # 记录每个变量上一次出现时在哪个kernel中

                    for ctx in reversed(spaceOP["op"].body):
                        if isinstance(ctx, OptForStat):
                            if ctx.FieldOut == []:
                                pass
                            else:
                                for field in ctx.FieldOut:
                                    fieldid = field.id
                                    kernel = ctx.ranges[0].var.prefix
                                    if (not curkernel.__contains__(fieldid)) or curkernel[
                                        fieldid
                                    ] != kernel:
                                        curkernel[fieldid] = kernel
                                    else:
                                        field.UpdateHalo = False

            # #根据condition设置信息
            # if gc.LonHaloPreLat != []:
            #     for i in range(newASTInfo.ProcRange[0],newASTInfo.ProcRange[1] + 1):
            #         newASTInfo.ProcHaloRange[0] = max(newASTInfo.ProcHaloRange[0], gc.LonHaloPreLat[i])

            newASTInfo.ProcHaloRange[0] = max(newASTInfo.ProcHaloRange[0], gc.Grid.ExternHalo[1])
            newASTInfo.ProcHaloRange[1] = max(newASTInfo.ProcHaloRange[1], gc.Grid.ExternHalo[1])
            newASTInfo.ProcHaloRange[2] = max(newASTInfo.ProcHaloRange[2], gc.Grid.ExternHalo[2])

            self.UniqueProcTimeOpList.append(newASTInfo)

            print("!!!!ProcList\n")
            print(newASTInfo.ProcTlieList, newASTInfo.ProcRange)
            print(newASTInfo.FieldHaloRange)
            print(newASTInfo.ProcHaloRange)
            # print(newASTInfo.TimeOpList[0][0]['op'])
            print("End of ProcList")

    # 全局分析 并行域; field halo; 每个loop涉及的进程
    def GlobalAnalyse(self):
        for timeOP in self.TimeOpList:
            print("?" * 30)
            print(timeOP)
            print("?" * 30)
            for spaceOP in timeOP:
                print("*" * 30)
                print(spaceOP)
                print(spaceOP["op"])
                print("*" * 30)
                self.AnalysisGlobalParaZone(spaceOP["op"])
                spaceDict, GHDict, ExternL = HaloAnalyzer()(spaceOP["op"])
                self.UpdateGlobalHaloRange(spaceDict)
                for extern in ExternL:
                    self.ExternList.add(extern)

        print("=======Global Halo Range=========\n")
        print(self.FieldHaloRange)
        print(self.GlobalHaloRange)
        print("=" * 30)

        print("=======Partition=========\n")
        self.ProcPartition = ProcessPartition()(self.GlobalParaZone)
        print(self.ProcPartition)
        print("=" * 30)

        # 转换forstate到带优化信息的OptFor
        for timeOP in self.TimeOpList:
            for spaceOP in timeOP:
                InvolvedList, ConstField = OptForTransformer()(
                    spaceOP["op"], self.FieldHaloRange, GHDict, self.ProcPartition
                )
                self.UpdateInvolvedProcList(InvolvedList)
                self.UpdateGolbalConst(ConstField)

        # ToDo: 考虑非规则的多种划分与多proclist的关系
        self.AnalyseInvolvedProcList(self.ProcPartition.ProcNum)

        print("#?" * 30)
        print(self.GlobalInvolvedProcList)

        # CubedSphere panel分析
        self.PanelHalo = 2

        # 根据划分和OptFor信息，根据计算流程，将AST分入多个副本; 每个副本维护自己的区域大小,halo大小
        self.TimeOPListCloner()

        # 考虑给入的LonHaloPreLat条件
        self.HaloTileList = LonHaloPreLatCondition(self.ProcPartition, self.UniqueProcTimeOpList)
        print("HaloTileList!!!!! ")
        for haloProc in self.HaloTileList:
            print(haloProc.range, haloProc.hw)

        # print("FFFFFFFF")
        # print(GHDict)

        # 各自SW优化
        if isinstance(gc.Backend, SWDesc):
            swOpt = swOptMain(self.UniqueProcTimeOpList, self.ProcPartition)
            swOpt.SWOpt()

            # print("*" * 30 + "SW OPT")
            # print(self.UniqueProcTimeOpList[0].TimeOpList[0][0]['op'])


Proc = ProcInfoMain()
