from main import *
from load import Load


def test_simple():
    with Load("Agent") as load:
        collector, env, mover = load.items(Collector, Game, Mover)
        for frame in loop(env, collector):
            actions = mover(env.board)
            env.step(actions)


def test_teleport():
    with Load("9x9_gamme0.995_softmax0.05") as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, teleporter=teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)


test_teleport()
