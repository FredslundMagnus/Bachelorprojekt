from main import *
from load import Load


def test_simple():
    with Load("causal3_9x9_20hoursONLYMOVERsoftmaxgam0995") as load:
        collector, env, mover = load.items(Collector, Game, Mover)
        for frame in loop(env, collector):
            actions = mover(env.board)
            env.step(actions)


def test_teleport():
    with Load("NOBUGcausal4_teleport", num=0) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.exploration.explore = teleporter.exploration.greedy
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
                print("performance is " + str((all_rewards/all_dones).item()))

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
    with Load("NOBUGcausal3_CFagent_convert1", num=0) as load:
        collector, env, mover, teleporter, CFagent = load.items(Collector, Game, Mover, Teleporter, CFAgent)
        teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        dones = CFagent.pre_process(env)
        for frame in loop(env, collector, teleporter=teleporter):
            CFagent.counterfact(env, dones, teleporter)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)

test_CFagent()
