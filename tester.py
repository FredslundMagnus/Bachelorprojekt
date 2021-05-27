from numpy.core.fromnumeric import mean, std
from torch import tensor, cat
from allGraphs import getInterventions, states, transform, transformNot, environments, Data
from layer import LayerType
from typing import List
from main import *
from load import Load
from helper import device
import torch
import sys
import numpy as np

def test_simple():
    with Load("causal3_9x9_20hoursONLYMOVERsoftmaxgam0995") as load:
        collector, env, mover = load.items(Collector, Game, Mover)
        for frame in loop(env, collector):
            actions = mover(env.board)
            env.step(actions)


def test_teleport(name="Diamonds2_convert4", num=0):
    with Load(name, num=num) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        #teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        all_rewards = 0
        all_dones = 0
        for frame in loop(env, collector, teleporter=teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            all_rewards += sum(rewards)
            all_dones += sum(dones)
            if frame % 1000 == 0:
                print("performance is " + str((all_rewards/all_dones).item()), file=sys.stderr)
                return (all_rewards/all_dones).item()
                # print("performance is " + str((all_rewards/all_dones).item()), file=sys.stderr)


def test_metateleport():
    with Load("causal3_9x9", num=0) as load:
        collector, env, mover, teleporter1, teleporter2 = load.items(Collector, Game, Mover, Teleporter, MetaTeleporter)
        teleporter1.exploration.explore = teleporter1.exploration.greedy
        teleporter2.exploration.explore = teleporter2.exploration.greedy
        intervention_idx2, modified_board2 = teleporter2.pre_process(env)
        intervention_idx1, _ = teleporter1.pre_process(env)
        for frame in loop(env, collector, teleporter1, teleporter2):
            modified_board2 = teleporter2.interveen(env.board, intervention_idx2, modified_board2)
            modified_board1 = teleporter1.interveen(env.board, intervention_idx1, modified_board2)
            actions = mover(modified_board1)
            observations, rewards, dones, info = env.step(actions)
            modified_board1, modified_board2, _, _, _, _, _, intervention_idx1, intervention_idx2 = teleporter2.metamodify(observations, rewards, dones, info, teleporter1.interventions)


def test_CFagent():
    with Load("Causal3_Conver2", num=0) as load:
        collector, env, mover, teleporter, CFagent = load.items(Collector, Game, Mover, Teleporter, CFAgent)
        teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        dones = CFagent.pre_process(env)
        CF_dones, cfs = torch.flatten(torch.nonzero(torch.ones(env.layers.board.shape[0], device=device).long())), 1
        for frame in loop(env, collector, teleporter=teleporter):
            CFagent.counterfact(env, dones, teleporter, CF_dones, cfs)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            CF_dones, cfs = CFagent.counterfact_check(dones, env, check=0)


def test_graphTrain():
    with Load("causal2_online_var_0.5_full_UCB1", num=0) as load:
        collector, env, mover, data = load.items(Collector, Game, Mover, Data)
        # data.graphMode = GraphMode.var  # Fix
        layers: List[LayerType] = environments[env.level][2]
        teleporter = Teleporter(env, network1=Networks.Teleporter, K1=5000000, learner1=Learners.Qlearn, exploration1=Explorations.softmaxer, gamma1=0.98, batch=env.layers.batch, width=env.layers.width, height=env.layers.height)
        convert = [env.layers.types.index(layer) for layer in layers]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        old_states = [state for state in states(env.board, convert, layers)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        eatCheese, interventions = ([True] * env.batch, [None] * env.batch)
        for frame in loop(env, collector, teleporter=teleporter):
            new_states = [state for state in states(env.board, convert, layers)]
            transform(old_states, new_states, dones, rewards, data, layers)
            transformNot(env.board, new_states, player, goal, convert, data, layers)
            stateChanged = [old != new for old, new in zip(old_states, new_states)]
            shouldInterviene = [cond1 or cond2 for cond1, cond2 in zip(stateChanged, eatCheese)]
            exploration = 0
            interventions = [(getInterventions(env, state, data, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
            modification = env.board[tensor(interventions)].unsqueeze(1)
            teleporter.interventions = tensor([m.flatten().argmax().item() for m in list(modification)], device=device)
            modified_board = cat((env.board, modification), dim=1)
            actions = mover(modified_board)
            _, rewards, dones, _ = env.step(actions)
            playerPositions = [(t := env.layers.dict[LayerType.Player].positions[i][0])[1] * env.layers.width + t[0] for i in range(env.batch)]
            eatCheese = [intervention == player_pos for intervention, player_pos in zip(teleporter.interventions, playerPositions)]
            old_states = new_states


def test_CFagent2():
    with Load("ReTest6", num=0) as load:
        mover, teleporter, collector, env, CFagent, simulator = load.items(Mover, Teleporter, Collector, Game, CFAgent, Simulator)
        teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        dones = CFagent.pre_process(env)
        CF_dones, cfs = torch.flatten(torch.nonzero(torch.ones(env.layers.board.shape[0], device=device).long())), 1
        for frame in loop(env, collector, teleporter=teleporter):
            CFagent.counterfact2(env, dones, teleporter, simulator, CF_dones, cfs)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            CF_dones, cfs = CFagent.counterfact_check(dones, env, check=0)


def test_option_critic():
    with Load("Attempt2_Rocks_option_critic", num=0) as load:
        env, collector = load.items(Game, Collector)
        collector.show(env)

test_teleport()
# Tests = [('Causal3_Conver1','Lights1_f1'), ('Causal3_Conver2','Lights1_f2'), ('Causal3_Conver4_3counterfactsNOCRASH_2', 'Lights1_f3'), ('Lights1_teleport', 'Lights1_tele'),
#          ('Maze_Conver1', 'Maze_f1'), ('Maze_Conver2', 'Maze_f2'), ('Maze_Conver4_3counterfactsNOCRASH_2', 'Maze_f3'), ('Maze_teleport', 'Maze_tele'),
#          ('Coconuts_Conver1', 'Coconuts_f1'), ('Coconuts_Conver2', 'Coconuts_f2'), ('Coconuts_Conver4_3counterfactsNOCRASH_2', 'Coconuts_f3'), ('Coconuts_teleport', 'Coconuts_tele'),
#          ('Causal4_Conver1', 'Lights2_f1'), ('Causal4_Conver2', 'Lights2_f2'), ('Causal4_Conver4_3counterfacts_2', 'Lights2_f3'), ('Lights2_teleport', 'Lights2_tele'),
#          ('MonsterLevel_Conver1', 'Monsters_f1'), ('MonsterLevel_Conver2', 'Monsters_f2'), ('MonsterLevel_Conver4_3counterfactsNOCRASH_2', 'Monsters_f3'), ('Monsters_teleport', 'Monsters_tele')]

# for test, name in Tests:
#     disablePrint()
#     performance = [None, None, None]
#     for i in range(len(performance)):
#         performance[i] = test_teleport(name=test, num=i)
#     enablePrint()
#     print(name)
#     print('$' + str(round(mean(performance),2)) + ' \pm ' + str(round(1.96 * std(performance)/np.sqrt(len(performance)),2)) + '$')
