
from allGraphs import environments, AllGraph
from game import Game
from load import Load


def test_graphTrain(data=None, getLayers=False):
    with Load("causal7_online", num=0) as load:
        env, dataN = load.items(Game, dict)
        if getLayers:
            return environments[env.level][2]
        for key, value in dataN.items():
            data[key] = value


AllGraph(test_graphTrain, test_graphTrain(getLayers=True), usePlayer=False)
