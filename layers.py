from layer import Layer
from colors import Colors
from typing import Tuple, List
from enum import Enum
import numpy as np
from torch import Tensor


class Player(Layer):
    color = Colors.green
    size = 1
    blocking = True

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (2, 3))

    def step(self, actions, layers):
        for batch, action in enumerate(actions):
            for x, y in self.positions[batch]:
                if action == 0:
                    self.move(batch, (x, y), (x+1, y), layers)
                elif action == 1:
                    self.move(batch, (x, y), (x, y+1), layers)
                elif action == 2:
                    self.move(batch, (x, y), (x-1, y), layers)
                elif action == 3:
                    self.move(batch, (x, y), (x, y-1), layers)

    def isDone(self, batch: int) -> bool:
        return True


class Blocks(Layer):
    color = Colors.gray
    size = 1
    blocking = True

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        for x, y in self.grid():
            if x == 0 or x == self._width-1 or y == 0 or y == self._height-1:
                self.add(batch, (x, y))

    def isDone(self, batch: int) -> bool:
        return True


class Gold(Layer):
    color = Colors.yellow
    size = 0.6
    blocking = False

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (4, 5))
        self.add(batch, (3, 2))
        self.add(batch, (7, 3))

    def check(self, batch: int, pos: Tuple[int, int]) -> float:
        if pos in self.positions[batch]:
            self.remove(batch, pos)
            return 1

    def isDone(self, batch: int) -> bool:
        return len(self.positions[batch]) == 0


class LayerType(Enum):
    Player = 0
    Blocks = 1
    Gold = 2


class Layers:
    def __init__(self, batch: int, width: int, height: int, *layers: Tuple[LayerType]) -> None:
        self.layers: List[Layer] = [Player(batch, width, height)]
        self.player: Player = self.layers[0]
        self.width: int = width
        self.height: int = height
        self.batch: int = batch
        if LayerType.Blocks in layers:
            self.layers.append(Blocks(batch, width, height))
        if LayerType.Gold in layers:
            self.layers.append(Gold(batch, width, height))
        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)

    def update(self):
        for batch in range(self.batch):
            if all(layer.isDone(batch) for layer in self.layers):
                self.restart(batch)

        for layer in self.layers:
            layer.update(self.board)

    def step(self, action: List[int]) -> Tuple[Tensor, List[float], List[int], List[dict]]:
        self.player.step(action, self)
        self.update()

    def getColorable(self):
        for layer in self.layers:
            for x, y in layer.positions[0]:
                yield layer.color, layer.size, x, y

    def isFree(self, batch: int, pos: Tuple[int, int]):
        for layer in self.layers:
            if not layer.isFree(batch, pos):
                return False
        return True

    def check(self, batch: int):
        for pos in self.player.positions[batch]:
            for layer in self.layers:
                layer.check(batch, pos)

    def restart(self, batch: int):
        for layer in self.layers:
            layer.restart(batch)
