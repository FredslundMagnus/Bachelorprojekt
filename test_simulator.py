from main import *
from load import Load
def test_simulator():
    with Load("Agent_Kobo", num=0, isLocal=True) as load:
         with Load("gold_9x9", num=1) as load2:
            env, mover, teleporter = load.items(Game, Mover, Teleporter)
            simulator = load2.items(Simulator, Collector)
            env.layers.levelType = Levels.Maze.value  # Fix
            intervention_idx, modified_board = teleporter.pre_process(env)
            for frame in loop(env, teleporter=teleporter):
                modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
                actions = mover(modified_board)
                observations, rewards, dones, info = env.step(actions)
                modified_board, _, _, _, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
test_simulator()