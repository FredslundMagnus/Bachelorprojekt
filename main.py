# https://github.com/lweitkamp/option-critic-pytorch/blob/master/main.py
# https://github.com/lweitkamp/option-critic-pytorch/blob/master/option_critic.py

from Utils.debug import disablePrint, enablePrint
from allGraphs import GraphMode
from game import Game, Levels
from agent import Teleporter, Mover, Networks, Learners, Explorations, MetaTeleporter, CFAgent
from collector import Collector
from auxillaries import run, loop, player, random, Save
from helper import function
from replaybuffer import ReplayBuffer, CFReplayBuffer, SimBuffer
from simulator import Simulator
from load import Load
from allGraphsTrain import graphTrain
from optionCritic import option_critic_run


def metateleport(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter1 = Teleporter(env, _extra_dim=1, **defaults)
    teleporter2 = MetaTeleporter(env, **defaults)
    buffer1 = ReplayBuffer(**defaults)
    buffer2 = ReplayBuffer(**defaults)

    with Save(env, collector, mover, teleporter1, teleporter2, **defaults) as save:
        intervention_idx2, modified_board2 = teleporter2.pre_process(env)
        intervention_idx1, _ = teleporter1.pre_process(env)
        for frame in loop(env, collector, save, teleporter1, teleporter2):
            modified_board2 = teleporter2.interveen(env.board, intervention_idx2, modified_board2)
            modified_board1 = teleporter1.interveen(env.board, intervention_idx1, modified_board2)
            actions = mover(modified_board1)
            observations, rewards, dones, info = env.step(actions)
            modified_board1, modified_board2, modified_rewards1, modified_rewards2, modified_dones1, modified_dones2, tele_rewards, intervention_idx1, intervention_idx2 = teleporter2.metamodify(observations, rewards, dones, info, teleporter1.interventions)
            buffer1.teleporter_save_data(teleporter1.boards, modified_board2, teleporter1.interventions, modified_rewards2, modified_dones2, intervention_idx1)
            buffer2.teleporter_save_data(teleporter2.boards, observations, teleporter2.interventions, tele_rewards, dones, intervention_idx2)
            mover.learn(modified_board1, actions, modified_rewards1, modified_dones1)
            board_before, board_after, intervention, tel_rewards, tele_dones = buffer1.sample_data()
            teleporter1.learn(board_after, intervention, tel_rewards, tele_dones, board_before)
            board_before, board_after, intervention, tel_rewards, tele_dones = buffer2.sample_data()
            teleporter2.learn(board_after, intervention, tel_rewards, tele_dones, board_before)
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
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones = buffer.sample_data()
            teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])


def simple(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    with Save(env, collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            actions = mover(env.board)
            observations, rewards, dones, info = env.step(actions)
            mover.learn(observations, actions, rewards, dones)
            collector.collect([rewards], [dones])


def CFagent(defaults):
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    buffer = ReplayBuffer(**defaults)
    CFagent = CFAgent(env, **defaults)
    CFbuffer = CFReplayBuffer(**defaults)
    collector = Collector(**defaults)

    with Save(env, collector, mover, teleporter, CFagent, **defaults) as save:
        intervention_idx, modified_board = teleporter.pre_process(env)
        dones = CFagent.pre_process(env)
        CF_dones, cfs = None, None
        for frame in loop(env, collector, save, teleporter):
            CFagent.counterfact(env, dones, teleporter, CF_dones, cfs)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones = buffer.sample_data()
            teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
            CF_dones, cfs = CFagent.counterfact_check(dones, env, **defaults)
            CFbuffer.CF_save_data(CFagent.boards, observations, CFagent.counterfactuals, rewards, dones, CF_dones)
            CFboard, CFobs, cf, CFrewards, CFdones1 = CFbuffer.sample_data()
            CFagent.learn(CFobs, cf, CFrewards, CFdones1, CFboard)

def Load_Cfagent(defaults):
    with Load(defaults["load_name"], num=defaults['num']) as load:
        collector, env, mover, teleporter, CFagent = load.items(Collector, Game, Mover, Teleporter, CFAgent)
        buffer = ReplayBuffer(**defaults)
        CFbuffer = CFReplayBuffer(**defaults)

        with Save(env, collector, mover, teleporter, CFagent, **defaults) as save:
            intervention_idx, modified_board = teleporter.pre_process(env)
            dones = CFagent.pre_process(env)
            CF_dones, cfs = None, None
            CFagent.CF_count = 0
            for frame in loop(env, collector, save, teleporter):
                CFagent.counterfact(env, dones, teleporter, CF_dones, cfs)
                modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
                actions = mover(modified_board)
                observations, rewards, dones, info = env.step(actions)
                modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
                buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
                mover.learn(modified_board, actions, modified_rewards, modified_dones)
                board_before, board_after, intervention, tele_rewards, tele_dones = buffer.sample_data()
                teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
                collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
                CF_dones, cfs = CFagent.counterfact_check(dones, env, **defaults)
                CFbuffer.CF_save_data(CFagent.boards, observations, CFagent.counterfactuals, rewards, dones, CF_dones)
                CFboard, CFobs, cf, CFrewards, CFdones1 = CFbuffer.sample_data()
                CFagent.learn(CFobs, cf, CFrewards, CFdones1, CFboard)


def CFagentv2(defaults):
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    buffer = ReplayBuffer(**defaults)
    CFagent = CFAgent(env, **defaults)
    CFbuffer = CFReplayBuffer(**defaults)
    simulator = Simulator(env, **defaults)
    simbuffer = SimBuffer(**defaults)
    collector = Collector(**defaults)

    with Save(env, collector, mover, teleporter, CFagent, simulator, **defaults) as save:
        intervention_idx, modified_board = teleporter.pre_process(env)
        dones = CFagent.pre_process(env)
        CF_dones, cfs = None, None
        for frame in loop(env, collector, save, teleporter):
            CFagent.counterfact2(env, dones, teleporter, simulator, CF_dones, cfs)
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones = buffer.sample_data()
            teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            simbuffer.simulator_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx)
            board_before, board_after, intervention = simbuffer.sample_data()
            lossboard = simulator.learn(board_before, board_after, intervention)
            collector.collect_loss(lossboard)
            collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
            CF_dones, cfs = CFagent.counterfact_check(dones, env, **defaults)
            CFbuffer.CF_save_data(CFagent.boards, observations, CFagent.counterfactuals, rewards, dones, CF_dones)
            CFboard, CFobs, cf, CFrewards, CFdones1 = CFbuffer.sample_data()
            CFagent.learn(CFobs, cf, CFrewards, CFdones1, CFboard)


class Defaults:
    name: str = "Agent"
    main: function = graphTrain
    level: Levels = Levels.Causal2
    failed_actions_chance: float = 0
    use_model: bool = False
    depth: int = 3
    model_explore: int = 100000
    samples: int = 5
    hours: float = 12
    batch: int = 100
    width: int = 9
    height: int = 9

    graphMode: GraphMode = GraphMode.UCB1

    network1: Networks = Networks.Teleporter
    K1: float = 5000000
    learner1: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.softmaxer
    gamma1: float = 0.98

    network2: Networks = Networks.Mini
    K2: float = 1000000
    learner2: Learners = Learners.Qlearn
    exploration2: Explorations = Explorations.epsilonGreedy
    gamma2: float = 0.95

    layer_Blocks: bool = True
    layer_Goal: bool = True
    layer_Gold: bool = True
    layer_Keys: bool = True
    layer_Door: bool = True
    layer_Holder: bool = True
    layer_Putter: bool = True

    layer_Rock: bool = True
    layer_Dirt: bool = True

    layer_Diamond1: bool = True
    layer_Diamond2: bool = True
    layer_Diamond3: bool = True
    layer_Diamond4: bool = True

    layer_Reddoor: bool = True
    layer_Redkeys: bool = True
    layer_Bluedoor: bool = True
    layer_Bluekeys: bool = True

    layer_Pink1: bool = True
    layer_Pink2: bool = True
    layer_Pink3: bool = True
    layer_Brown1: bool = True
    layer_Brown2: bool = True
    layer_Brown3: bool = True

    layer_Greendown: bool = True
    layer_Greenup: bool = True
    layer_Greenstar: bool = True
    layer_Yellowstar: bool = True
    layer_Bluestar: bool = True

    layer_Coconut: bool = True

    layer_Monster: bool = True

    layer_Greencross: bool = True
    layer_Bluecross: bool = True
    layer_Redcross: bool = True
    layer_Purplecross: bool = True
    layer_Super1: bool = True
    layer_Super2: bool = True
    layer_Super3: bool = True
    layer_Super4: bool = True
    layer_Super5: bool = True
    layer_Super6: bool = True
    layer_Super7: bool = True

    epsilon_cap: float = 0.2
    softmax_cap: float = 0.02
    update: int = 10000
    reset_chance: float = 0.002
    modified_done_chance: float = 0.05
    miss_intervention_cost: float = -0.15
    intervention_cost: float = -0.05
    replay_size: int = 100000
    sample_size: int = 50
    CF_convert: int = 3
    Counterfacts: int = 1
    TopN: int = 6
    Random_counterfacts: bool = False
    num: int = 0
    load_name: str = "Causal4_Conver4_3counterfacts"


run(Defaults)
