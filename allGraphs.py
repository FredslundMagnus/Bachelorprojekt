from typing import List
from layer import LayerType
from itertools import combinations as combi
from main import *
from load import Load
from numpy import ndindex as ranges, array
from helper import restart
from graphs import Edge, Graph, Node
from threading import currentThread
from helper import device
from typing import FrozenSet, Dict

environments = {
    Levels.Causal3: ["causal3_9x9_20hours", 2, [LayerType.Gold, LayerType.Bluedoor, LayerType.Bluekeys, LayerType.Reddoor, LayerType.Redkeys]],
    Levels.Causal2: ["causal2_good_24h", 1, [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]],  # causal2_9x9_0.3, 0
    Levels.Causal1: ["causal1_good_24h", 0, [LayerType.Gold, LayerType.Keys, LayerType.Door]],
}

environment = environments[Levels.Causal2]
gamma = 0.99


def combinations(layer: Levels):
    for i in range(len(environment[2])):
        for c in combi([v for v in environment[2] if v != layer], i):
            yield frozenset(c)


def satatisfied(key: FrozenSet[Levels], state: FrozenSet[Levels]) -> bool:
    pass


def bestIntervention(state: FrozenSet[Levels], data: Dict[Levels, Dict[FrozenSet[Levels], float]]) -> Levels:
    maxV, maxL = 0, None
    for layer in environment[2]:
        temp = 0
        for key, value in data[layer].items():
            if not satatisfied(key, state):
                temp += value * (1-gamma)
        if temp >= maxV:
            maxV, maxL = temp, layer
    return maxL


def runner(data=None):
    if data == None:
        data = {}
    for layer in environment[2]:
        data[layer] = {c: 1 for c in combinations(layer)}
    print(data[layer])


runner()
