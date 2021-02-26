from game import Game
from agent import Agent, Networks
from collector import Collector
from auxillaries import loop, person, random

collector = Collector()
env = Game()
agent = Agent(env, Networks.Small)


for frame in loop(env, collector):
    env.step(agent(env))
    # agent.learn()
