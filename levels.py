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
            for pos in sample(self.notUsed, 30):
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


class Levels(Enum):
    Maze = Maze
    Rocks = Rocks
    Causal1 = Causal1
