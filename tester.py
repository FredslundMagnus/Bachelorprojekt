from main import *
from load import Load


def test_simple():
    with Load("Agent") as load:
        collector, env, mover = load.items(Collector, Game, Mover)
        for frame in loop(env, collector):
            actions = mover(env.board)
            env.step(actions)


def test_teleport():
    with Load("Rocks_9x9_META_attempt2_highK", num=0) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        teleporter.extradim = 0
        teleporter.exploration.explore = teleporter.exploration.greedy
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, teleporter=teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, _, intervention_idx = teleporter.modify(observations, rewards, dones, info)

def test_metateleport():
    with Load("causal1_9x9_META_attempt2_highK", num=0) as load:
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


test_teleport()
