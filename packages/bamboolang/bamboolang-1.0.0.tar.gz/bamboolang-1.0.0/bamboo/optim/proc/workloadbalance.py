from dataclasses import dataclass
from typing import Dict, List, cast, Tuple
import math


@dataclass
class PartitionInfo:
    def __init__(
        self,
        region: int,
        regionWidth: List[int],
        regionProc: List[int],
        regionPx: List[int],
        regionPy: List[int],
        error: str,
    ):
        self.region = region
        self.regionWidth = regionWidth
        self.regionProc = regionProc
        self.regionPx = regionPx
        self.regionPy = regionPy
        self.error = error


def initialPartition(nx: int, ny: int, proc: int, maxx: int, maxy: int) -> (int, int):
    for x in range(1, math.ceil(math.sqrt(proc))):
        if proc % x == 0:
            px = x
            py = int(proc / x)
            if py <= maxy and px <= maxx and ny % py == 0 and nx % px == 0:
                return px, py

    return -1, -1


# 是否均衡;不均衡时,过大=True,过小=False
def checkblance(
    ny: int, ny_cur: int, py_cur: int, workload: List[int], avg: float, threshold: float
) -> (bool, bool):
    sum = 0
    p = 0
    nyproc = ny_cur / py_cur
    for i in range(ny - ny_cur, ny):
        sum = sum + workload[i]
        p += 1
        if p == nyproc:
            if sum > avg * (1 + threshold):
                return False, True
            if sum < avg * (1 - threshold):
                return False, False
            sum = 0
            p = 0

    return True, None


# 总大小,进程数,负载
def balance(
    nx: int,
    ny: int,
    proc: int,
    workload: List[int],
    minRegion: List[int],
    threshold: float,
) -> PartitionInfo:
    balancePartition = PartitionInfo(0, [], [], [], [], "None")

    # 根据最小进程区域现在,设置各维度最大划分
    maxpx = 0
    maxpy = 0
    if minRegion[0] != -1:
        maxpx = nx / minRegion[0]
    else:
        maxpx = proc + 1
    if minRegion[1] != -1:
        maxpy = ny / minRegion[1]
    else:
        maxpy = proc + 1

    if maxpx * maxpy < proc:
        balancePartition.error = "Proc To Big"
        return balancePartition

    nx_cur = nx
    ny_cur = ny
    px_cur, py_cur = initialPartition(nx_cur, ny_cur, proc, maxpx, maxpy)

    sum = 0
    for load in workload:
        sum += load
    avg = sum / ny

    while checkblance(ny, ny_cur, py_cur, workload, avg, threshold) == False:
        pass

    balancePartition.region += 1
    balancePartition.regionWidth.append(ny_cur)
    balancePartition.regionProc.append(px_cur * py_cur)
    balancePartition.regionPx.append(px_cur)
    balancePartition.regionPy.append(py_cur)

    print(px_cur, py_cur)

    return balancePartition


workload: List[int] = []

for i in range(0, 180):
    workload.append(1)

bestPartition = balance(360, 180, 20, workload, [-1, 3], 0.05)
