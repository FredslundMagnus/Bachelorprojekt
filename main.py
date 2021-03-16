from game import Game
from agent import Teleporter, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save
from helper import function
from replaybuffer import ReplayBuffer


def teleport(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    buffer = ReplayBuffer(**defaults)

    with Save(env, collector, mover, teleporter, **defaults) as save:
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, save, teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones = buffer.sample_data()
            teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])


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
    hours: float = 0.15
    batch: int = 100
    width: int = 9
    height: int = 9
    network1: Networks = Networks.Teleporter
    network2: Networks = Networks.Mini
    learner1: Learners = Learners.Qlearn
    learner2: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.softmaxer
    exploration2: Explorations = Explorations.epsilonGreedy

    layer_Blocks: bool = True
    layer_Goal: bool = True
    layer_Gold: bool = True
    layer_Keys: bool = False
    layer_Door: bool = False
    layer_Holder: bool = False
    layer_Putter: bool = False
    layer_Rock: bool = False
    layer_Dirt: bool = False

    K: float = 200000
    epsilon_cap: float = 0.2
    softmax_cap: float = 0.03
    gamma: float = 0.98
    update: int = 10000
    reset_chance: float = 0.002
    modified_done_chance: float = 0.05
    miss_intervention_cost: float = -0.2
    intervention_cost: float = -0.05
    replay_size: int = 50000
    sample_size: int = 50


run(Defaults)
