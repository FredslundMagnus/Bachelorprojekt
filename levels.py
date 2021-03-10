from level import Level
from layers import LayerType
from typing import List, Tuple, Set
from random import choice, sample


class Maze(Level):
    def __init__(self, uses: List[LayerType], shape: Tuple[int, int], start: Tuple[int, int] = None, end: Tuple[int, int] = None) -> None:
        super().__init__(uses, shape, start, end)

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
    def __init__(self, uses: List[LayerType], shape: Tuple[int, int], start: Tuple[int, int] = None, end: Tuple[int, int] = None) -> None:
        super().__init__(uses, shape, start, end)

    def generate(self):
        self.start = choice(self.notUsed)
        self.end = choice(self.notUsed)

        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append(self.start)
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append(self.end)
        if LayerType.Rock in self.uses:
            for pos in sample(self.notUsed, 10):
                self.level[LayerType.Rock].append(pos)
        if LayerType.Dirt in self.uses:
            for pos in self.notUsed:
                self.level[LayerType.Dirt].append(pos)
        return True

