from game import Game
from agent import Teleporter, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save
from helper import function
from replaybuffer import ReplayBuffer
import torch
from helper import device


def teleport(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    buffer = ReplayBuffer(**defaults)

    with Save(collector, mover, teleporter, **defaults) as save:
        modified_dones = torch.ones(env.layers.board.shape[0], device=device)
        first_intervention = True
        modified_board = torch.zeros(env.layers.board.shape[0], env.layers.board.shape[1] + 1, env.layers.board.shape[2], env.layers.board.shape[3], device=device)
        for frame in loop(env, collector, save, teleporter):
            intervention_idx = torch.flatten(torch.nonzero(modified_dones.long()))
            if len(intervention_idx) > 0:
                needs_intervention_board = env.board[intervention_idx]
                new_boards, intervention = teleporter(needs_intervention_board)
            for i in range(len(intervention_idx)):
                batch_idx = intervention_idx[i]
                if not first_intervention:
                    # if batch_idx == 0:
                    #    print(teleporter.current_boards[batch_idx].unsqueeze(0), observations[batch_idx].unsqueeze(0), teleporter.current_interventions[batch_idx].unsqueeze(0), my_rewards[batch_idx].unsqueeze(0), dones[batch_idx].unsqueeze(0))
                    # if torch.argmax(teleporter.current_boards[batch_idx][-1]) == teleporter.current_interventions[batch_idx].unsqueeze(0):
                    #    print(teleporter.current_boards[batch_idx].unsqueeze(0), observations[batch_idx].unsqueeze(0), teleporter.current_interventions[batch_idx].unsqueeze(0), my_rewards[batch_idx].unsqueeze(0), dones[batch_idx].unsqueeze(0))
                    buffer.save_data((torch.clone(teleporter.current_boards[batch_idx].unsqueeze(0)), torch.clone(observations[batch_idx].unsqueeze(0)), torch.clone(teleporter.current_interventions[batch_idx].unsqueeze(0)), torch.clone(my_rewards[batch_idx].unsqueeze(0)), torch.clone(dones[batch_idx].unsqueeze(0))))
                teleporter.current_boards[batch_idx] = env.board[batch_idx]
                modified_board[batch_idx] = new_boards[i]
                teleporter.current_interventions[batch_idx] = intervention[i]
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            #print(intervention[0], actions[0], rewards[0], dones[0])
            modified_board, modified_rewards, modified_dones, my_rewards = teleporter.modify(teleporter.current_interventions.to(dtype=int), observations, rewards, dones, info)
            #print(modified_rewards[0], modified_dones[0], my_rewards[0])
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            if frame > 100:
                board_before, board_after, action, tele_rewards, tele_dones = buffer.sample_data(batch=50)
                teleporter(board_before)
                teleporter.learn(board_after, action.long(), tele_rewards, tele_dones)
            #print(rewards[0], dones[0], modified_rewards[0], modified_dones[0], my_rewards[0])
            collector.collect([rewards, modified_rewards, my_rewards], [dones, modified_dones])
            first_intervention = False


def simple(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    with Save(env, collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            actions = mover(env.board)
            observations, rewards, dones, info = env.step(actions)
            mover.learn(observations, actions, rewards, dones)
            collector.collect([rewards], [dones])


class Defaults:
    name: str = "Agent"
    main: function = teleport
    hours: float = 12.0
    batch: int = 100
    width: int = 11
    height: int = 11
    network1: Networks = Networks.Teleporter
    network2: Networks = Networks.Mini
    learner1: Learners = Learners.Qlearn
    learner2: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.softmaxer
    exploration2: Explorations = Explorations.epsilonGreedy

    layer_Blocks: bool = True
    layer_Goal: bool = True
    layer_Gold: bool = False
    layer_Keys: bool = False
    layer_Door: bool = False
    layer_Holder: bool = False
    layer_Putter: bool = False

    K: float = 100000
    epsilon_cap: float = 0.1
    softmax_cap: float = 0.02
    gamma: float = 0.95
    update: int = 10000
    reset_chance: float = 0.005
    modified_done_chance: float = 0.05
    miss_intervention_cost: float = -0.2
    intervention_cost: float = -0.1
    replay_size: int = 50000


run(Defaults)
