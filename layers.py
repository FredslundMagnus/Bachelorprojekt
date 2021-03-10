from layer import Layer, Shape, LayerType
from colors import Colors
from typing import Dict, Tuple, List
import numpy as np
from torch import Tensor
from levels import Maze, Rocks
from random import random
from copy import copy


class Player(Layer):
    name = "Player"
    color = Colors.blue
    size = 1
    blocking = True
    shape = Shape.Circle
    type = LayerType.Player

    def step(self, actions, layers):
        deltas = [(1,0), (0,1), (-1,0), (0,-1)]
        for batch, action in enumerate(actions):
            for x, y in self.positions[batch]:
                self.move(batch, (x, y), (x + deltas[action][0], y + deltas[action][1]), layers, deltas[action])



class Blocks(Layer):
    name = "Block"
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
    name = "Gold"
    color = Colors.yellow
    size = 0.6
    blocking = False
    shape = Shape.Circle
    type = LayerType.Gold

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]

class Dirt(Layer):
    name = "Dirt"
    color = Colors.brown
    size = 1
    blocking = False
    shape = Shape.Square
    type = LayerType.Dirt

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)

class Rock(Layer):
    name = "Rock"
    color = Colors.deepOrange
    size = 0.6
    blocking = True
    shape = Shape.Circle
    type = LayerType.Rock

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        adders = []
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
            adders.append((pos[0] + action[0], pos[1]))
        rocks = copy(self.positions[batch])
        for rock in rocks:
            item_under = (rock[0], rock[1] + 1)
            if rock in layersDict[LayerType.Dirt].positions[batch] or item_under in layersDict[LayerType.Blocks].positions[batch]:
                pass
            elif all(item_under not in layer.positions[batch] for _, layer in layersDict.items()) and item_under not in adders:
                self.remove(batch, rock)
                adders.append(item_under)
            elif item_under in layersDict[LayerType.Rock].positions[batch]:
                left_side = (rock[0] + 1, rock[1])
                left_down_side = (rock[0] + 1, rock[1] + 1)
                right_side = (rock[0] - 1, rock[1])
                right_down_side = (rock[0] - 1, rock[1] + 1)
                if all(right_side not in layer.positions[batch] for _, layer in layersDict.items()) and all(right_down_side not in layer.positions[batch] for _, layer in layersDict.items()) and right_side not in adders and pos != right_side:
                    self.remove(batch, rock)
                    adders.append(right_side)
                elif all(left_side not in layer.positions[batch] for _, layer in layersDict.items()) and all(left_down_side not in layer.positions[batch] for _, layer in layersDict.items()) and left_side not in adders and pos != left_side:
                    self.remove(batch, rock)
                    adders.append(left_side)         

        [self.add(batch, x) for x in adders]

class Goal(Layer):
    name = "Goal"
    color = Colors.green
    size = 1
    blocking = False
    shape = Shape.Square
    type = LayerType.Goal

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        positions = layersDict[LayerType.Player].positions[batch]
        return not positions or positions[0] in self.positions[batch] or not self.positions[batch]


class Keys(Layer):
    name = "Keys"
    color = Colors.purple
    size = 0.4
    blocking = False
    shape = Shape.Circle
    type = LayerType.Keys

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Door(Layer):
    name = "Door"
    color = Colors.purple
    size = 1
    shape = Shape.Square
    type = LayerType.Door

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._blocking: Dict[int, bool] = {}
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self._blocking[batch] = True

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self._blocking[batch] = LayerType.Keys in layersDict and bool(layersDict[LayerType.Keys].positions[batch])

    def isBlocking(self, batch: int):
        return self._blocking[batch]


class Holder(Layer):
    name = "Holder"
    color = Colors.orange.c300
    size = 1
    blocking = False
    shape = Shape.Square
    type = LayerType.Holder


class Putter(Layer):
    name = "Putter"
    color = Colors.orange.c700
    size = 0.4
    blocking = False
    shape = Shape.Square
    type = LayerType.Putter

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._carried: Dict[int, bool] = {}
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self._carried[batch] = False

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        positions = layersDict[LayerType.Player].positions[batch]
        if positions and self._carried[batch]:
            self.remove(batch, self.positions[batch][0])
            self.add(batch, positions[0])

        if positions and positions[0] in self.positions[batch]:
            self._carried[batch] = True
        if LayerType.Holder in layersDict:
            positions = layersDict[LayerType.Holder].positions[batch]
            if positions and positions[0] in self.positions[batch]:
                self._carried[batch] = False

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        if LayerType.Holder not in layersDict:
            return True
        positions = layersDict[LayerType.Holder].positions[batch]
        if not positions or not self.positions[batch]:
            return True
        return positions[0] == self.positions[batch][0]


class Layers:
    def __init__(self, batch: int, width: int, height: int, reset_chance: float, *layers: Tuple[LayerType]) -> None:
        self.frames_since_chance = [0] * batch
        self.layers: List[Layer] = []
        self.player: Player = Player(batch, width, height)
        self.width: int = width
        self.height: int = height
        self.batch: int = batch
        self.reset_chance = reset_chance
        self.types: List[LayerType] = []
        self.dict: Dict[LayerType, Layer] = {LayerType.Player: self.player}
        self.types.append(LayerType.Player)
        self.names: List[str] = []

        if LayerType.Blocks in layers:
            self.layers.append(Blocks(batch, width, height))
            self.dict[LayerType.Blocks] = self.layers[-1]
            self.types.append(LayerType.Blocks)
            self.names.append(LayerType.Blocks.name)
        if LayerType.Goal in layers:
            self.layers.append(Goal(batch, width, height))
            self.dict[LayerType.Goal] = self.layers[-1]
            self.types.append(LayerType.Goal)
            self.names.append(LayerType.Goal.name)
        if LayerType.Door in layers:
            self.layers.append(Door(batch, width, height))
            self.dict[LayerType.Door] = self.layers[-1]
            self.types.append(LayerType.Door)
            self.names.append(LayerType.Door.name)
        if LayerType.Keys in layers:
            self.layers.append(Keys(batch, width, height))
            self.dict[LayerType.Keys] = self.layers[-1]
            self.types.append(LayerType.Keys)
            self.names.append(LayerType.Keys.name)
        if LayerType.Gold in layers:
            self.layers.append(Gold(batch, width, height))
            self.dict[LayerType.Gold] = self.layers[-1]
            self.types.append(LayerType.Gold)
            self.names.append(LayerType.Gold.name)
        if LayerType.Holder in layers:
            self.layers.append(Holder(batch, width, height))
            self.dict[LayerType.Holder] = self.layers[-1]
            self.types.append(LayerType.Holder)
            self.names.append(LayerType.Holder.name)
        self.layers.append(self.player)
        if LayerType.Putter in layers:
            self.layers.append(Putter(batch, width, height))
            self.dict[LayerType.Putter] = self.layers[-1]
            self.types.append(LayerType.Putter)
            self.names.append(LayerType.Putter.name)
        if LayerType.Rock in layers:
            self.layers.append(Rock(batch, width, height))
            self.dict[LayerType.Rock] = self.layers[-1]
            self.types.append(LayerType.Rock)
            self.names.append(LayerType.Rock.name)
            for i in range(len(self.layers)):
                if self.layers[i].name == "Rock":
                    self.Rocks_idx = i
        if LayerType.Dirt in layers:
            self.layers.append(Dirt(batch, width, height))
            self.dict[LayerType.Dirt] = self.layers[-1]
            self.types.append(LayerType.Dirt)
            self.names.append(LayerType.Dirt.name)
        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)
        self.counter = np.zeros(batch)

    def __len__(self) -> int:
        return len(self.layers)

    def update(self):
        self.counter += 1
        self.frames_since_chance = [x+1 for x in self.frames_since_chance]
        rewards = [0.0 for _ in range(self.batch)]
        dones = [0 for _ in range(self.batch)]
        for batch in range(self.batch):
            if all(layer.isDone(batch, self.dict) for layer in self.layers):
                self.restart(batch)
                rewards[batch] = 1
                dones[batch] = 1
                self.counter[batch] = 0
            elif random() < self.reset_chance or self.frames_since_chance[batch] > 10:
                self.restart(batch)
                rewards[batch] = 0
                dones[batch] = 1
                self.counter[batch] = 0

        No_change = [1 for _ in range(self.batch)]
        for layer in self.layers:
            No_change = layer.update(self.board, No_change)
        self.frames_since_chance = [c*a for c, a in zip(self.frames_since_chance, No_change)]
        return rewards, dones

    def step(self, action: List[int]) -> Tuple[List[float], List[int], List[dict]]:
        self.info = [{} for _ in range(self.batch)]
        self.player.step(action, self)
        rewards, dones = self.update()
        return rewards, dones, self.info

    def getColorable(self, dim: int):
        for layer in self.layers:
            for x, y in layer.positions[dim]:
                yield layer.shape, layer.color, layer.size, x, y, layer.__class__.__name__

    def isFree(self, batch: int, pos: Tuple[int, int]):
        for layer in self.layers:
            if not layer.isFree(batch, pos):
                return False
        return True

    def check(self, batch: int, action, board):
        for layer in self.layers:
            layer.check(batch, self.dict, action, board)
        

    def restart(self, batch: int):
        if (x := self.dict[LayerType.Player].positions[batch]):
            self.info[batch]['player_end'] = x[0]
        self.level = Rocks(self.types, (self.width-2, self.height-2)).level
        for layer in self.layers:
            layer.restart(batch, self.level[layer.type])
