from typing import List
from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges, array
from helper import restart
from graphs import Edge, Graph, Node
from threading import currentThread

environments = {
    Levels.Causal3: ["causal3_9x9_20hours", 2, [LayerType.Gold, LayerType.Dirt, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys]],
    Levels.Causal2: ["causal2_9x9", 2, [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]]
}

environment = environments[Levels.Causal3]
useLayersOnlyOnce = False


class PathGraph(Graph):
    @property
    def updateNotes(self) -> List[function]:
        return [self.updateNotes1, self.updateNotes2, self.updateNotes3, self.updateNotes4]

    @property
    def updateEdges(self) -> List[function]:
        return [self.updateEdges1, self.updateEdges2, self.updateEdges3]

    def updateNotes1(self, nodes: List[Node]) -> None:
        """
        Hvert lag får værdien udfra hvor stor procentdel, (af de gange
        den indgik i en plan), hvor den var i position 1.
        """
        counter_pos = [{k: 0 for k in self.layers} for _ in range(len(self.layers))]
        for path in self.data:
            for i, k in enumerate(path):
                counter_pos[i][k] += self.data[path]

        counter_total = {k: 0 for k in self.layers}
        for path in self.data:
            for k in counter_total:
                if k in path:
                    counter_total[k] += self.data[path]
        for node in nodes:
            k = node.layer
            node.value = counter_pos[0][k]/counter_total[k]

    def updateNotes2(self, nodes: List[Node]) -> None:
        """
        Hvert lag får værdien udfra hvor mange gange den står som nummer 1.
        """
        counter_pos = [{k: 0 for k in self.layers} for _ in range(len(self.layers))]
        for path in self.data:
            for i, k in enumerate(path):
                counter_pos[i][k] += self.data[path]

        for node in nodes:
            k = node.layer
            node.value = counter_pos[0][k]

    def updateNotes3(self, nodes: List[Node]) -> None:
        """
        Hvert lag får den værdi der svarer til det index hvor den
        fleste gange var på det index.
        """
        counter_pos = [{k: 0 for k in self.layers} for _ in range(len(self.layers))]
        for path in self.data:
            for i, k in enumerate(path):
                counter_pos[i][k] += self.data[path]

        for node in nodes:
            k = node.layer
            maxi = 0
            for i in range(len(self.layers)):
                if counter_pos[i][k] > counter_pos[maxi][k]:
                    maxi = i
                node.value = len(self.layers) - maxi

    def updateNotes4(self, nodes: List[Node]) -> None:
        """
        Hvert lag får den værdi der svarer til det index hvor den
        fylder den største procentdel i forhold til de andre index.
        """
        counter_pos = [{k: 0 for k in self.layers} for _ in range(len(self.layers))]
        for path in self.data:
            for i, k in enumerate(path):
                counter_pos[i][k] += self.data[path]

        pr_pos = [sum(counter.values()) for counter in counter_pos]

        for node in nodes:
            k = node.layer
            maxi = 0
            for i in range(len(self.layers)):
                if counter_pos[i][k] / pr_pos[i] > counter_pos[maxi][k] / pr_pos[maxi]:
                    maxi = i
                node.value = len(self.layers) - maxi

        self.minimize(nodes)

    def updateEdges1(self, edges: List[Edge]) -> None:
        """
        Hver edge for værdien hvor mange gange der var en conection direkte fra
        Fra-noden til Til-noden.
        """
        counter = {(layer1, layer2): 0 for layer1 in self.layers for layer2 in self.layers}
        for path in self.data:
            for a, b in zip(path[1:], path[:-1]):
                counter[(a, b)] += self.data[path]

        for edge in edges:
            edge.value = counter[(edge.fra.layer, edge.til.layer)]

    def updateEdges2(self, edges: List[Edge]) -> None:
        """
        Hver edge for værdien udfra hvor mange gange der var en conection direkte fra
        Fra-noden til Til-noden divideret med antallet af gange hvor der var 0 eller
        flere mellem nodes mellem Fra-noden og Til-Noden.
        """
        counters = [{(layer1, layer2): 0 for layer1 in self.layers for layer2 in self.layers} for i in range(len(self.layers)-1)]
        for i, counter in enumerate(counters, start=1):
            for path in self.data:
                try:
                    for a, b in zip(path[i:], path[:-i]):
                        counter[(a, b)] += self.data[path]
                except Exception:
                    pass
        for edge in edges:
            try:
                edge.value = counters[0][(edge.fra.layer, edge.til.layer)] / sum([counter[(edge.fra.layer, edge.til.layer)] for counter in counters])
            except ZeroDivisionError:
                edge.value = 0

    def updateEdges3(self, edges: List[Edge]) -> None:
        """
        Hver edge for værdien hvor mange gange der var en conection direkte fra
        Fra-noden til Til-noden i forholdet til hvor mange gange der var en 
        forbindesle enten fra Fra-noden til Til-noden eller den anden vej.
        """
        counter = {(layer1, layer2): 0 for layer1 in self.layers for layer2 in self.layers}
        for path in self.data:
            for a, b in zip(path[1:], path[:-1]):
                counter[(a, b)] += self.data[path]

        for edge in edges:
            edge.value = counter[(edge.fra.layer, edge.til.layer)] / (counter[(edge.fra.layer, edge.til.layer)] + counter[(edge.til.layer, edge.fra.layer)])


def createCausalGraph(data=None):
    with Load(environment[0], num=environment[1]) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.extradim = 0  # fix
        teleporter.exploration.explore = teleporter.exploration.greedy
        flippables = environment[2]
        convert = [env.layers.types.index(layer) for layer in flippables]
        d = {}
        if data == None:
            data = {}
        for frame in loop(env, collector, teleporter=teleporter):
            intervention_idx, modified_board = teleporter.pre_process(env)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            movers = array([torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])])[:50]
            mask = array([layer in convert for layer in movers])
            results = torch.zeros((50, *(shape := (len(flippables), *env.board.shape[2:]))))
            for layer, x, y in ranges(shape):
                board = env.board[:50]
                pixel = board[:, convert[layer], x, y]
                board[:, convert[layer], x, y][pixel == 0], board[:, convert[layer], x, y][pixel == 1], board[:, convert[layer], x, y][pixel == 2] = 2, 0, 1
                results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
            flip = list(results[mask].max(dim=3)[0].max(dim=2)[0].argsort(dim=1, descending=True))
            paths = [[] for _ in range(len(flip))]
            for i in range(len(flippables)):
                flippers = [convert[v[i]] for v in flip]
                for i, f in enumerate(flippers):
                    paths[i].append(f)
                alive = [v1 != v2 for v1, v2 in zip(flippers, list(movers[mask]))]
                flip = [v for v, a in zip(flip, alive) if a]
                for p in [v for v, a in zip(paths, alive) if not a]:
                    if tuple(p) in d:
                        d[tuple(p)] += 1
                        data[tuple([LayerType.Goal] + [flippables[convert.index(k)] for k in p] + [LayerType.Player])] += 1
                    else:
                        d[tuple(p)] = 1
                        data[tuple([LayerType.Goal] + [flippables[convert.index(k)] for k in p] + [LayerType.Player])] = 1
                paths = [v for v, a in zip(paths, alive) if a]
                mask[mask] = alive
            # Printer de 10 mest sete paths
            # for k in list(sorted(d, key=d.get, reverse=True))[:10]:
            #     print(k, d[k], end=" : ")
            # print("")
            restart(env)
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                print("")
                break

        counter_pos = [{k: 0 for k in convert} for _ in range(len(flippables))]
        for path in d:
            for i, k in enumerate(path):
                counter_pos[i][k] += d[path]

        counter_total = {k: 0 for k in convert}
        for path in d:
            for k in counter_total:
                if k in path:
                    counter_total[k] += d[path]
        for i, counter in enumerate(counter_pos):
            print("Position", i+1)
            for layer, k in zip(flippables, convert):
                percent = counter_pos[i][k]/counter_total[k]
                print(f"{layer.name}: {str(100*percent)[:4]}% of {layer.name}'s total {counter_total[k]} times in a path.")
            print("")


def createCausalGraph2(data=None):
    with Load(environment[0], num=environment[1]) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.extradim = 0  # fix
        teleporter.exploration.explore = teleporter.exploration.greedy
        flippables = environment[2]
        convert = [env.layers.types.index(layer) for layer in flippables]
        d = {}
        if data == None:
            data = {}
        for frame in loop(env, collector, teleporter=teleporter):
            intervention_idx, modified_board = teleporter.pre_process(env)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            movers = array([torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])])[:50]
            mask = array([layer in convert for layer in movers])
            results = torch.zeros((50, *(shape := (len(flippables), *env.board.shape[2:]))))
            for layer, x, y in ranges(shape):
                board = env.board[:50]
                pixel = board[:, convert[layer], x, y]
                board[:, convert[layer], x, y][pixel == 0], board[:, convert[layer], x, y][pixel == 1], board[:, convert[layer], x, y][pixel == 2] = 2, 0, 1
                results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
            board_size = (results[mask].shape[2] * results[mask].shape[3])
            resulto = results[mask].flatten(start_dim=1)
            flip = []
            for i in range(results[mask].shape[0]):
                order = []
                for _ in range(20):
                    maxers = torch.argmax(resulto[i])
                    order.append((maxers//board_size).item())
                    resulto[i][maxers] = -10**6
                flip.append(torch.tensor(order))
            paths = [[] for _ in range(len(flip))]
            for i in range(len(flippables)):
                flippers = [convert[v[i]] for v in flip]
                for i, f in enumerate(flippers):
                    paths[i].append(f)
                alive = [v1 != v2 for v1, v2 in zip(flippers, list(movers[mask]))]
                flip = [v for v, a in zip(flip, alive) if a]
                for p in [v for v, a in zip(paths, alive) if not a]:
                    if tuple(p) in d:
                        d[tuple(p)] += 1
                        data[tuple([LayerType.Goal] + [flippables[convert.index(k)] for k in p] + [LayerType.Player])] += 1
                    else:
                        d[tuple(p)] = 1
                        data[tuple([LayerType.Goal] + [flippables[convert.index(k)] for k in p] + [LayerType.Player])] = 1
                paths = [v for v, a in zip(paths, alive) if a]
                mask[mask] = alive
            # Printer de 10 mest sete paths
            # for k in list(sorted(d, key=d.get, reverse=True))[:10]:
            #     print(k, d[k], end=" : ")
            # print("")
            restart(env)
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                print("")
                break

        counter_pos = [{k: 0 for k in convert} for _ in range(len(flippables))]
        for path in d:
            for i, k in enumerate(path):
                counter_pos[i][k] += d[path]

        counter_total = {k: 0 for k in convert}
        for path in d:
            for k in counter_total:
                if k in path:
                    counter_total[k] += d[path]
        for i, counter in enumerate(counter_pos):
            print("Position", i+1)
            for layer, k in zip(flippables, convert):
                percent = counter_pos[i][k]/counter_total[k]
                print(f"{layer.name}: {str(100*percent)[:4]}% of {layer.name}'s total {counter_total[k]} times in a path.")
            print("")


PathGraph(createCausalGraph if useLayersOnlyOnce else createCausalGraph2, environment[2])
