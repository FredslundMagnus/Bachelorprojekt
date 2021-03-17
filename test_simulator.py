from main import *
from load import Load
from simulator import Simulator
from replaybuffer import ReplayBuffer

def test_simul():
    with Load("gold_9x9", num=1) as load:
        collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
        simulator = Simulator(env, env.layers.width, env.layers.height)
        env.layers.levelType = Levels.Maze.value  # Fix
        intervention_idx, modified_board = teleporter.pre_process(env)
        buffer = ReplayBuffer(50000, 50)
        for frame in loop(env, collector, teleporter=teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, _, _, teleport_rewards, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
            board_before, board_after, intervention, _, tele_dones, normal_rewards = buffer.sample_data()
            simulator.learn(board_before, board_after, intervention, normal_rewards, tele_dones)


test_simul()
