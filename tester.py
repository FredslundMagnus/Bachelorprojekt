from main import *
from load import Load


def test_simple():
    with Load("Agent") as load:
        collector, env, mover = load.items(Collector, Game, Mover)
        for frame in loop(env, collector):
            actions = mover(env.board)
            env.step(actions)


def test_teleport():
    with Load("Rock_level_hard_softlow", num=0) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, teleporter=teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)


test_teleport()
