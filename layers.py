from layer import Layer, Shape, LayerType
from colors import Colors
from typing import Dict, Tuple, List
import numpy as np
from torch import Tensor
from levels import Maze


class Player(Layer):
    color = Colors.blue
    size = 1
    blocking = True
    shape = Shape.Circle
    type = LayerType.Player

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


class Blocks(Layer):
    color = Colors.gray
    size = 1
    blocking = True
    shape = Shape.Square
    type = LayerType.Blocks

    def reset(self, batch: int) -> None:
        for x, y in self.grid():
            if x == 0 or x == self._width-1 or y == 0 or y == self._height-1:
                self.add(batch, (x, y))


class Gold(Layer):
    color = Colors.yellow
    size = 0.6
    blocking = False
    shape = Shape.Circle
    type = LayerType.Gold

    def check(self, batch: int, layersDict: Dict[LayerType, Layer]) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Goal(Layer):
    color = Colors.green
    size = 1
    blocking = False
    shape = Shape.Square
    type = LayerType.Goal

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        positions = layersDict[LayerType.Player].positions[batch]
        return not positions or positions[0] in self.positions[batch] or not self.positions[batch]


class Keys(Layer):
    color = Colors.purple
    size = 0.4
    blocking = False
    shape = Shape.Circle
    type = LayerType.Keys

    def check(self, batch: int, layersDict: Dict[LayerType, Layer]) -> None:
        score = 0
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)
            score = 1
        if len(self.positions[batch]) == 0:
            door = layersDict[LayerType.Door]
            for pos in door.positions[batch]:
                door.remove(batch, pos)
        return score


class Door(Layer):
    color = Colors.purple
    size = 1
    blocking = True
    shape = Shape.Square
    type = LayerType.Door


class Layers:
    def __init__(self, batch: int, width: int, height: int, *layers: Tuple[LayerType]) -> None:
        self.layers: List[Layer] = []
        self.player: Player = Player(batch, width, height)
        self.width: int = width
        self.height: int = height
        self.batch: int = batch
        self.types: List[LayerType] = []
        self.dict: Dict[LayerType, Layer] = {LayerType.Player: self.player}
        self.types.append(LayerType.Player)
        if LayerType.Blocks in layers:
            self.layers.append(Blocks(batch, width, height))
            self.dict[LayerType.Blocks] = self.layers[-1]
            self.types.append(LayerType.Blocks)
        if LayerType.Goal in layers:
            self.layers.append(Goal(batch, width, height))
            self.dict[LayerType.Goal] = self.layers[-1]
            self.types.append(LayerType.Goal)
        if LayerType.Door in layers:
            self.layers.append(Door(batch, width, height))
            self.dict[LayerType.Door] = self.layers[-1]
            self.types.append(LayerType.Door)
        if LayerType.Keys in layers:
            self.layers.append(Keys(batch, width, height))
            self.dict[LayerType.Keys] = self.layers[-1]
            self.types.append(LayerType.Keys)
        if LayerType.Gold in layers:
            self.layers.append(Gold(batch, width, height))
            self.dict[LayerType.Gold] = self.layers[-1]
            self.types.append(LayerType.Gold)
        self.layers.append(self.player)
        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)

    def __len__(self) -> int:
        return len(self.layers)

    def update(self):
        for batch in range(self.batch):
            if all(layer.isDone(batch, self.dict) for layer in self.layers):
                self.restart(batch)

        for layer in self.layers:
            layer.update(self.board)

    def step(self, action: List[int]) -> Tuple[Tensor, List[float], List[int], List[dict]]:
        self.player.step(action, self)
        self.update()

    def getColorable(self):
        for layer in self.layers:
            for x, y in layer.positions[0]:
                yield layer.shape, layer.color, layer.size, x, y

    def isFree(self, batch: int, pos: Tuple[int, int]):
        for layer in self.layers:
            if not layer.isFree(batch, pos):
                return False
        return True

    def check(self, batch: int):
        for layer in self.layers:
            layer.check(batch, self.dict)

    def restart(self, batch: int):
        level = Maze(self.types, (self.width-2, self.height-2), (1, 1), (self.width-2, self.height-2)).level
        for layer in self.layers:
            layer.restart(batch, level[layer.type])
