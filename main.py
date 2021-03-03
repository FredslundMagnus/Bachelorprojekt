from torch import long
from game import Game
from agent import Teleport_intervention, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save
from helper import function
from replay_buffer import replay_buffer
import torch
from helper import device


def teleport(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleport_intervention(env, **defaults)
    buffer = replay_buffer(size=10000)

    with Save(collector, mover, teleporter, **defaults) as save:
        modified_dones = torch.ones(env.layers.board.shape[0], device=device)
        first_intervention = True
        modified_board = torch.zeros(env.layers.board.shape[0], env.layers.board.shape[1] + 1, env.layers.board.shape[2], env.layers.board.shape[3], device=device)
        for frame in loop(env, collector, save):
            intervention_idx = torch.flatten(torch.nonzero(modified_dones.long()))
            if len(intervention_idx) > 0:
                needs_intervention_board = env.board[intervention_idx]
                new_boards, intervention = teleporter(needs_intervention_board)
            for i in range(len(intervention_idx)):
                batch_idx = intervention_idx[i]
                if not first_intervention:
                    buffer.save_data((teleporter.current_boards[batch_idx].unsqueeze(0), observations[batch_idx].unsqueeze(0), teleporter.current_interventions[batch_idx].unsqueeze(0), rewards[batch_idx].unsqueeze(0), dones[batch_idx].unsqueeze(0)))
                teleporter.current_boards[batch_idx] = env.board[batch_idx]
                modified_board[batch_idx] = new_boards[i]
                teleporter.current_interventions[batch_idx] = intervention[i]
            actions = mover(modified_board)

            observations, rewards, dones = env.step(actions)
            modified_board, modified_rewards, modified_dones = teleporter.modify(teleporter.current_interventions.to(dtype=int), observations, rewards, dones)

            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            if frame > 100:
                board_before, board_after, action, tele_rewards, tele_dones = buffer.sample_data(batch=100)
                teleporter(board_before)
                teleporter.learn(board_after, action.long(), tele_rewards, tele_dones)
            collector.collect(rewards, dones, modified_rewards, modified_dones)
            first_intervention = False


def simple(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    with Save(env, collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            actions = mover(env.board)
            observations, rewards, dones = env.step(actions)
            mover.learn(observations, actions, rewards, dones)
            collector.collect(rewards, dones, rewards, dones)


class Defaults:
    name: str = "Agent"
    network1: Networks = Networks.Teleporter
    network2: Networks = Networks.Teleporter
    learner1: Learners = Learners.Qlearn
    learner2: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.epsilonGreedy
    exploration2: Explorations = Explorations.epsilonGreedy
    replay_buffer: replay_buffer = replay_buffer
    gamma: float = 0.95
    K: float = 500000
    batch: int = 100
    hours: float = 12.0
    width: int = 11
    height: int = 11
    update: int = 1000
    reset_chance: float = 0.002
    main: function = teleport


run(Defaults)
