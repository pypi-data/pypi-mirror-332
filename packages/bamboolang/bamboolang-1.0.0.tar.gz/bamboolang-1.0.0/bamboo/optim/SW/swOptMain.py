from typing import Dict, List, cast, Tuple

from bamboo.optim.proc import OptForStat, UniqueProcASTInfo
from bamboo.optim.proc.partition import (
    ProcessPartition,
    PartitionConfiguration,
    ProcessTile,
)

from bamboo.optim.SW.singlekernel import SWOptForTransformerSingle

from bamboo.configuration import GlobalConfiguration


# SW后端优化总控
class swOptMain:
    UniqueProcTimeOpList: List[UniqueProcASTInfo] = []  # 不同类AST的副本
    ProcPartition: PartitionConfiguration

    def ProcTileRange(self, UniqueProcAST: UniqueProcASTInfo) -> Tuple[int, int, int]:
        tileid = UniqueProcAST.ProcTlieList[0]
        for proctile in self.ProcPartition.TileProcList:
            if proctile.id == tileid:
                x = int(GlobalConfiguration.Grid.NumLon / proctile.ProcLon)
                y = proctile.range[1] - proctile.range[0] + 1
                z = GlobalConfiguration.Grid.NumLev

                return [x, y, z]

    def __init__(
        self,
        UniqueProcTimeOpList: List[UniqueProcASTInfo],
        ProcPartition: PartitionConfiguration,
    ):
        self.UniqueProcTimeOpList = UniqueProcTimeOpList
        self.ProcPartition = ProcPartition

    def SWOpt(self):
        for UniqueProcAST in self.UniqueProcTimeOpList:
            procdomain = self.ProcTileRange(UniqueProcAST)
            for timeOP in UniqueProcAST.TimeOpList:
                for spaceOP in timeOP:
                    SWOptForTransformerSingle()(
                        spaceOP["op"],
                        procdomain,
                        UniqueProcAST.FieldHaloRange,
                        UniqueProcAST.ProcHaloRange,
                    )
