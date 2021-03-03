from game import Game
from agent import Teleport_intervention, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save
from helper import function


def teleport(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)
    teleporter = Teleport_intervention(env, **defaults)

    with Save(collector, mover, teleporter, **defaults) as save:
        for frame in loop(env, collector, save):
            modified_board, intervention = teleporter(env.board)
            actions = mover(modified_board)
            observations, rewards, dones = env.step(actions)
            modified_observations, modified_rewards, modified_dones = teleporter.modify(intervention, observations, rewards, dones)
            mover.learn(modified_observations, actions, modified_rewards, modified_dones)
            teleporter.learn(observations, intervention, rewards, dones)
            collector.collect(rewards, dones)


def simple(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    with Save(collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            actions = mover(env.board)
            observations, rewards, dones = env.step(actions)
            mover.learn(observations, actions, rewards, dones)
            collector.collect(rewards, dones)


class Defaults:
    name: str = "Agent"
    network1: Networks = Networks.Teleporter
    network2: Networks = Networks.Mini
    learner1: Learners = Learners.Qlearn
    learner2: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.epsilonGreedy
    exploration2: Explorations = Explorations.epsilonGreedy
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
