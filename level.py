from layer import LayerType
from typing import List, Tuple, Dict, Set
from abc import ABCMeta, abstractclassmethod
from functools import reduce


class Level(metaclass=ABCMeta):
    def __init__(self, uses: List[LayerType], shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> None:
        self.uses: Set[LayerType] = set(uses)
        self.shape: Tuple[int, int] = shape
        self.start: Tuple[int, int] = start
        self.end: Tuple[int, int] = end
        self.level: Dict[LayerType, List[Tuple[int, int]]] = {e: [] for e in LayerType}
        if not self.generate():
            self.level = None

    @staticmethod
    def dist2(pos1: Tuple[int, int], pos2: Tuple[int, int]):
        return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

    @abstractclassmethod
    def generate(self):
        pass

    def inverse(self, s: Set[Tuple[int, int]]):
        for x in range(1, self.shape[0]+1):
            for y in range(1, self.shape[1]+1):
                if (x, y) not in s:
                    yield x, y

    def elementsIn(self, *types):
        return reduce(lambda acc, e: acc + e, [self.level[t] for t in types], [])

    @property
    def notUsed(self):
        return list(self.inverse(self.elementsIn(*LayerType)))
