
from torch import Tensor
from layer import LayerType
from itertools import combinations as combi
from typing import FrozenSet, Iterable, List
from game import Game, Levels
from random import random
from dataclasses import dataclass
from enum import Enum
from math import sqrt, log
import torch
from helper import device


@dataclass
class Info:
    satisfiable: int = 0
    unsatisfiable: int = 0
    n: int = 0


class GraphMode(Enum):
    var = 0
    UCB1 = 1


class Data:
    def __init__(self, layers: List[LayerType] = None, graphMode: GraphMode = None) -> None:
        self.layers = layers
        self.data = {}
        self.graphMode = graphMode
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

    def UCB1(self, layer: LayerType, state: FrozenSet[LayerType]):
        info: Info = self.data[layer][state]
        c = 2
        if (n := info.n):
            Q = info.satisfiable / n
            return Q + c * sqrt(log(self.t)/n)
        return float('inf')

    def expected_moves_UCB1(self, state: FrozenSet[LayerType], layer: LayerType) -> float:
        if layer == LayerType.Goal:
            return 1/max(self.UCB1(LayerType.Goal, state), 1e-10)
        next_state = frozenset(list(state) + [layer])
        return 1/max(self.UCB1(layer, state), 1e-10) + min(self.expected_moves_UCB1(next_state, layer) for layer in self.layers_not_in(next_state))

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


def UCB1(state: FrozenSet[LayerType], data: Data) -> LayerType:
    return min(data.layers_not_in(state), key=lambda layer: data.expected_moves_UCB1(state, layer))


def transform(old_states: List[FrozenSet[LayerType]], new_states: List[FrozenSet[LayerType]], dones: Tensor, rewards: Tensor, data: Data, layers: List[LayerType], model, use_model) -> None:
    loss = 0
    for old_state, new_state, done, reward in zip(old_states, new_states, dones.tolist(), rewards.tolist()):
        if reward:
            if use_model:
                loss += model.learn(LayerType.Goal, old_state, True)
            data.satisfiable(LayerType.Goal, old_state)
        elif not done and old_state != new_state:
            for layer in new_state.difference(old_state):
                if use_model:
                    loss += model.learn(layer, old_state, True)
                data.satisfiable(layer, old_state)
    return loss


def transformNot(boards: Tensor, states: List[FrozenSet[LayerType]], player: int, goal: int, convert: List[int], data: Data, layers: List[LayerType], model, use_model) -> None:
    loss = 0
    for board, state in zip(boards, states):
        for layer, i in zip(layers + [LayerType.Goal], convert + [goal]):
            if (board[player] * board[i]).sum().item():
                if use_model:
                    loss += model.learn(layer, state, False)
                data.unsatisfiable(layer, state)
    return loss


def format(env: Game, layer: LayerType) -> List[bool]:
    best = env.layers.types.index(layer)
    return [best == i for i in range(env.board.shape[1])]


def getInterventions(env: Game, state: FrozenSet[LayerType], data: Data, exploration: float = 1) -> List[bool]:
    if data.graphMode == GraphMode.UCB1:
        return format(env, UCB1(state, data))
    if random() <= exploration:
        return format(env, bestIntervention(state, data))
    return format(env, rightIntervention(state, data))

def getInterventionsmodel(state, all_layers, layers, model, env, not_in):
    if random() <= model.exploration:
        br, ba = recursiveBEST(layers, state, model.depth, model, all_layers, 1, env, not_in)
    else:
        br, ba = recursiveExplore(layers, state, model.depth-2, model, all_layers, 1, env, not_in)
    return format(env, ba)

def recursiveBEST(layers, state, depth, model, all_layers, reward_trace, env, not_in):
    if depth == 0:
        return 0, None
    best_reward = 0
    best_action = [False for _ in range(len(all_layers))]
    for layer in all_layers:
        if layer in not_in:
            if depth == model.depth:
                prediction = model.predict(layer, state)
            else:
                prediction = model.predict_no_convert(layer, state)
            reward, _ = recursiveBEST(layers, prediction, depth-1, model, all_layers, reward_trace*(1 - prediction[0, len(layers)]), env, not_in)
            reward += prediction[0, len(layers)] * reward_trace
            if reward > best_reward:
                best_reward, best_action = reward, layer
    return best_reward, best_action

def recursiveExplore(layers, state, depth, model, all_layers, reward_trace, env, not_in):
    if depth == 0:
        return 0, None
    best_reward = 0
    best_action = [False for _ in range(len(all_layers))]
    for layer in all_layers:
        if layer in not_in:
            for j in range(model.samples):
                if j == 0:
                    if depth == model.depth-2:
                        prediction = model.predict(layer, state)
                    else:
                        prediction = model.predict_no_convert(layer, state)
                else: 
                    if depth == model.depth-2:
                        prediction = torch.cat((prediction, model.predict(layer, state)), dim=0)
                    else:
                        prediction = torch.cat((prediction, model.predict_no_convert(layer, state)), dim=0) 
            mean_pred = torch.mean(prediction, 0).unsqueeze(0)
            var_pred = torch.var(prediction, 0).unsqueeze(0)
            reward, _ = recursiveExplore(layers, mean_pred, depth-1, model, all_layers, reward_trace*(1 - prediction[0, len(layers)]), env, not_in)
            reward += torch.sum(var_pred) * reward_trace
            if reward > best_reward:
                best_reward, best_action = reward * reward_trace, layer
    return best_reward, best_action