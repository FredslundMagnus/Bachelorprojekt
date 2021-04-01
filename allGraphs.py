from abc import abstractmethod
from layers import Diamond1
from torch import Tensor, tensor
from layer import LayerType
from itertools import combinations as combi
from main import *
from load import Load
from numpy import ndindex as ranges, array
from helper import restart
from graphs import Edge, Graph, Node
from threading import currentThread
from helper import device
from typing import FrozenSet, Dict, Iterable, List

environments = {
    Levels.Causal3: ["causal3_9x9_20hours", 2, [LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys]],
    Levels.Causal2: ["causal2_good_24h", 1, [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]],  # causal2_9x9_0.3, 0
    Levels.Causal1: ["causal1_good_24h", 0, [LayerType.Gold, LayerType.Keys, LayerType.Door]],
}

environment = environments[Levels.Causal2]
alpha = 0.9


class AllGraph(Graph):
    @property
    def updateNotes(self) -> List[function]:
        return [self.updateNotes1]

    @property
    def updateEdges(self) -> List[function]:
        return [self.updateEdges1]

    @abstractmethod
    def mostProbable(dict: Dict[FrozenSet[LayerType], float]):
        return max(dict, key=dict.get)

    def updateNotes1(self, nodes: List[Node]) -> None:
        """
        Hvert lag får værdien udfra hvor mange gange den står som nummer 1.
        """

        mostProbables = {}
        for layer in self.layers:
            mostProbables[layer] = AllGraph.mostProbable(self.data[layer])

        for node in nodes:
            node.value

    def updateEdges1(self, edges: List[Edge]) -> None:
        """
        Hver edge for værdien hvor mange gange der var en conection direkte fra
        Fra-noden til Til-noden.
        """
        # counter = {(layer1, layer2): 0 for layer1 in self.layers for layer2 in self.layers}
        # for path in self.data:
        #     for a, b in zip(path[1:], path[:-1]):
        #         counter[(a, b)] += self.data[path]

        # for edge in edges:
        #     edge.value = counter[(edge.fra.layer, edge.til.layer)]
        pass


def combinations(layer: LayerType) -> Iterable[FrozenSet[LayerType]]:
    for i in range(len(environment[2]) + 1):
        for c in combi([v for v in environment[2] if v != layer], i):
            yield frozenset(c)


def satatisfied(key: FrozenSet[LayerType], state: FrozenSet[LayerType]) -> bool:
    for layer in state:
        if layer not in key:
            return False
    return True


def bestIntervention(state: FrozenSet[LayerType], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]]) -> LayerType:
    maxV, maxL = 0, None
    for layer in environment[2]:
        temp = 0
        for key, value in data[layer].items():
            if not satatisfied(key, state):
                temp += value * (1-alpha)
        if temp >= maxV:
            maxV, maxL = temp, layer
    return maxL


def states(board: Tensor, convert: List[int]) -> Iterable[FrozenSet[LayerType]]:
    for batch in range(board.shape[0]):
        state = []
        for layer, i in zip(environment[2], convert):
            if not board[batch, i].sum().item():
                state.append(layer)
        yield frozenset(state)


def expand(state: FrozenSet[LayerType], hide: LayerType) -> Iterable[FrozenSet[LayerType]]:
    extras = [layer for layer in environment[2] if layer not in state and layer != hide]
    for i in range(1, len(extras) + 1):
        for c in combi(extras, i):
            yield frozenset(list(state) + list(c))


def compress(state: FrozenSet[LayerType]) -> Iterable[FrozenSet[LayerType]]:
    for i in range(len(state) + 1):
        for c in combi(state, i):
            yield frozenset(c)


def transform(old_states: List[FrozenSet[LayerType]], new_states: List[FrozenSet[LayerType]], dones: Tensor, rewards: Tensor, data: Dict[LayerType, Dict[FrozenSet[LayerType], float]]) -> None:
    for old_state, new_state, done, reward in zip(old_states, new_states, dones.tolist(), rewards.tolist()):
        if reward:
            for overkill in expand(old_state, None):
                data[LayerType.Goal][overkill] *= alpha
        elif not done and old_state != new_state:
            for layer in new_state.difference(old_state):
                for overkill in expand(old_state, layer):
                    data[layer][overkill] *= alpha


def transformNot(boards: Tensor, states: List[FrozenSet[LayerType]], player: int, goal: int, convert: List[int], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]]) -> None:
    for board, state in zip(boards, states):
        for layer, i in zip(environment[2] + [LayerType.Goal], convert + [goal]):
            if (board[player] * board[i]).sum().item():
                for undershoot in compress(state):
                    data[layer][undershoot] *= alpha


def runner(data=None):
    if data == None:
        data = {}
    for layer in environment[2]:
        data[layer] = {c: 1 for c in combinations(layer)}
    data[LayerType.Goal] = {c: 1 for c in combinations(None)}
    with Load(environment[0], num=environment[1]) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.extradim = 0  # fix
        teleporter.exploration.explore = teleporter.exploration.greedy
        convert = [env.layers.types.index(layer) for layer in environment[2]]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        intervention_idx, modified_board = teleporter.pre_process(env)
        old_states = [state for state in states(env.board, convert)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        for frame in loop(env, collector, teleporter=teleporter):
            # for layer in [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4, LayerType.Goal]:
            #     print(f"\n\n{layer.name}\n", {key: value for key, value in data[layer].items() if value > 0.001})
            #     print(f"\n", [key for key, value in data[layer].items() if value > 0.001])
            new_states = [state for state in states(env.board, convert)]
            transform(old_states, new_states, dones, rewards, data)
            transformNot(env.board, new_states, player, goal, convert, data)
            interventions = [bestIntervention(state, data) for state in new_states]
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)  # Only on the intervention layers
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            old_states = new_states
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                break


# runner()
AllGraph(runner, environment[2], usePlayer=False)
