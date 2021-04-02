from level import Level
from layer import Layer, Shape, LayerType
from colors import Colors
from typing import Dict, Tuple, List
import numpy as np
# from levels import Levels
from random import random, choice


class Player(Layer):
    name = "Player"
    color = Colors.blue
    size = 1
    blocking = True
    shape = Shape.Circle
    type = LayerType.Player

    def step(self, actions, layers):
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
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
        adders = set()
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
            adders.add((pos[0] + action[0], pos[1]))
        rocks = set(self.positions[batch])
        s = board.all_items[batch]
        for rock in rocks:
            x, y = rock[0], rock[1]
            item_under = (x, y + 1)
            if item_under in s:
                if s[item_under] == 0 and item_under not in adders:
                    self.remove(batch, rock)
                    adders.add(item_under)
                elif item_under in rocks:
                    left_side, left_down_side, right_side, right_down_side = (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1)
                    if s[right_side] == 0 and s[right_down_side] == 0 and right_side not in adders and (pos[0], pos[1]) != right_side:
                        self.remove(batch, rock)
                        adders.add(right_side)
                    elif s[left_side] == 0 and s[left_down_side] == 0 and left_side not in adders and (pos[0], pos[1]) != left_side:
                        self.remove(batch, rock)
                        adders.add(left_side)

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


class Diamond1(Layer):
    name = "Diamond1"
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square
    type = LayerType.Diamond1

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Diamond2(Layer):
    name = "Diamond2"
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square
    type = LayerType.Diamond2

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond1 in layersDict and bool(layersDict[LayerType.Diamond1].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Diamond3(Layer):
    name = "Diamond3"
    color = Colors.red
    size = 0.2
    blocking = False
    shape = Shape.Square
    type = LayerType.Diamond3

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond2 in layersDict and bool(layersDict[LayerType.Diamond2].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Diamond4(Layer):
    name = "Diamond4"
    color = Colors.purple
    size = 0.2
    blocking = False
    shape = Shape.Square
    type = LayerType.Diamond4

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond3 in layersDict and bool(layersDict[LayerType.Diamond3].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Redkeys(Layer):
    name = "Redkeys"
    color = Colors.red
    size = 0.4
    blocking = False
    shape = Shape.Circle
    type = LayerType.Redkeys

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
        if pos in layersDict[LayerType.Bluekeys].positions[batch] or pos in layersDict[LayerType.Bluekeys]._removed[batch]:
            while True:
                new_pos = (choice(range(3, board.width - 3)), choice(range(2, board.height - 2)))
                if new_pos not in layersDict[LayerType.Bluekeys].positions[batch] and new_pos not in layersDict[LayerType.Redkeys].positions[batch] and new_pos != pos:
                    break
            self.add(batch, new_pos)


class Reddoor(Layer):
    name = "Reddoor"
    color = Colors.red
    size = 1
    shape = Shape.Square
    type = LayerType.Reddoor

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._blocking: Dict[int, bool] = {}
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self._blocking[batch] = True

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self._blocking[batch] = LayerType.Redkeys in layersDict and bool(layersDict[LayerType.Redkeys].positions[batch])

    def isBlocking(self, batch: int):
        return self._blocking[batch]


class Bluekeys(Layer):
    name = "Bluekeys"
    color = Colors.lightBlue
    size = 0.4
    blocking = False
    shape = Shape.Circle
    type = LayerType.Bluekeys

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
        if pos in layersDict[LayerType.Redkeys].positions[batch] or pos in layersDict[LayerType.Redkeys]._removed[batch]:
            while True:
                new_pos = (choice(range(3, board.width - 3)), choice(range(2, board.height - 2)))
                if new_pos not in layersDict[LayerType.Bluekeys].positions[batch] and new_pos not in layersDict[LayerType.Redkeys].positions[batch] and new_pos != pos:
                    break
            self.add(batch, new_pos)


class Bluedoor(Layer):
    name = "Bluedoor"
    color = Colors.lightBlue
    size = 1
    shape = Shape.Square
    type = LayerType.Bluedoor

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._blocking: Dict[int, bool] = {}
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self._blocking[batch] = True

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self._blocking[batch] = LayerType.Bluekeys in layersDict and bool(layersDict[LayerType.Bluekeys].positions[batch])

    def isBlocking(self, batch: int):
        return self._blocking[batch]


class Layers:
    def __init__(self, batch: int, width: int, height: int, level, reset_chance: float, *layers: Tuple[LayerType]) -> None:
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
        self.levelType: Level = level.value

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
        if LayerType.Bluedoor in layers:
            self.layers.append(Bluedoor(batch, width, height))
            self.dict[LayerType.Bluedoor] = self.layers[-1]
            self.types.append(LayerType.Bluedoor)
            self.names.append(LayerType.Bluedoor.name)
        if LayerType.Reddoor in layers:
            self.layers.append(Reddoor(batch, width, height))
            self.dict[LayerType.Reddoor] = self.layers[-1]
            self.types.append(LayerType.Reddoor)
            self.names.append(LayerType.Reddoor.name)
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
        if LayerType.Diamond1 in layers:
            self.layers.append(Diamond1(batch, width, height))
            self.dict[LayerType.Diamond1] = self.layers[-1]
            self.types.append(LayerType.Diamond1)
            self.names.append(LayerType.Diamond1.name)
        if LayerType.Diamond2 in layers:
            self.layers.append(Diamond2(batch, width, height))
            self.dict[LayerType.Diamond2] = self.layers[-1]
            self.types.append(LayerType.Diamond2)
            self.names.append(LayerType.Diamond2.name)
        if LayerType.Diamond3 in layers:
            self.layers.append(Diamond3(batch, width, height))
            self.dict[LayerType.Diamond3] = self.layers[-1]
            self.types.append(LayerType.Diamond3)
            self.names.append(LayerType.Diamond3.name)
        if LayerType.Diamond4 in layers:
            self.layers.append(Diamond4(batch, width, height))
            self.dict[LayerType.Diamond4] = self.layers[-1]
            self.types.append(LayerType.Diamond4)
            self.names.append(LayerType.Diamond4.name)
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
        if LayerType.Bluekeys in layers:
            self.layers.append(Bluekeys(batch, width, height))
            self.dict[LayerType.Bluekeys] = self.layers[-1]
            self.types.append(LayerType.Bluekeys)
            self.names.append(LayerType.Bluekeys.name)
        if LayerType.Redkeys in layers:
            self.layers.append(Redkeys(batch, width, height))
            self.dict[LayerType.Redkeys] = self.layers[-1]
            self.types.append(LayerType.Redkeys)
            self.names.append(LayerType.Redkeys.name)
        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)
        self.counter = np.zeros(batch)
        self.all_items = [{} for _ in range(self.batch)]

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

        if LayerType.Rock in self.types:
            for layer in self.layers:
                No_change = layer.update(self.board, No_change, self.all_items)
        else:
            for layer in self.layers:
                No_change = layer.NoRock_update(self.board, No_change)

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
        self.level = self.levelType(self.types, (self.width-2, self.height-2)).level
        for layer in self.layers:
            layer.restart(batch, self.level[layer.type], self.all_items)
