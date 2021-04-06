import inspect
import sys
from level import Level
from layer import Layer, Shape, LayerType
from colors import Colors
from typing import Dict, Tuple, List
import numpy as np
from random import randint, random, choice


class Player(Layer):
    color = Colors.blue
    size = 1
    blocking = True
    shape = Shape.Circle

    def step(self, actions, layers):
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for batch, action in enumerate(actions):
            for x, y in self.positions[batch]:
                self.move(batch, (x, y), (x + deltas[action][0], y + deltas[action][1]), layers, deltas[action])


class Blocks(Layer):
    color = Colors.gray
    size = 1
    blocking = True
    shape = Shape.Square

    def reset(self, batch: int) -> None:
        for x, y in self.grid():
            if x == 0 or x == self._width-1 or y == 0 or y == self._height-1:
                self.add(batch, (x, y))


class Gold(Layer):
    color = Colors.yellow
    size = 0.6
    blocking = False
    shape = Shape.Circle

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Dirt(Layer):
    color = Colors.brown
    size = 1
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Rock(Layer):
    color = Colors.deepOrange
    size = 0.6
    blocking = True
    shape = Shape.Circle

    def __init__(self, batch: int, width: int, height: int) -> None:
        self.falling = [set() for _ in range(batch)]
        super().__init__(batch, width, height)

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self.falling[batch] = set()
        adders = set()
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
            adders.add((pos[0] + action[0], pos[1]))
        rocks = set(self.positions[batch])
        rocks_n_coconuts = rocks.union(set(layersDict[LayerType.Coconut].positions[batch])) if LayerType.Coconut in layersDict else rocks
        s = board.all_items[batch]
        for rock in rocks:
            x, y = rock[0], rock[1]
            item_under = (x, y + 1)
            if item_under in s:
                if s[item_under] == 0 and item_under not in adders:
                    self.remove(batch, rock)
                    adders.add(item_under)
                    self.falling[batch].add(item_under)
                elif item_under in rocks_n_coconuts:
                    left_side, left_down_side, right_side, right_down_side = (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1)
                    if s[right_side] == 0 and s[right_down_side] == 0 and right_side not in adders and (pos[0], pos[1]) != right_side:
                        self.remove(batch, rock)
                        adders.add(right_side)
                    elif s[left_side] == 0 and s[left_down_side] == 0 and left_side not in adders and (pos[0], pos[1]) != left_side:
                        self.remove(batch, rock)
                        adders.add(left_side)

        [self.add(batch, x) for x in adders]


class Goal(Layer):
    color = Colors.green
    size = 1
    blocking = False
    shape = Shape.Square

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        positions = layersDict[LayerType.Player].positions[batch]
        return not positions or positions[0] in self.positions[batch] or not self.positions[batch]


class Keys(Layer):
    color = Colors.purple
    size = 0.4
    blocking = False
    shape = Shape.Circle

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Door(Layer):
    color = Colors.purple
    size = 1
    shape = Shape.Square

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
    color = Colors.orange.c300
    size = 1
    blocking = False
    shape = Shape.Square


class Putter(Layer):
    color = Colors.orange.c700
    size = 0.4
    blocking = False
    shape = Shape.Square

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
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Diamond2(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond1 in layersDict and bool(layersDict[LayerType.Diamond1].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Diamond3(Layer):
    color = Colors.red
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond2 in layersDict and bool(layersDict[LayerType.Diamond2].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Diamond4(Layer):
    color = Colors.purple
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Diamond3 in layersDict and bool(layersDict[LayerType.Diamond3].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Redkeys(Layer):
    color = Colors.red
    size = 0.4
    blocking = False
    shape = Shape.Circle

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
        if pos in layersDict[LayerType.Bluekeys].positions[batch] or pos in layersDict[LayerType.Bluekeys]._removed[batch]:
            while True:
                new_pos = (choice(range(3, board.width - 3)), choice(range(2, board.height - 2)))
                if LayerType.Rock in layersDict and LayerType.Coconut in layersDict:
                    if board.all_items[batch][new_pos] == 0 and new_pos not in layersDict[LayerType.Rock].falling[batch] and new_pos not in layersDict[LayerType.Coconut].falling[batch]:
                        break
                elif new_pos not in layersDict[LayerType.Bluekeys].positions[batch] and new_pos not in layersDict[LayerType.Redkeys].positions[batch] and new_pos != pos:
                    break
            self.add(batch, new_pos)


class Reddoor(Layer):
    color = Colors.red
    size = 1
    shape = Shape.Square

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
    color = Colors.lightBlue
    size = 0.4
    blocking = False
    shape = Shape.Circle

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
        if pos in layersDict[LayerType.Redkeys].positions[batch] or pos in layersDict[LayerType.Redkeys]._removed[batch]:
            while True:
                new_pos = (choice(range(3, board.width - 3)), choice(range(2, board.height - 2)))
                if LayerType.Rock in layersDict and LayerType.Coconut in layersDict:
                    if board.all_items[batch][new_pos] == 0 and new_pos not in layersDict[LayerType.Rock].falling[batch] and new_pos not in layersDict[LayerType.Coconut].falling[batch]:
                        break
                elif new_pos not in layersDict[LayerType.Bluekeys].positions[batch] and new_pos not in layersDict[LayerType.Redkeys].positions[batch] and new_pos != pos:
                    break
            self.add(batch, new_pos)


class Bluedoor(Layer):
    color = Colors.lightBlue
    size = 1
    shape = Shape.Square

    def __init__(self, batch: int, width: int, height: int) -> None:
        self._blocking: Dict[int, bool] = {}
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self._blocking[batch] = True

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self._blocking[batch] = LayerType.Bluekeys in layersDict and bool(layersDict[LayerType.Bluekeys].positions[batch])

    def isBlocking(self, batch: int):
        return self._blocking[batch]


class Pink1(Layer):
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Pink2(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Pink1 in layersDict and bool(layersDict[LayerType.Pink1].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Pink3(Layer):
    color = Colors.red
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Pink2 in layersDict and bool(layersDict[LayerType.Pink2].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Brown1(Layer):
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Brown2(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Brown1 in layersDict and bool(layersDict[LayerType.Brown1].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)


class Brown3(Layer):
    color = Colors.red
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Brown2 in layersDict and bool(layersDict[LayerType.Brown2].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]


class Greendown(Layer):
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Greenup(Layer):
    color = Colors.green
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch]:
            self.remove(batch, pos)


class Greenstar(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked1 = LayerType.Greendown in layersDict and bool(layersDict[LayerType.Greendown].positions[batch])
        blocked2 = LayerType.Greenup in layersDict and bool(layersDict[LayerType.Greenup].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked1 and not blocked2:
            self.remove(batch, pos)


class Bluestar(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Greenstar in layersDict and bool(layersDict[LayerType.Greenstar].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch] or not (LayerType.Yellowstar in layersDict and bool(layersDict[LayerType.Yellowstar].positions[batch]))


class Yellowstar(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        blocked = LayerType.Greenstar in layersDict and bool(layersDict[LayerType.Greenstar].positions[batch])
        if (pos := layersDict[LayerType.Player].positions[batch][0]) in self.positions[batch] and not blocked:
            self.remove(batch, pos)

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch] or not (LayerType.Bluestar in layersDict and bool(layersDict[LayerType.Bluestar].positions[batch]))


class Coconut(Layer):
    color = Colors.deepOrange
    size = 0.6
    blocking = True
    shape = Shape.Circle
    def __init__(self, batch: int, width: int, height: int) -> None:
        self.falling = [set() for _ in range(batch)]
        super().__init__(batch, width, height)

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        self.falling[batch] = set()
        adders = set()
        pos = layersDict[LayerType.Player].positions[batch][0]
        if pos in self.positions[batch]:
            self.remove(batch, pos)
            adders.add((pos[0] + action[0], pos[1]))
        nuts = set(self.positions[batch])
        s = board.all_items[batch]
        for nut in nuts:
            x, y = nut[0], nut[1]
            item_under = (x, y + 1)
            item_over = (x, y - 1)
            if item_under in s:
                if item_over in layersDict[LayerType.Rock].falling[batch]:
                    self.remove(batch, nut)
                    layersDict[LayerType.Gold].add(batch, nut)
                elif s[item_under] == 0 and item_under not in adders:
                    self.remove(batch, nut)
                    adders.add(item_under)
                    self.falling[batch].add(item_under)
                elif item_under in nuts:
                    left_side, left_down_side, right_side, right_down_side = (x + 1, y), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1)
                    if s[right_side] == 0 and s[right_down_side] == 0 and right_side not in adders and (pos[0], pos[1]) != right_side:
                        self.remove(batch, nut)
                        adders.add(right_side)
                    elif s[left_side] == 0 and s[left_down_side] == 0 and left_side not in adders and (pos[0], pos[1]) != left_side:
                        self.remove(batch, nut)
                        adders.add(left_side)
        [self.add(batch, x) for x in adders]

    def isDone(self, batch: int, layersDict: Dict[LayerType, Layer]) -> bool:
        return not self.positions[batch]

    def isDead(self, batch: int, layersDict, board) -> bool:
        # highest = 100
        # for rock in layersDict[LayerType.Rock].positions[batch]:
        #     if rock[0] > 1 and rock[0] < board.shape[3] - 2:
        #         if rock[1] < highest:
        #             highest = rock[1]
        # for nut in set(self.positions[batch]):
        #     if nut[1] <= highest:
        #         return True
        return False

class Monster(Layer):
    color = Colors.blue
    size = 0.2
    blocking = False
    shape = Shape.Square

    def __init__(self, batch: int, width: int, height: int) -> None:
        self.moving = [{} for _ in range(batch)]
        for dict in self.moving:
            for j in width:
                for i in height:
                    dict[(i, j)] = 0

        super().__init__(batch, width, height)

    def check(self, batch: int, layersDict: Dict[LayerType, Layer], action, board) -> None:
        for monster in self.positions[batch]:
            x, y = monster
            right = (x+1, y)
            left = (x-1, y)
            up = (x, y+1)
            down = (x, y-1)
            if self.moving[batch][monster] == 0:
                self.moving[batch][monster] = randint(0,3)
            if self.moving[batch][monster] == 1 and (board.all_items[batch][right] == 0 or right in layersDict[LayerType.Player].positions[batch][0]):
                self.remove(batch, monster)
                self.add(batch, right)    
            elif self.moving[batch][monster] == 2 and (board.all_items[batch][left] == 0 or left in layersDict[LayerType.Player].positions[batch][0]):
                self.remove(batch, monster)
                self.add(batch, left)   
            elif self.moving[batch][monster] == 3 and (board.all_items[batch][up] == 0 or up in layersDict[LayerType.Player].positions[batch][0]):
                self.remove(batch, monster)
                self.add(batch, up)   
            elif self.moving[batch][monster] == 4 and (board.all_items[batch][down] == 0 or down in layersDict[LayerType.Player].positions[batch][0]):
                self.remove(batch, monster)
                self.add(batch, down)    
            else: 
                self.moving[batch][monster] = 0

    def isDead(self, batch: int, layersDict, board) -> bool:
        if layersDict[LayerType.Player].positions[batch][0] in self.positions[batch]:
            return True
        return False

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
        self.levelType: Level = level.value
        abovePlayer = {LayerType.Putter}

        for layer in [layer for layer in layers if layer not in abovePlayer]:
            self.add(layer, layers)

        self.layers.append(self.player)

        for layer in [layer for layer in layers if layer in abovePlayer]:
            self.add(layer, layers)

        for i, layer in enumerate(self.layers):
            if layer.type == LayerType.Rock:
                self.Rocks_idx = i

        self.board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)
        self.counter = np.zeros(batch)
        self.all_items = [{} for _ in range(self.batch)]

    def add(self, layerType: LayerType, layers: Tuple[LayerType]):
        if layerType in layers:
            for _, Class in inspect.getmembers(sys.modules[__name__], inspect.isclass):
                if Layer in inspect.getmro(Class) and Class.__name__ == layerType.name:
                    self.layers.append(Class(self.batch, self.width, self.height))
                    self.dict[layerType] = self.layers[-1]
                    self.types.append(layerType)

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
            elif random() < self.reset_chance or self.frames_since_chance[batch] > 10 or any(layer.isDead(batch, self.dict, self.board) for layer in self.layers):
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
