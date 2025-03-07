import math
from dataclasses import dataclass
from typing import List, Optional, Tuple
from bamboo.configuration import GlobalConfiguration as gc


# 描述进程划分后同一纬度带下的同行进程(因特殊计算只与纬度有关，带内划分的不同经度进程可统一分析)
@dataclass
class ProcessTile:
    # id 按从南到北的顺序; range纬度范围,闭区间; ProcLon:带内进程数;
    def __init__(self, id: int, range: Tuple[int, int], ProcLon: int):
        self.id = id
        self.range = range
        self.ProcLon = ProcLon

    def __str__(self) -> str:
        return f"[ ProcTileId = {self.id}, range = {self.range}, ProcLon = {self.ProcLon} ]"


# 描述整体进程划分
@dataclass
class PartitionConfiguration:
    def __init__(self, ProcNum: int):
        self.ProcNum = ProcNum
        self.TileLatNum: List[int] = []
        self.TileProcLon: List[int] = []
        self.TileProcLat: List[int] = []
        self.TileWorkLoad: List[int] = []
        self.TileProcList: List[ProcessTile] = []

    def __str__(self) -> str:
        s = f"ProcNum = {self.ProcNum}, LatNum = {self.TileLatNum}, ProcLon = {self.TileProcLon}, ProcLat = {self.TileProcLat}, ProcList = ["
        for id, tile in enumerate(self.TileProcList):
            if id:
                s = s + ", "
            s = s + str(tile)

        s += "]"
        return s


# 进程划分功能模块
# 可从初始状态，按规则划分返回一个基础划分
# 亦可接收某种划分状态和其负载情况，返回一个调整负载后的进阶划分
class ProcessPartition:
    Partition: PartitionConfiguration

    def Gen1dPartition(self) -> None:
        self.Partition.TileLatNum.append(gc.Grid.NumLat)
        self.Partition.TileProcLat.append(self.Partition.ProcNum)
        self.Partition.TileProcLon.append(1)

    def Gen2dPartition(self) -> None:
        ProcNum = gc.ProcNum
        Divisor: List[Tuple[int, int]] = []
        while True:
            for x in range(2, int(math.sqrt(ProcNum))):
                if ProcNum % x == 0:
                    Divisor.append((int(ProcNum / x), x))

            if len(Divisor):
                break

            ProcNum -= 1

        # 更贴近gmcore场景，目前直接选择纬向划分最少的方式
        self.Partition.TileLatNum.append(gc.Grid.NumLat)
        self.Partition.TileProcLat.append(Divisor[0][0])
        self.Partition.TileProcLon.append(Divisor[0][1])

    def GenSquarePartition(self) -> None:
        ProcNum = gc.ProcNum / 6
        self.Partition.TileLatNum.append(gc.Grid.NumLat)
        proc = int(math.sqrt(ProcNum))
        self.Partition.TileProcLat.append(proc)
        self.Partition.TileProcLon.append(proc)

    def ModifyTileProcList(self) -> None:
        LatOffset: int = 0
        self.Partition.TileProcList = []

        for Tileid in range(0, len(self.Partition.TileLatNum)):
            LatNum = self.Partition.TileLatNum[Tileid]
            ProcLat = self.Partition.TileProcLat[Tileid]
            ProcLon = self.Partition.TileProcLon[Tileid]

            for procid in range(0, ProcLat):
                TileLen = int(LatNum / (ProcLat - procid))
                if LatNum % (ProcLat - procid):
                    TileLen += 1

                Tile = ProcessTile(
                    len(self.Partition.TileProcList),
                    (LatOffset, LatOffset + TileLen - 1),
                    ProcLon,
                )
                self.Partition.TileProcList.append(Tile)
                LatNum -= TileLen
                LatOffset += TileLen

    def DoPartition(self, GlobalParaZone: List[bool], Action: str) -> None:
        # 考虑并行域
        if gc.Grid.GridType == "LonLat":
            if Action == "Init":
                self.Gen1dPartition()
            elif Action == "Better":
                pass
            else:
                print("DoPartition Wrong Action")
                exit()
        elif gc.Grid.GridType == "CubedSphere":
            self.GenSquarePartition()
        else:
            print("DoPartition Wrong GridType")
            exit()

        self.ModifyTileProcList()

    def __call__(
        self,
        GlobalParaZone: List[bool],
        CurPartition: Optional[PartitionConfiguration] = None,
    ) -> PartitionConfiguration:
        if CurPartition is None:
            # 无现有划分，开始默认划分
            self.Partition = PartitionConfiguration(gc.ProcNum)
            Action = "Init"
        else:
            # 已有划分，根据负载情况开始优化
            self.Partition = CurPartition
            Action = "Better"
            pass

        self.DoPartition(GlobalParaZone, Action)

        return self.Partition
