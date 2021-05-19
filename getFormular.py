
from __future__ import annotations
from allGraphs import environments, Data, compress, LayerType
from game import Game
from load import Load
from pprint import pprint
from sympy import symbols, Symbol
from functools import reduce


def test_graphTrain(name: str) -> tuple[dict[LayerType, dict[frozenset[LayerType], float]], frozenset[LayerType]]:
    data = {}
    with Load(name, num=0) as load:
        env, dataN = load.items(Game, Data)
        for layer, states in dataN.data.items():
            data[layer] = {}
            for state in states:
                p = dataN.p(layer, state)
                if p != 0 and not any([dataN.p(layer, small) != 0 for small in compress(state, inclusiv_self=False)]):
                    data[layer][state] = p
                else:
                    data[layer][state] = 0
    return data, environments[env.level][2]


def getName(layer: LayerType, isMinus1: bool = True):
    return f"\img{'{'}{layer.name}{'}'}^{'{'}{'t-1' if isMinus1 else 't'}{'}'}"


def getActionName(layer: LayerType, isMinus1: bool = True):
    return f"\img{'{'}{LayerType.Player.name}{'}'}^{'{'}{'t-1' if isMinus1 else 't'}{'}'}_{'{'}\imgSmall{'{'}{layer.name}{'}'}{'}'}"


def formatState(state: frozenset[LayerType]):
    try:
        return reduce(lambda p0, p1: p0 * p1, (symbols(getName(layer)) for layer in state))
    except:
        return Symbol('')


def handleFloat(v: float) -> Symbol:
    return Symbol(f" Bernoulli({str(round(v, 1))})")


def clean(r: Symbol, layer: LayerType) -> str:
    r: str = str(r)
    if "+" in r:
        r = f"({r})"
    r += "*" + getActionName(layer)
    r = r.replace('0*', '').replace('*', '\cdot').replace("Bernoulli(1.0)\cdot", "")
    if r.startswith("\cdot"):
        r = r[5:]
    return r


def draw(name: str):
    data, layers = test_graphTrain(name)
    print('\\begin{align*} ')
    for layer, info in data.items():
        l = symbols(getName(layer, isMinus1=False)) if layer != LayerType.Goal else symbols('T^t')
        r = clean(sum([formatState(state) * handleFloat(chance) for state, chance in info.items() if chance]), layer)
        if layer == LayerType.Goal:
            print(f"{symbols(getName(layer, isMinus1=False))} &= {r}*(1-{symbols('T^{t-1}')})\\\\".replace('*', "\cdot"))
        print(f"{l} &= {r}+{getName(layer) if layer != LayerType.Goal else symbols('T^{t-1}')}", end="\n" if layer == LayerType.Goal else "\\\\\n")
    print('\\end{align*}')
    print("$$" + "\,\,\,,\,\,\,".join([f"{symbols(getActionName(layer, isMinus1=False))}=0" for layer in list(layers) + [LayerType.Goal]]) + "$$\n")


draw("Diamonds1_0.5_UCB1")
draw("Diamonds2_0.5_UCB1")
draw("Diamonds3_0.5_UCB1")
draw("Diamonds4_0.5_UCB1")

draw("Diamonds1_0.0_UCB1")
draw("Diamonds2_0.0_UCB1")
draw("Diamonds3_0.0_UCB1")
draw("Diamonds4_0.0_UCB1")
