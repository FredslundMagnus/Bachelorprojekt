from level import Level
from layers import LayerType
from typing import List, Tuple, Set
from random import choice, sample, random
from enum import Enum


class Maze(Level):
    def generate(self):
        xs = [i for i in range(1, self.shape[0]+1) if i % 2 == 1]
        ys = [i for i in range(1, self.shape[1]+1) if i % 2 == 1]
        if self.shape[0] % 2 == 0:
            xs[-1] += 1
        if self.shape[1] % 2 == 0:
            ys[-1] += 1
        self.nodes: Set[Tuple[int, int]] = set([(x, y) for x in xs for y in ys])
        if self.start == None and self.end == None:
            self.start, self.end = tuple(sample(list(self.nodes), 2))
        elif self.start == None:
            self.start = choice([node for node in self.nodes if node != self.end])
        elif self.end == None:
            self.end = choice([node for node in self.nodes if node != self.start])

        if self.start not in self.nodes or self.end not in self.nodes:
            return False
        self.lines: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        self.order: List[Tuple[int, int]] = []
        self.RFS(self.start)
        self.noBlocks: Set[Tuple[int, int]] = set()
        for start, end in self.lines:
            for a in ((x, y) for x in range(min(start[0], end[0]), max(start[0], end[0])+1) for y in range(min(start[1], end[1]), max(start[1], end[1])+1)):
                self.noBlocks.add(a)
        if LayerType.Blocks in self.uses:
            for pos in self.inverse(self.noBlocks):
                self.level[LayerType.Blocks].append(pos)
        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append(self.start)
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append(self.end)
        if LayerType.Door in self.uses and LayerType.Keys in self.uses:
            indexes: List[int] = list(range(1, self.order.index(self.end)-1))
            elements = list(sorted(sample(indexes, 3)))
            for i in elements[:2]:
                self.level[LayerType.Keys].append(self.order[i])
            self.level[LayerType.Door].append(self.order[elements[2]])
        elif LayerType.Door in self.uses:
            self.level[LayerType.Door].append(choice(self.notUsed))
        elif LayerType.Keys in self.uses:
            for pos in sample(self.notUsed, 2):
                self.level[LayerType.Keys].append(pos)
        if LayerType.Gold in self.uses:
            for pos in sample(self.notUsed, 3):
                self.level[LayerType.Gold].append(pos)
        if LayerType.Holder in self.uses:
            self.level[LayerType.Holder].append(choice(self.notUsed))
        if LayerType.Putter in self.uses:
            self.level[LayerType.Putter].append(choice(self.notUsed))
        if LayerType.Rock in self.uses:
            self.level[LayerType.Rock].append(choice(self.notUsed))
        return True

    def DFS(self, node):
        self.nodes.remove(node)
        self.order.append(node)
        if node == self.end:
            return
        posibilities = set([(node[0] + x, node[1]) for x in range(-3, 4)]) | set([(node[0], node[1] + y) for y in range(-3, 4)])
        posibilities.intersection_update(self.nodes)
        while len(posibilities):
            chosen = choice(list(posibilities))
            self.lines.add((node, chosen))
            self.DFS(chosen)
            posibilities.intersection_update(self.nodes)

    def RFS(self, start):
        frontier = {start}
        self.nodes.remove(start)
        self.order.append(start)
        while frontier:
            node = choice(list(frontier))
            frontier.remove(node)
            if node == self.end:
                continue
                # return
            posibilities = set([(node[0] + x, node[1]) for x in range(-3, 4)]) | set([(node[0], node[1] + y) for y in range(-3, 4)])
            posibilities.intersection_update(self.nodes)
            for posibility in posibilities:
                self.lines.add((node, posibility))
                frontier.add(posibility)
                self.nodes.remove(posibility)
                self.order.append(posibility)


class Rocks(Level):
    def generate(self):
        self.start = (1, self.shape[1])
        self.end = (self.shape[0], 1)

        self.level[LayerType.Dirt].append((1, self.shape[1] - 1))
        self.level[LayerType.Dirt].append((1, self.shape[1] - 2))
        self.level[LayerType.Dirt].append((2, self.shape[1]))
        self.level[LayerType.Dirt].append((2, self.shape[1] - 1))
        self.level[LayerType.Dirt].append((2, self.shape[1] - 2))
        self.level[LayerType.Dirt].append((3, self.shape[1]))
        self.level[LayerType.Dirt].append((3, self.shape[1] - 1))
        self.level[LayerType.Dirt].append((3, self.shape[1] - 2))

        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append(self.start)
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append(self.end)
        if LayerType.Rock in self.uses:
            for pos in sample(self.notUsed, 25):
                self.level[LayerType.Rock].append(pos)
        if LayerType.Dirt in self.uses:
            for pos in self.notUsed:
                self.level[LayerType.Dirt].append(pos)
        return True


class Causal1(Level):
    def generate(self):
        door_chance, key_chance, gold_chance = 0.025, 0.1, 0.1
        gold = choice(self.notUsed)
        if LayerType.Gold in self.uses:
            if random() > gold_chance:
                self.level[LayerType.Gold].append(gold)
        if LayerType.Door in self.uses:
            appender = self.level[LayerType.Door].append
            x, y = gold
            if x+1 != self.shape[0]+1 and random() > door_chance:
                appender((x+1, y))
            if x-1 != 0 and random() > door_chance:
                appender((x-1, y))
            if y+1 != self.shape[1]+1 and random() > door_chance:
                appender((x, y+1))
            if y-1 != 0 and random() > door_chance:
                appender((x, y-1))
        if LayerType.Keys in self.uses:
            if random() > key_chance:
                self.level[LayerType.Keys].append(choice(self.notUsed))
        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append(choice(self.notUsed))
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append(choice(self.notUsed))

        return True


class Causal2(Level):
    def generate(self):
        for layer in [LayerType.Player, LayerType.Goal]:
            if layer in self.uses:
                self.level[layer].append(choice(self.notUsed))

        for layer in [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]:
            if layer in self.uses and random() > 0.3:
                self.level[layer].append(choice(self.notUsed))

        return True


class Causal3(Level):
    def generate(self):
        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append((self.shape[0]//2, self.shape[1]//2))
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append((self.shape[0], self.shape[1]))
        if LayerType.Gold in self.uses:
            if random() > 0.2:
                self.level[LayerType.Gold].append((1, 1))
        if LayerType.Blocks in self.uses:
            for i in range(self.shape[1] - 1):
                self.level[LayerType.Blocks].append((2, 1 + i))
                self.level[LayerType.Blocks].append((self.shape[0] - 1, self.shape[1] - i))
        if random() > 0.2:
            if random() > 0.5:
                self.level[LayerType.Bluedoor].append((2, self.shape[1]))
            else:
                self.level[LayerType.Reddoor].append((2, self.shape[1]))
        if random() > 0.2:
            if random() > 0.5:
                self.level[LayerType.Bluedoor].append((self.shape[0] - 1, 1))
            else:
                self.level[LayerType.Reddoor].append((self.shape[0] - 1, 1))
        if LayerType.Bluekeys in self.uses:
            for pos in sample(self.notUsed, 4):
                if pos[0] > 2 and pos[0] < self.shape[0] - 2:
                    self.level[LayerType.Bluekeys].append(pos)
        if LayerType.Redkeys in self.uses:
            for pos in sample(self.notUsed, 4):
                if pos[0] > 2 and pos[0] < self.shape[0] - 2:
                    self.level[LayerType.Redkeys].append(pos)

        return True


class Causal4(Level):
    def generate(self):
        door_pos = choice(range(3))
        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append((self.shape[0]//2, self.shape[1]//2))
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append((self.shape[0], self.shape[1]))
        if LayerType.Gold in self.uses:
            self.level[LayerType.Gold].append((1, 1))
        if LayerType.Blocks in self.uses:
            for i in range(self.shape[1] - 1):
                self.level[LayerType.Blocks].append((self.shape[0] - 1, self.shape[1] - i))
            for i in range(self.shape[1] - 2):
                self.level[LayerType.Blocks].append((2, 1 + i))
            self.level[LayerType.Blocks].append((2, self.shape[1]))
            self.level[LayerType.Blocks].append((1, self.shape[1]))
            self.level[LayerType.Blocks].remove((self.shape[0] - 1, self.shape[1] - door_pos - 2))
        if LayerType.Rock in self.uses:
            self.level[LayerType.Rock].append((self.shape[0] - 1, self.shape[1] - door_pos - 2))
        if random() > 0.5:
            self.level[LayerType.Bluedoor].append((2, self.shape[1] - 1))
        else:
            self.level[LayerType.Reddoor].append((2, self.shape[1] - 1))
        if random() > 0.5:
            self.level[LayerType.Bluedoor].append((self.shape[0] - 1, 1))
        else:
            self.level[LayerType.Reddoor].append((self.shape[0] - 1, 1))
        if random() > 0.5:
            self.level[LayerType.Bluedoor].append((self.shape[0], self.shape[1] - door_pos - 1))
        else:
            self.level[LayerType.Reddoor].append((self.shape[0], self.shape[1] - door_pos - 1))

        if LayerType.Dirt in self.uses:
            for i in range(self.shape[1] - 1):
                self.level[LayerType.Dirt].append((1, 2 + i))
                self.level[LayerType.Dirt].append((self.shape[0], self.shape[1] - i - 1))
            self.level[LayerType.Dirt].remove((1, self.shape[1]))
            self.level[LayerType.Dirt].remove((self.shape[0], self.shape[1] - door_pos - 1))
        if LayerType.Bluekeys in self.uses:
            for pos in sample(self.notUsed, 3):
                if pos[0] > 2 and pos[0] < self.shape[0] - 2 and pos[1] < self.shape[1] - 1 and pos[1] > 0:
                    self.level[LayerType.Bluekeys].append(pos)
        if LayerType.Redkeys in self.uses:
            for pos in sample(self.notUsed, 3):
                if pos[0] > 2 and pos[0] < self.shape[0] - 2 and pos[1] < self.shape[1] - 1 and pos[1] > 0:
                    self.level[LayerType.Redkeys].append(pos)

        return True


class Causal5(Level):
    def generate(self):
        for layer in [LayerType.Player, LayerType.Goal]:
            if layer in self.uses:
                self.level[layer].append(choice(self.notUsed))

        for layer in [LayerType.Pink1, LayerType.Pink2, LayerType.Pink3, LayerType.Brown1, LayerType.Brown2, LayerType.Brown3]:
            if layer in self.uses and random() > 0.25:
                self.level[layer].append(choice(self.notUsed))

        return True


class Levels(Enum):
    Maze = Maze
    Rocks = Rocks
    Causal1 = Causal1
    Causal2 = Causal2
    Causal3 = Causal3
    Causal4 = Causal4
    Causal5 = Causal5
