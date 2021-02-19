from layer import Layer
from colors import Colors
from typing import Tuple, List
from enum import Enum
import numpy as np
from torch import Tensor


class Player(Layer):
    color = Colors.green
    size = 1

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (2, 3))


class Blocks(Layer):
    color = Colors.gray
    size = 1

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        for x, y in self.grid():
            if x == 0 or x == self._width-1 or y == 0 or y == self._height-1:
                self.add(batch, (x, y))


class Gold(Layer):
    color = Colors.yellow
    size = 0.6

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (4, 5))


class LayerType(Enum):
    Player = 0
    Blocks = 1
    Gold = 2


class Layers:
    def __init__(self, batch: int, width: int, height: int, *layers: Tuple[LayerType]) -> None:
        self.layers: List[Layer] = [Player(batch, width, height)]
        self.width: int = width
        self.height: int = height
        self.batch: int = batch
        if LayerType.Blocks in layers:
            self.layers.append(Blocks(batch, width, height))
        if LayerType.Gold in layers:
            self.layers.append(Gold(batch, width, height))
        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)

    def update(self):
        for layer in self.layers:
            layer.update(self.board)

    def step(self, action: List[int]) -> Tuple[Tensor, List[float], List[int], List[dict]]:
        pass

    def getColorable(self):
        for layer in self.layers:
            for x, y in layer.positions[0]:
                yield layer.color, layer.size, x, y
