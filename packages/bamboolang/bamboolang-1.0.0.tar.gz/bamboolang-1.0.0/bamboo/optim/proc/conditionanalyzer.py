from typing import Any, List, Optional, Tuple, cast, Dict
import copy
from dataclasses import dataclass

from bamboo.optim.proc import UniqueProcASTInfo
from bamboo.optim.proc.partition import (
    ProcessPartition,
    PartitionConfiguration,
    ProcessTile,
)
from bamboo.configuration import GlobalConfiguration as gc


@dataclass
class HaloProcTileInfo:
    def __init__(self, range: Tuple[int, int], hw: Tuple[int, int, int]):
        self.range = range
        self.hw = hw


def LonHaloPreLatCondition(
    Partition: PartitionConfiguration, UniqueProcTimeOpList: List[UniqueProcASTInfo]
) -> List[HaloProcTileInfo]:
    HaloTileList: List[HaloProcTileInfo] = []

    ProcList: List[int] = []

    # 没有外部条件,直接延续现有进程分组和halo宽度
    if gc.LonHaloPreLat == []:
        for UniqueProc in UniqueProcTimeOpList:
            HaloTileList.append(HaloProcTileInfo(UniqueProc.ProcRange, UniqueProc.ProcHaloRange))
    else:
        for UniqueProc in UniqueProcTimeOpList:
            preHalo: int = -1
            preRange: List[int] = [0, 0]
            for procid in UniqueProc.ProcTlieList:
                proc = Partition.TileProcList[procid]
                procHalo = UniqueProc.ProcHaloRange[0]
                for i in range(proc.range[0], proc.range[1] + 1):
                    procHalo = max(procHalo, gc.LonHaloPreLat[i])

                if preHalo == -1:
                    preHalo = procHalo
                    preRange[0] = proc.range[0]
                    preRange[1] = proc.range[1]
                elif preHalo == procHalo:
                    preRange[1] = proc.range[1]
                else:
                    HaloTileList.append(
                        HaloProcTileInfo(
                            (preRange[0], preRange[1]),
                            (
                                preHalo,
                                UniqueProc.ProcHaloRange[1],
                                UniqueProc.ProcHaloRange[2],
                            ),
                        )
                    )
                    preHalo = procHalo
                    preRange[0] = proc.range[0]
                    preRange[1] = proc.range[1]

            print("Update ProcHalo", UniqueProc.ProcHaloRange[0], preHalo)
            UniqueProc.ProcHaloRange[0] = max(UniqueProc.ProcHaloRange[0], preHalo)

            HaloTileList.append(
                HaloProcTileInfo(
                    (preRange[0], preRange[1]),
                    (preHalo, UniqueProc.ProcHaloRange[1], UniqueProc.ProcHaloRange[2]),
                )
            )

    return HaloTileList

    #     for i in range(0,Partition.ProcNum):
    #         ProcList.append(i)
    #     HaloTileList.append(copy.deepcopy(ProcList))
    #     return HaloTileList

    # for i in range(0,len(gc.LonHaloPreLat)):
    #     gc.LonHaloPreLat[i] = max(gc.LonHaloPreLat[i],gc.Grid.ExternHalo[0])

    # preHalo : int = -1
    # for proc in Partition.TileProcList:
    #     prochalo : int = 0
    #     for i in range(proc.range[0],proc.range[1] + 1):
    #         prochalo = max(prochalo,gc.LonHaloPreLat[i])
    #     if preHalo == -1:
    #         preHalo = prochalo
    #         ProcList.append(proc.id)
    #     elif preHalo == prochalo:
    #         ProcList.append(proc.id)
    #     else:
    #         HaloTileList.append(copy.deepcopy(ProcList))
    #         ProcList.clear()
    #         preHalo = prochalo
    #         ProcList.append(proc.id)

    # HaloTileList.append(copy.deepcopy(ProcList))

    return HaloTileList
