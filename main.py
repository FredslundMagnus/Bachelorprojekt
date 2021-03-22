from game import Game
from agent import Teleporter, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save
from helper import function
from replaybuffer import ReplayBuffer
from levels import Levels
from simulator import Simulator
from load import Load

def metateleport(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter1 = Teleporter(env, _extra_dim=1, **defaults)
    teleporter2 = Teleporter(env, **defaults)
    buffer1 = ReplayBuffer(**defaults)
    buffer2 = ReplayBuffer(**defaults)

    with Save(env, collector, mover, teleporter1, teleporter2, **defaults) as save:
        intervention_idx2, modified_board2 = teleporter2.pre_process(env)
        intervention_idx1, _ = teleporter1.pre_process(env)
        for frame in loop(env, collector, save, teleporter1):
            modified_board2 = teleporter2.interveen(env.board, intervention_idx2, modified_board2)
            modified_board1 = teleporter1.interveen(env.board, intervention_idx1, modified_board2)
            actions = mover(modified_board1)
            observations, rewards, dones, info = env.step(actions)
            modified_board1, modified_board2, modified_rewards1, modified_rewards2, modified_dones1, modified_dones2, tele_rewards, intervention_idx1, intervention_idx2 = teleporter2.metamodify(observations, rewards, dones, info, teleporter1.interventions)
            buffer1.teleporter_save_data(teleporter1.boards, modified_board2, teleporter1.interventions, modified_rewards2, dones, intervention_idx1, rewards)
            buffer2.teleporter_save_data(teleporter2.boards, observations, teleporter2.interventions, tele_rewards, dones, intervention_idx2, rewards)
            mover.learn(modified_board1, actions, modified_rewards1, modified_dones1)
            board_before, board_after, intervention, tele_rewards, tele_dones, normal_rewards = buffer1.sample_data()
            teleporter1.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            board_before, board_after, intervention, tele_rewards, tele_dones, normal_rewards = buffer2.sample_data()
            teleporter2.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            collector.collect([rewards, modified_rewards1, modified_rewards2, tele_rewards], [dones, modified_dones1, modified_dones2])




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
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones, normal_rewards = buffer.sample_data()
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


def simulation(defaults):
    with Load("gold_9x9", num=1) as load:
        env, mover, teleporter = load.items(Game, Mover, Teleporter)
        env.hours = 4
        teleporter.modified_done_chance = 0
        simulator = Simulator(env, env.layers.width, env.layers.height)
        env.layers.levelType = Levels.Maze.value  # Fix
        intervention_idx, modified_board = teleporter.pre_process(env)
        buffer = ReplayBuffer(**defaults)
        collector = Collector(**defaults)
        with Save(env, collector, simulator, **defaults) as save:
            for frame in loop(env, collector, save, teleporter=teleporter):
                modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
                actions = mover(modified_board)
                observations, rewards, dones, info = env.step(actions)
                modified_board, _, _, teleport_rewards, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
                buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
                board_before, board_after, intervention, _, tele_dones, normal_rewards = buffer.sample_data()
                lossboard, lossRD = simulator.learn(board_before, board_after, intervention, normal_rewards, tele_dones)
                collector.collect_loss(lossboard, lossRD)


class Defaults:
    name: str = "Agent"
    main: function = metateleport
    level: Levels = Levels.Rocks
    hours: float = 12
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
    layer_Gold: bool = False
    layer_Keys: bool = False
    layer_Door: bool = False
    layer_Holder: bool = False
    layer_Putter: bool = False
    layer_Rock: bool = True
    layer_Dirt: bool = True
    layer_Diamond1: bool = True
    layer_Diamond2: bool = True
    layer_Diamond3: bool = True
    layer_Diamond4: bool = True

    K: float = 200000
    epsilon_cap: float = 0.1
    softmax_cap: float = 0.02 # 0.025
    gamma: float = 0.98
    update: int = 10000
    reset_chance: float = 0.002
    modified_done_chance: float = 0.05 # 0.04
    miss_intervention_cost: float = -0.2 # -0.15
    intervention_cost: float = -0.05
    replay_size: int = 100000
    sample_size: int = 50


run(Defaults)
