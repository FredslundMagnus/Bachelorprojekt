from main import *
from load import Load
from replaybuffer import ReplayBuffer
import torch
import matplotlib.pyplot as plt

def test_simulator():
    with Load("Agent_Kobo", num=1, isLocal=True) as load:
         with Load("gold_9x9", num=1) as load2:
            env, mover, teleporter = load2.items(Game, Mover, Teleporter)
            simulator, collector = load.items(Simulator, Collector)
            env.layers.levelType = Levels.Maze.value  # Fix
            intervention_idx, modified_board = teleporter.pre_process(env)
            buffer = ReplayBuffer(50000, 50)
            lossboard = [[0 for _ in range(20)] for _ in range(len(env.layers.layers))]
            lossRD = [0 for _ in range(20)]
            for i in range(20):
                for frame in loop(env, collector, teleporter=teleporter):
                    modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
                    actions = mover(modified_board)
                    observations, rewards, dones, info = env.step(actions)
                    modified_board, _, _, teleport_rewards, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
                    buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
                    board_before, board_after, intervention, _, tele_dones, normal_rewards = buffer.sample_data()
                    guessboard, guessRD = simulator.simulate(board_before, intervention)
                    guessboard = guessboard[tele_dones == 0]
                    limit = (i+1)/60 + 0.2
                    guessboard[guessboard > limit] = 1
                    guessboard[guessboard < limit] = 0
                    guessRD[guessRD > limit] = 1
                    guessRD[guessRD < limit] = 0
                    lossRD[i] += (torch.sum((guessRD - torch.cat((normal_rewards.unsqueeze(1), tele_dones.unsqueeze(1)), dim=1))**2).item())/(guessRD.shape[0] * 10000)
                    for j in range(len(env.layers.layers)):
                        lossboard[j][i] += torch.sum((guessboard.reshape(-1, 4, env.layers.height, env.layers.height)[:,j] - ((board_after - board_before)[tele_dones == 0]**2)[:,j])**2).item()/(guessboard.shape[0] * 10000)
                    if frame % 10000 == 0:
                        print(i)
                        break
            x_values = [((x+1)/60 + 0.2) for x in list(range(20))]
            for i in range(len(lossboard)):
                print(lossboard[i])
                plt.plot(x_values,lossboard[i])
                plt.show()
            plt.plot(x_values,lossRD)
            plt.show()

test_simulator()