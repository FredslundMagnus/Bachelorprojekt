from abc import ABCMeta, abstractproperty
from typing import Iterable, List, Tuple
from colors import Color
from enum import Enum
import numpy as np
from copy import copy


class LayerType(Enum):
    Player = 0
    Blocks = 1
    Gold = 2
    Goal = 3
    Keys = 4
    Door = 5
    Holder = 6
    Putter = 7
    Dirt = 8
    Rock = 9
    Diamond1 = 10
    Diamond2 = 11
    Diamond3 = 12
    Diamond4 = 13


class Shape(Enum):
    Square = 0
    Circle = 1


class Layer(metaclass=ABCMeta):
    __layer__ = 0

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._batch = batch
        self._width = width
        self._height = height
        self._positions: List[List[Tuple[int, int]]] = [[] for _ in range(batch)]
        self._removed: List[List[Tuple[int, int]]] = [[] for _ in range(batch)]
        self._added: List[List[Tuple[int, int]]] = [[] for _ in range(batch)]
        self._layer = Layer.__layer__
        self._grid = set(self.grid())
        Layer.__layer__ += 1
        for i in range(batch):
            self.clear(i)
            self.reset(i)

    def restart(self, batch: int, positions: List[Tuple[int, int]], all_items) -> None:
        self.clear2(batch, all_items)
        for pos in positions:
            self.add(batch, pos)
        self.reset(batch)

    def reset(self, batch: int) -> None:
        pass

    def check(self, batch: int, layersDict, action, board) -> None:
        pass

    def isDone(self, batch: int, layersDict) -> bool:
        return True

    @property
    def layer(self) -> int:
        return self._layer

    @property
    def positions(self) -> List[List[Tuple[int, int]]]:
        return self._positions

    def isFree(self, batch: int, pos: Tuple[int, int]) -> bool:
        return not self.isBlocking(batch) or pos not in self.positions[batch]

    def move(self, batch: int, _from: Tuple[int, int], _to: Tuple[int, int], layers, action):
        if _to in self._grid and layers.isFree(batch, _to):
            if "Rock" not in layers.names:
                self.remove(batch, _from)
                self.add(batch, _to)
            elif layers.all_items[batch][_to] == 1:
                self.remove(batch, _from)
                self.add(batch, _to)
            elif (_to[0], _to[1] - 1) not in layers.dict[LayerType.Rock].positions[batch]:
                self.remove(batch, _from)
                self.add(batch, _to)
        elif "Rock" in layers.names and action[1] == 0:
            if _to in layers.dict[LayerType.Rock].positions[batch] and _to[0] < layers.width - 1 and _to[0] > 0:
                push_to = (_to[0] + action[0], _to[1])
                fall_to = (_to[0], _to[1] + 1)
                if layers.all_items[batch][push_to] == 0 and layers.all_items[batch][fall_to] != 0:
                    self.remove(batch, _from)
                    self.add(batch, _to)
        layers.check(batch, action, layers)

    def remove(self, batch: int, _pos: Tuple[int, int]):
        self._positions[batch].remove(_pos)
        self._removed[batch].append(_pos)

    def add(self, batch: int, _pos: Tuple[int, int]):
        self._positions[batch].append(_pos)
        self._added[batch].append(_pos)

    def clear(self, batch: int):
        self._removed[batch] += self._positions[batch]
        self._positions[batch] = []
        self._added[batch] = []

    def clear2(self, batch: int, all_items):
        self._removed[batch] += self._positions[batch]
        self._positions[batch] = []
        for item in self._added[batch]:
            all_items[batch][item] += 1
        self._added[batch] = []

    def elements(self, li: List[List[Tuple[int, int]]]):
        for batch, pos in enumerate(li):
            for x, y in pos:
                yield batch, x, y

    def update(self, board, No_change, all_items) -> None:
        for batch in range(len(No_change)):
            if No_change[batch] == 1 and len(self._removed[batch]) != 0:
                No_change[batch] = 0

        for batch, x, y in self.elements(self._removed):
            board[batch, self._layer, y, x] = 0
            all_items[batch][(x, y)] -= 1

        for batch, x, y in self.elements(self._added):
            board[batch, self._layer, y, x] = 1
            all_items[batch][(x, y)] += 1
        self._removed = [[] for _ in range(self._batch)]
        self._added = [[] for _ in range(self._batch)]
        return No_change

    def NoRock_update(self, board, No_change) -> None:
        for batch in range(len(No_change)):
            if No_change[batch] == 1 and len(self._removed[batch]) != 0:
                No_change[batch] = 0

        for batch, x, y in self.elements(self._removed):
            board[batch, self._layer, y, x] = 0

        for batch, x, y in self.elements(self._added):
            board[batch, self._layer, y, x] = 1

        self._removed = [[] for _ in range(self._batch)]
        self._added = [[] for _ in range(self._batch)]
        return No_change

    def grid(self) -> Iterable[Tuple[int, int]]:
        for x in range(self._width):
            for y in range(self._height):
                yield x, y

    @abstractproperty
    def color(self) -> Color:
        pass

    @abstractproperty
    def size(self) -> float:
        pass

    @abstractproperty
    def shape(self) -> Shape:
        pass

    @abstractproperty
    def type(self) -> LayerType:
        pass

    @property
    def blocking(self) -> bool:
        pass

    def isBlocking(self, batch: int) -> bool:
        return self.blocking
