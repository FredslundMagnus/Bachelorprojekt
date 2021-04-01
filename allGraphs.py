from torch import Tensor
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
gamma = 0.99


class AllGraph(Graph):
    @property
    def updateNotes(self) -> List[function]:
        return []

    @property
    def updateEdges(self) -> List[function]:
        return []

    def __len__(self) -> int:
        return max([len(path) for path in self.data])


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
                temp += value * (1-gamma)
        if temp >= maxV:
            maxV, maxL = temp, layer
    return maxL


def states(board: Tensor, convert: List[int]) -> Iterable[FrozenSet[LayerType]]:
    for batch in range(board.shape[0]):
        state = []
        for layer, i in zip(environment[2], convert):
            if board[batch, i].sum().item():
                state.append(layer)
        yield frozenset(state)


def transform(old_state: FrozenSet[LayerType], new_state: FrozenSet[LayerType], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]]) -> None:
    pass


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
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, teleporter=teleporter):
            new_states = states(env.board, convert)
            for old_state, new_state in zip(old_states, new_states):
                if old_state != new_state:
                    transform(old_state, new_state, data)

            interventions = [bestIntervention(state, data) for state in new_states]
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)  # Only on the intervention layers
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)

            old_states = new_states
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                break


runner()
# AllGraph(runner, environment[2])
