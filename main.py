import sys
from game import Game
from agent import Agent, Networks, Learners
from collector import Collector
from auxillaries import run, loop, person, random


class Defaults:
    name: str = "Agent"
    network: Networks = Networks.Small
    learner: Learners = Learners.Qlearn
    gamma: float = 0.99
    batch: int = 100
    hours: float = 12.0
    width: int = 15
    height: int = 15


def main(defaults):
    collector = Collector()
    env = Game(**defaults)
    agent = Agent(env, **defaults)

    for frame in loop(env, collector):
        actions = agent(env)
        observations, rewards, dones = env.step(actions)
        agent.learn(observations, actions, rewards, dones)
        collector.collect(actions)


run(Defaults, main)
