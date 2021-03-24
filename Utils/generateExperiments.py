
from main import Defaults, teleport, simple
from network import Networks
from learner import Learners
from levels import Levels, Rocks
from agent import Teleporter, Mover, Networks, Learners, Explorations


file = open('Utils/experiments.sh', 'w')
file.write('#!/bin/sh\n')

features, folders = dict(Defaults.__annotations__), ['', 'Markdown']


def check(params):
    for key, value in params.items():
        if key not in features:
            raise Exception(f'The feature "{key}" does not exist.')
        if value.__class__ != features[key]:
            if value.__class__ == int and features[key] == float:
                params[key] = float(value)
            else:
                if value.__class__.__name__ != features[key].__name__:
                    raise Exception(f'The feature "{key}" should be of type {features[key].__name__}.')
                else:
                    params[key] = value.__name__


def createFolders(name):
    for folder in folders:
        file.write(f"mkdir ../outputs/{name}/{folder}\n")


def genExperiments(name, n=1, **params):
    createFolders(name)
    check(params)
    for i in range(n):
        file.write(f'bsub -o "../outputs/{name}/Markdown/{name}_{i}.md" -J "{name}_{i}" -P "-name {name}-{i} {" ".join(f"-{name} {value}" for name, value in params.items())}" < submit.sh\n')


#genExperiments(f"teleport_short", hours=3.0)
#genExperiments(f"teleport_normal", hours=16)
#genExperiments(f"teleport_gold", hours=16, layer_Gold=True)

#genExperiments(f"gold_small", hours=10.0, width=7, height=7)
#genExperiments(f"gold_medium", hours=10.0, width=9, height=9)
#genExperiments(f"gold_big", hours=10.0, width=11, height=11)
# genExperiments(f"keys_door_small", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True)
# genExperiments(f"holder_putter_small", hours=10.0, width=9, height=9, layer_Holder=True, layer_Putter=True)
# genExperiments(f"keys_door_gold_small", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Gold=True)
# genExperiments(f"holder_putter_gold_small", hours=10.0, width=9, height=9, layer_Holder=True, layer_Putter=True, layer_Gold=True)
# genExperiments(f"9x9_K_100000", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=100000)
# genExperiments(f"9x9_K_500000", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=500000)
# genExperiments(f"9x9_K_100000_epsilon_cap_0.1", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=100000, epsilon_cap=0.1)
# genExperiments(f"9x9_K_500000_epsilon_cap_0.1", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=500000, epsilon_cap=0.1)
# genExperiments(f"9x9_K_100000_epsilon_cap_0", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=100000, epsilon_cap=0)
# genExperiments(f"9x9_K_500000_epsilon_cap_0", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, K=500000, epsilon_cap=0)
# genExperiments(f"maze_size_13_low_rest_chance", hours=10.0, width=13, height=13)
# genExperiments(f"maze_size_15_low_rest_chance", hours=10.0, width=15, height=15)
# genExperiments(f"maze_size_17_low_rest_chance", hours=10.0, width=17, height=17)
# genExperiments(f"maze_size_19_low_rest_chance", hours=10.0, width=19, height=19)
# genExperiments(f"maze_size_13_high_rest_chance", hours=10.0, width=13, height=13, reset_chance = 0.005)
# genExperiments(f"maze_size_15_high_rest_chance", hours=10.0, width=15, height=15, reset_chance = 0.005)
# genExperiments(f"maze_size_17_high_rest_chance", hours=10.0, width=17, height=17, reset_chance = 0.005)
# genExperiments(f"maze_size_19_high_rest_chance", hours=10.0, width=19, height=19, reset_chance = 0.005)
# genExperiments(f"9x9_gamme0.99_eps_intervention", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.99, exploration1=Explorations.epsilonGreedy)
# genExperiments(f"9x9_gamme0.95", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.95)
# genExperiments(f"9x9_gamme0.99", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.99)
# genExperiments(f"9x9_gamme0.995", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.995)
# genExperiments(f"9x9_gamme0.99_softmax0.05", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.95, softmax_cap=0.05)
# genExperiments(f"9x9_gamme0.99_softmax0.05", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.99, softmax_cap=0.05)
# genExperiments(f"9x9_gamme0.995_softmax0.05", hours=10.0, width=9, height=9, layer_Keys=True, layer_Door=True, layer_Holder=True, layer_Putter=True, layer_Gold=True, gamma=0.995, softmax_cap=0.05)
# genExperiments(f"gold_9x9", n=3, hours=24.0, width=9, height=9)
# genExperiments(f"gold_11x11", n=3, hours=24.0, width=11, height=11)
# genExperiments(f"causal1_9x9", n=3, hours=12.0, level=Levels.Causal1, main=teleport)
# genExperiments(f"simul_gold_9x9", n=3, hours=4.0)
# genExperiments(f"Rock_level_hard", hours=11.0, level=Levels.Rocks)
# genExperiments(f"Rock_level_hard_Klow", hours=11.0, level=Levels.Rocks, K=10000)
# genExperiments(f"Rock_level_hard_Khigh", hours=11.0, level=Levels.Rocks, K=1000000)
# genExperiments(f"Rock_level_hard_epshigh", hours=11.0, level=Levels.Rocks, epsilon_cap=0.2)
# genExperiments(f"Rock_level_hard_epslow", hours=11.0, level=Levels.Rocks, epsilon_cap=0)
# genExperiments(f"Rock_level_hard_softhigh", hours=11.0, level=Levels.Rocks, softmax_cap=0.05)
# genExperiments(f"Rock_level_hard_softlow", hours=11.0, level=Levels.Rocks, softmax_cap=0.01)
# genExperiments(f"Rock_level_hard_gammalow", hours=11.0, level=Levels.Rocks, gamma=0.95)
# genExperiments(f"Rock_level_hard_resethigh", hours=11.0, level=Levels.Rocks, reset_chance=0.005)
# genExperiments(f"Rock_level_hard_modresetlow", hours=11.0, level=Levels.Rocks, modified_done_chance=0.02)
# genExperiments(f"Rock_level_hard_misslow", hours=11.0, level=Levels.Rocks, miss_intervention_cost=-0.1)
# genExperiments(f"Rock_level_hard_interventionlow", hours=11.0, level=Levels.Rocks, intervention_cost=-0.1)
# genExperiments(f"causal2_9x9", n=4, hours=10.0, level=Levels.Causal2)
# genExperiments(f"Rock_level_hard_new_parameters", hours=11.0, level=Levels.Rocks)
# genExperiments(f"Rocks_9x9_META_attempt2", n=1, hours=11.0, level=Levels.Rocks)
# genExperiments(f"causal1_9x9_META_attempt2", n=1, hours=11.0, level=Levels.Causal1)
# genExperiments(f"Rocks_9x9_META_attempt2_highK", n=1, hours=11.0, level=Levels.Rocks, K=500000)
# genExperiments(f"causal1_9x9_META_attempt2_highK", n=1, hours=11.0, level=Levels.Causal1, K=500000)
# genExperiments(f"causal2_9x9_META_attempt2", n=1, hours=11.0, level=Levels.Causal2, layer_Diamond1 = True, layer_Diamond2 = True, layer_Diamond3 = True, layer_Diamond4 = True, layer_Dirt = False, layer_Rock = False, layer_Gold = False)
genExperiments(f"test_METAk100000new", n=1, hours=4, level=Levels.Causal1, K=100000)
genExperiments(f"test_METAk500000new", n=1, hours=4, level=Levels.Causal1, K=500000)
genExperiments(f"test_METAk1000000new", n=1, hours=4, level=Levels.Causal1, K=1000000)

file.close()
