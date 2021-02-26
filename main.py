from game import Game
from agent import Agent, Networks, Learners
from collector import Collector
from auxillaries import loop, person, random

collector = Collector()
env = Game()
agent = Agent(env, Networks.Small, Learners.Qlearn)


for frame in loop(env, collector):
    actions = agent(env)
    observations, rewards, dones = env.step(actions)
    agent.learn(observations, actions, rewards, dones)
    collector.collect(actions)
