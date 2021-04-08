from abc import abstractmethod
# from paint import Paint
from torch import Tensor, tensor, cat
from layer import LayerType
from itertools import combinations as combi
# from main import *
from load import Load
from threading import currentThread
from typing import FrozenSet, Dict, Iterable, List
from game import Game, Levels
from agent import Teleporter, Mover, Networks, Learners, Explorations, MetaTeleporter, CFAgent
from collector import Collector
from auxillaries import loop, Save
from helper import function
from random import random

environments = {
    Levels.Causal7: ["causal7_demo", 0, [LayerType.Greencross, LayerType.Bluecross, LayerType.Redcross, LayerType.Purplecross]],
    Levels.Causal6: ["causal6_demo", 0, [LayerType.Greendown, LayerType.Greenup, LayerType.Greenstar, LayerType.Yellowstar, LayerType.Bluestar]],
    Levels.Causal5: ["causal5_demo", 0, [LayerType.Pink1, LayerType.Brown1, LayerType.Pink2, LayerType.Brown2, LayerType.Pink3, LayerType.Brown3]],
    Levels.Causal3: ["causal3_demo", 0, [LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys]],
    Levels.Causal2: ["causal2_demo", 0, [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]],
    Levels.Causal1: ["causal1_demo", 0, [LayerType.Gold, LayerType.Keys, LayerType.Door]],
}

level = Levels.Causal7
alpha = 0.95
useBestIntervention = True
GAME_UI = False
if __name__ == "__main__":
    from graphs import Edge, Graph, Node

    class AllGraph(Graph):
        @property
        def updateNotes(self) -> List[function]:
            return [self.updateNotes1]

        @property
        def updateEdges(self) -> List[function]:
            return [self.updateEdges0, self.updateEdges1, self.updateEdges2, self.updateEdges3, self.updateEdges4, self.updateEdges5]

        @abstractmethod
        def mostProbable(dict: Dict[FrozenSet[LayerType], float]):
            return max(dict, key=dict.get)

        def updateNotes1(self, nodes: List[Node]) -> None:
            """
            Hvert lag får værdien udfra hvor mange gange den står som nummer 1.
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

        def updateEdges0(self, edges: List[Edge]) -> None:
            """
            Ikke normaliseret
            """
            for edge in edges:
                edge.value = 0
                for s, v in self.data[edge.til.layer].items():
                    if edge.fra.layer in s:
                        edge.value += v

        def updateEdges1(self, edges: List[Edge]) -> None:
            """
            Normaliseret med fra nodes
            """
            self.updateEdges0(edges)
            for edge in edges:
                edge.value /= sum(self.data[edge.fra.layer].values())

        def updateEdges2(self, edges: List[Edge]) -> None:
            """
            Normaliseret med til nodes
            """
            self.updateEdges0(edges)
            for edge in edges:
                edge.value /= sum(self.data[edge.til.layer].values())

        def updateEdges3(self, edges: List[Edge]) -> None:
            """
            Normaliseret med antal gange fra og til var mulige
            """
            self.updateEdges0(edges)
            for edge in edges:
                try:
                    edge.value /= sum([1 for key in self.data[edge.fra.layer] if edge.til.layer in key])
                except Exception as e:
                    edge.value = 0

        def updateEdges4(self, edges: List[Edge]) -> None:
            """
            Max-værdien fra Fra-nodes til Til-nodes
            """
            for edge in edges:
                edge.value = 0
                for s, v in self.data[edge.til.layer].items():
                    if edge.fra.layer in s:
                        edge.value = max(edge.value, v)

        def updateEdges5(self, edges: List[Edge]) -> None:
            """
            Chance for Fra-nodes til Til-nodes
            """
            for edge in edges:
                edge.value = 1
                for s, v in self.data[edge.til.layer].items():
                    if edge.fra.layer in s:
                        edge.value *= 1 - v
                edge.value = 1 - edge.value


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


def expand(state: FrozenSet[LayerType], hide: LayerType, layers: List[LayerType]) -> Iterable[FrozenSet[LayerType]]:
    extras = [layer for layer in layers if layer not in state and layer != hide]
    for i in range(1, len(extras) + 1):
        for c in combi(extras, i):
            yield frozenset(list(state) + list(c))


def compress(state: FrozenSet[LayerType]) -> Iterable[FrozenSet[LayerType]]:
    for i in range(len(state) + 1):
        for c in combi(state, i):
            yield frozenset(c)


def flip_chance(state: FrozenSet[LayerType], layer: LayerType, data: Dict[LayerType,  Dict[FrozenSet[LayerType], float]]):
    chanceForFlip = 1
    for partial in compress(state):
        chanceForFlip *= (1 - data[layer][partial])
    return 1 - chanceForFlip


def bestIntervention(state: FrozenSet[LayerType], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]], layers: List[LayerType]) -> LayerType:
    maxV, maxL = 0, None
    for layer in [layer for layer in (layers + [LayerType.Goal]) if layer not in state]:

        chanceForFlip = min(flip_chance(state, layer, data), 0.99)

        temp = 0
        for overkill in expand(state, layer, layers):
            temp += data[layer][overkill] * (1-alpha) * chanceForFlip

        for partial in compress(state):
            temp += data[layer][partial] * (1-alpha) * (1-chanceForFlip)

        if temp >= maxV:
            maxV, maxL = temp, layer
    return maxL


def rightIntervention(state: FrozenSet[LayerType], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]], layers: List[LayerType]) -> LayerType:
    layer = LayerType.Goal
    used = {LayerType.Goal}
    while flip_chance(state, layer, data) <= 0.9:
        stats = {explainer: flip_chance(explainer, layer, data) for explainer in data[layer] if not any(use in explainer for use in used)}
        if stats == {}:
            chances = {layer: flip_chance(state, layer, data) for layer in layers if layer not in state}
            if chances == {}:
                return LayerType.Goal
            return max(chances, key=chances.get)
        chances = {layer: flip_chance(state, layer, data) for layer in max(stats, key=stats.get) if layer not in stats and layer not in used}
        if chances == {}:
            chances = {layer: flip_chance(state, layer, data) for layer in layers if layer not in state}
            if chances == {}:
                return LayerType.Goal
            return max(chances, key=chances.get)
        layer = max(chances, key=chances.get)
        used.add(layer)
    return layer


def transform(old_states: List[FrozenSet[LayerType]], new_states: List[FrozenSet[LayerType]], dones: Tensor, rewards: Tensor, data: Dict[LayerType, Dict[FrozenSet[LayerType], float]], layers: List[LayerType]) -> None:
    for old_state, new_state, done, reward in zip(old_states, new_states, dones.tolist(), rewards.tolist()):
        if reward:
            for overkill in expand(old_state, None, layers):
                data[LayerType.Goal][overkill] *= alpha
        elif not done and old_state != new_state:
            for layer in new_state.difference(old_state):
                for overkill in expand(old_state, layer, layers):
                    data[layer][overkill] *= alpha


def transformNot(boards: Tensor, states: List[FrozenSet[LayerType]], player: int, goal: int, convert: List[int], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]], layers: List[LayerType]) -> None:
    for board, state in zip(boards, states):
        for layer, i in zip(layers + [LayerType.Goal], convert + [goal]):
            if (board[player] * board[i]).sum().item():
                for undershoot in compress(state):
                    data[layer][undershoot] *= alpha


def getInterventions(env: Game, state: FrozenSet[LayerType], data: Dict[LayerType, Dict[FrozenSet[LayerType], float]], layers: List[LayerType], exploration: float = 1) -> List[bool]:
    if random() <= exploration:
        best = env.layers.types.index(bestIntervention(state, data, layers))
    else:
        best = env.layers.types.index(rightIntervention(state, data, layers))
    return [best == i for i in range(env.board.shape[1])]


def runnerBestIntervention(data=None):
    layers: List[LayerType] = environments[level][2]
    if data == None:
        data = {}
    for layer in layers:
        data[layer] = {c: 1 for c in combinations(layer, layers)}
    data[LayerType.Goal] = {c: 1 for c in combinations(None, layers)}
    with Load(environments[level][0], num=environments[level][1]) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        convert = [env.layers.types.index(layer) for layer in layers]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        old_states = [state for state in states(env.board, convert, layers)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        eatCheese, interventions = ([True] * env.batch, [None] * env.batch)  # New
        for frame in loop(env, collector, teleporter=teleporter):
            new_states = [state for state in states(env.board, convert, layers)]
            transform(old_states, new_states, dones, rewards, data, layers)
            transformNot(env.board, new_states, player, goal, convert, data, layers)
            stateChanged = [old != new for old, new in zip(old_states, new_states)]  # New
            shouldInterviene = [cond1 or cond2 for cond1, cond2 in zip(stateChanged, eatCheese)]  # New
            # interventions = tensor([getInterventions(env, state, data) for state in new_states]) # Old
            interventions = [(getInterventions(env, state, data, layers) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]  # New
            modification = env.board[tensor(interventions)].unsqueeze(1)
            teleporter.interventions = [m.flatten().argmax().item() for m in list(modification)]
            modified_board = cat((env.board, modification), dim=1)
            actions = mover(modified_board)
            _, rewards, dones, _ = env.step(actions)
            playerPositions = [(t := env.layers.dict[LayerType.Player].positions[i][0])[1] * env.layers.width + t[0] for i in range(env.batch)]  # New
            eatCheese = [intervention == player_pos for intervention, player_pos in zip(teleporter.interventions, playerPositions)]  # New
            old_states = new_states
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                break


def runnerNormalTeleport(data=None):
    layers: List[LayerType] = environments[level][2]
    if data == None:
        data = {}
    for layer in layers:
        data[layer] = {c: 1 for c in combinations(layer, layers)}
    data[LayerType.Goal] = {c: 1 for c in combinations(None, layers)}
    with Load(environments[level][0], num=environments[level][1]) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.extradim = 0  # fix
        teleporter.exploration.explore = teleporter.exploration.greedy
        convert = [env.layers.types.index(layer) for layer in layers]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        intervention_idx, modified_board = teleporter.pre_process(env)
        old_states = [state for state in states(env.board, convert, layers)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        for frame in loop(env, collector, teleporter=teleporter):
            new_states = [state for state in states(env.board, convert, layers)]
            transform(old_states, new_states, dones, rewards, data, layers)
            transformNot(env.board, new_states, player, goal, convert, data, layers)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            old_states = new_states
            setattr(currentThread(), "frame", frame)
            if getattr(currentThread(), "do_run", True) == False:
                break


if __name__ == "__main__":
    if GAME_UI:
        runnerBestIntervention() if useBestIntervention else runnerNormalTeleport()
    else:
        AllGraph(runnerBestIntervention if useBestIntervention else runnerNormalTeleport, environments[level][2], usePlayer=False)
