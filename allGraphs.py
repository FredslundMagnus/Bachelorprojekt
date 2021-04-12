
from torch import Tensor
from layer import LayerType
from itertools import combinations as combi
from typing import FrozenSet, Iterable, List
from game import Game, Levels
from random import random
from dataclasses import dataclass


@dataclass
class Info:
    satisfiable: int = 0
    unsatisfiable: int = 0
    n: int = 0


class Data:
    def __init__(self, layers: List[LayerType] = None) -> None:
        self.layers = layers
        self.data = {}
        self.t = 0
        for layer in layers:
            self.data[layer] = {c: Info() for c in combinations(layer, layers)}
        self.data[LayerType.Goal] = {c: Info() for c in combinations(None, layers)}

    def satisfiable(self, layer: LayerType, state: FrozenSet[LayerType]):
        info = self.data[layer][state]
        info.satisfiable += 1
        info.n += 1

    def unsatisfiable(self, layer: LayerType, state: FrozenSet[LayerType]):
        info = self.data[layer][state]
        info.unsatisfiable += 1
        info.n += 1

    def p(self, layer: LayerType, state: FrozenSet[LayerType]):
        info: Info = self.data[layer][state]
        if (s := info.satisfiable):
            return s / info.n
        return 0

    def var(self, layer: LayerType, state: FrozenSet[LayerType]):
        info: Info = self.data[layer][state]
        a = 1
        n = info.n
        if n == 0:
            return float("inf")
        p = (info.satisfiable + a) / (n + 2*a)
        return (p * (1-p))/n

    def expected_moves(self, state: FrozenSet[LayerType], layer: LayerType) -> float:
        if layer == LayerType.Goal:
            return 1/max(self.p(LayerType.Goal, state), 1e-10)
        next_state = frozenset(list(state) + [layer])
        return 1/max(self.p(layer, state), 1e-10) + min(self.expected_moves(next_state, layer) for layer in self.layers_not_in(next_state))

    def n(self, layer: LayerType, state: FrozenSet[LayerType]):
        return self.data[layer][state].n

    def layers_not_in(self, state: FrozenSet[LayerType], goal_layer: bool = True):
        return [layer for layer in (self.layers + ([LayerType.Goal] if goal_layer else [])) if layer not in state]


environments = {
    Levels.Causal7: ["causal7_demo", 0, [LayerType.Greencross, LayerType.Bluecross, LayerType.Redcross, LayerType.Purplecross]],
    Levels.Causal6: ["causal6_demo", 0, [LayerType.Greendown, LayerType.Greenup, LayerType.Greenstar, LayerType.Yellowstar, LayerType.Bluestar]],
    Levels.Causal5: ["causal5_demo", 0, [LayerType.Pink1, LayerType.Brown1, LayerType.Pink2, LayerType.Brown2, LayerType.Pink3, LayerType.Brown3]],
    Levels.Causal3: ["causal3_demo", 0, [LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys]],
    Levels.Causal2: ["causal2_demo", 0, [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]],
    Levels.Causal1: ["causal1_demo", 0, [LayerType.Gold, LayerType.Keys, LayerType.Door]],
}


def combinations(layer: LayerType, layers: List[LayerType]) -> Iterable[FrozenSet[LayerType]]:
    for i in range(len(layers) + 1):
        for c in combi([v for v in layers if v != layer], i):
            yield frozenset(c)


def satatisfied(key: FrozenSet[LayerType], state: FrozenSet[LayerType]) -> bool:
    for layer in state:
        if layer not in key:
            return False
    return True


def states(board: Tensor, convert: List[int], layers: List[LayerType]) -> Iterable[FrozenSet[LayerType]]:
    for batch in range(board.shape[0]):
        state = []
        for layer, i in zip(layers, convert):
            if not board[batch, i].sum().item():
                state.append(layer)
        yield frozenset(state)


def compress(state: FrozenSet[LayerType], inclusiv_self=True) -> Iterable[FrozenSet[LayerType]]:
    for i in range(len(state) + int(inclusiv_self)):
        for c in combi(state, i):
            yield frozenset(c)


def bestIntervention(state: FrozenSet[LayerType], data: Data) -> LayerType:
    return max(data.layers_not_in(state), key=lambda layer: data.var(layer, state))


def rightIntervention(state: FrozenSet[LayerType], data: Data) -> LayerType:
    return min(data.layers_not_in(state), key=lambda layer: data.expected_moves(state, layer))


def transform(old_states: List[FrozenSet[LayerType]], new_states: List[FrozenSet[LayerType]], dones: Tensor, rewards: Tensor, data: Data, layers: List[LayerType]) -> None:
    for old_state, new_state, done, reward in zip(old_states, new_states, dones.tolist(), rewards.tolist()):
        if reward:
            data.satisfiable(LayerType.Goal, old_state)
        elif not done and old_state != new_state:
            for layer in new_state.difference(old_state):
                data.satisfiable(layer, old_state)


def transformNot(boards: Tensor, states: List[FrozenSet[LayerType]], player: int, goal: int, convert: List[int], data: Data, layers: List[LayerType]) -> None:
    for board, state in zip(boards, states):
        for layer, i in zip(layers + [LayerType.Goal], convert + [goal]):
            if (board[player] * board[i]).sum().item():
                data.unsatisfiable(layer, state)


def getInterventions(env: Game, state: FrozenSet[LayerType], data: Data, exploration: float = 1) -> List[bool]:
    if random() <= exploration:
        best = env.layers.types.index(bestIntervention(state, data))
    else:
        best = env.layers.types.index(rightIntervention(state, data))
    return [best == i for i in range(env.board.shape[1])]
