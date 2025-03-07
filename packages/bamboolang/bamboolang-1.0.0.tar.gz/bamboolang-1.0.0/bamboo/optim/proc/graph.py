import math
from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Edge:
    def __init__(self, tail: int, next: int):
        self.tail = tail
        self.next = next


class FieldGraph:
    FirstEdge: List[int]
    EageList: List[Edge]

    def __init__(self):
        self.FirstEdge = []
        self.EageList = []
