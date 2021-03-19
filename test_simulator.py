from main import *
from load import Load
from replaybuffer import ReplayBuffer
import torch

def test_simulator():
    with Load("Agent_Kobo", num=1, isLocal=True) as load:
         with Load("gold_9x9", num=1) as load2:
            env, mover, teleporter = load2.items(Game, Mover, Teleporter)
            simulator, collector = load.items(Simulator, Collector)
            env.layers.levelType = Levels.Maze.value  # Fix
            intervention_idx, modified_board = teleporter.pre_process(env)
            buffer = ReplayBuffer(50000, 50)
            lossboard = 0
            lossRD = 0
            for frame in loop(env, collector, teleporter=teleporter):
                modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
                actions = mover(modified_board)
                observations, rewards, dones, info = env.step(actions)
                modified_board, _, _, teleport_rewards, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
                buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
                board_before, board_after, intervention, _, tele_dones, normal_rewards = buffer.sample_data()
                guessboard, guessRD = simulator.simulate(board_before, intervention)
                guessboard[guessboard > 0.7] = 1
                guessboard[guessboard < 0.7] = 0
                guessRD[guessRD > 0.4] = 1
                guessRD[guessRD < 0.4] = 0
                lossRD += torch.sum((guessRD - torch.cat((normal_rewards.unsqueeze(1), tele_dones.unsqueeze(1)), dim=1))**2).item()
                lossboard += torch.sum((guessboard.reshape(-1, 4, env.layers.height, env.layers.height) - (board_after - board_before)**2)**2).item()
                if frame % 1000 == 0:
                    print(lossboard)
                    print(lossRD)

test_simulator()