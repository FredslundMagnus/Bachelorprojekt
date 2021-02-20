from level import Level
from layers import LayerType
from typing import List, Tuple, Set
from random import choice, sample


class Maze(Level):
    def __init__(self, uses: List[LayerType], shape: Tuple[int, int], start: Tuple[int, int], end: Tuple[int, int]) -> None:
        super().__init__(uses, shape, start, end)

    def generate(self):
        if LayerType.Blocks not in self.uses:
            return False
        xs = [i for i in range(1, self.shape[0]+1) if i % 2 == 1]
        ys = [i for i in range(1, self.shape[1]+1) if i % 2 == 1]
        if self.shape[0] % 2 == 0:
            xs[-1] += 1
        if self.shape[1] % 2 == 0:
            ys[-1] += 1
        self.nodes: Set[Tuple[int, int]] = set([(x, y) for x in xs for y in ys])
        if self.start not in self.nodes or self.end not in self.nodes:
            return False
        self.lines: Set[Tuple[Tuple[int, int], Tuple[int, int]]] = set()
        self.DFS(self.start)
        self.noBlocks: Set[Tuple[int, int]] = set()
        for start, end in self.lines:
            for a in ((x, y) for x in range(min(start[0], end[0]), max(start[0], end[0])+1) for y in range(min(start[1], end[1]), max(start[1], end[1])+1)):
                self.noBlocks.add(a)

        for pos in self.inverse(self.noBlocks):
            self.level[LayerType.Blocks].append(pos)

        if LayerType.Door in self.uses and LayerType.Keys in self.uses:
            nodes: Set[Tuple[int, int]] = set(self.noBlocks)
            nodes.remove(self.end)
            posibilities = set([(self.end[0] + x, self.end[1]) for x in range(-1, 2)]) | set([(self.end[0], self.end[1] + y) for y in range(-1, 2)])
            posibilities.intersection_update(nodes)
            for pos in posibilities:
                print(pos)
                self.level[LayerType.Door].append(pos)
            nodes: Set[Tuple[int, int]] = [(x, y) for x in xs for y in ys]
            nodes.remove(self.end)
            nodes.remove(self.start)
            first = choice(nodes)
            nodes.remove(first)
            self.level[LayerType.Keys].append(first)
            self.level[LayerType.Keys].append(choice(nodes))
        if LayerType.Gold in self.uses:
            nodes: Set[Tuple[int, int]] = [(x, y) for x in xs for y in ys]
            nodes.remove(self.end)
            nodes.remove(self.start)
            for pos in self.level[LayerType.Keys]:
                nodes.remove(pos)
            first = choice(nodes)
            nodes.remove(first)
            self.level[LayerType.Gold].append(first)
            self.level[LayerType.Gold].append(choice(nodes))

        if LayerType.Player in self.uses:
            self.level[LayerType.Player].append(self.start)
        if LayerType.Goal in self.uses:
            self.level[LayerType.Goal].append(self.end)
        return True

    def DFS(self, node):
        self.nodes.remove(node)
        if node == self.end:
            return
        posibilities = set([(node[0] + x, node[1]) for x in range(-3, 4)]) | set([(node[0], node[1] + y) for y in range(-3, 4)])
        posibilities.intersection_update(self.nodes)
        while len(posibilities):
            chosen = choice(list(posibilities))
            self.lines.add((node, chosen))
            self.DFS(chosen)
            posibilities.intersection_update(self.nodes)


print(Maze([LayerType.Blocks, LayerType.Door, LayerType.Keys], (7, 7), (1, 1), (7, 7)).level[LayerType.Blocks])
