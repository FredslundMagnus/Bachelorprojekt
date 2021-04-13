
from allGraphs import environments, Data, compress
from game import Game
from load import Load
from helper import function
from abc import abstractmethod
from graphs import Edge, Graph, Node
from typing import FrozenSet, Dict, List
from layer import LayerType


class AllGraph(Graph):
    @property
    def updateNotes(self) -> List[function]:
        return [self.Notes]

    @property
    def updateEdges(self) -> List[function]:
        return [self.Edges]

    @abstractmethod
    def mostProbable(dict: Dict[FrozenSet[LayerType], float]):
        return max(dict, key=dict.get)

    def Notes(self, nodes: List[Node]) -> None:
        """
        Hvert node ligger som næste element, hvis det er mulig at tage den ud fra de elementer tidligere i listen.
        """

        mostProbables = {}
        ls = {}
        for layer in self.layers:
            mostProbables[layer] = AllGraph.mostProbable(self.data[layer])
            ls[layer] = len(mostProbables[layer])
        curentSets = set(frozenset())
        removed = set()
        layers = {layer for layer in self.layers}
        i = 0
        while any(layers) and i < 10:
            for layer in layers:
                if mostProbables[layer] in curentSets:
                    [node for node in nodes if node.layer == layer][0].value = i
                    removed.add(layer)
            layers = {layer for layer in self.layers if layer not in removed}
            curentSets = set(compress(removed))
            i += 1

    def Edges(self, edges: List[Edge]) -> None:
        """
        Chance for Fra-nodes til Til-nodes
        """
        for edge in edges:
            edge.value = 1
            for s, v in self.data[edge.til.layer].items():
                if edge.fra.layer in s:
                    edge.value *= 1 - v
            edge.value = 1 - edge.value
            if self.isMinimised:
                edge.value = 0 if edge.value == 0 else 1


def test_graphTrain(data=None, getLayers=False):
    with Load("causal2_online_var_0.5_full", num=0) as load:
        env, dataN = load.items(Game, Data)
        if getLayers:
            return environments[env.level][2]
        for layer, states in dataN.data.items():
            data[layer] = {}
            for state in states:
                p = dataN.p(layer, state)
                if p != 0 and not any([dataN.p(layer, small) != 0 for small in compress(state, inclusiv_self=False)]):
                    data[layer][state] = p
                else:
                    data[layer][state] = 0


AllGraph(test_graphTrain, test_graphTrain(getLayers=True), usePlayer=False)
