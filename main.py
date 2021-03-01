from game import Game
from agent import Teleport_intervention, Mover, Networks, Learners
from collector import Collector
from auxillaries import run, loop, person, random


class Defaults:
    name: str = "Agent"
    network1: Networks = Networks.Small
    learner1: Learners = Learners.Qlearn
    network2: Networks = Networks.Small
    learner2: Learners = Learners.Qlearn
    gamma: float = 0.99
    batch: int = 100
    hours: float = 12.0
    width: int = 15
    height: int = 15


def main(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    for frame in loop(env, collector):
        actions = mover(env.board)
        observations, rewards, dones = env.step(actions)
        mover.learn(observations, actions, rewards, dones)
        collector.collect(actions)


run(Defaults, main)
