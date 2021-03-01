from game import Game
from agent import Teleport_intervention, Mover, Networks, Learners, Explorations
from collector import Collector
from auxillaries import run, loop, person, random
from save import Save


class Defaults:
    name: str = "Agent"
    network1: Networks = Networks.Large
    learner1: Learners = Learners.DoubleQlearn
    network2: Networks = Networks.Mini
    learner2: Learners = Learners.DoubleQlearn
    gamma: float = 0.99
    exploration1: Explorations = Explorations.epsilonGreedy
    exploration2: Explorations = Explorations.epsilonGreedy
    K: float = 10**5
    batch: int = 100
    hours: float = 12.0
    width: int = 9
    height: int = 9
    update: int = 1000


def main(defaults):
    collector = Collector()
    env = Game(**defaults)
    mover = Mover(env, **defaults)
    # teleporter = Teleport_intervention(env, **defaults)

    with Save(collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            # modified_board, intervention = teleporter(env.board)
            actions = mover(env.board)  # mover(modified_board)
            observations, rewards, dones = env.step(actions)
            # modified_observations, modified_rewards, modified_dones = teleporter.modify(observations)
            mover.learn(observations, actions, rewards, dones)  # mover.learn(modified_observations, actions, modified_rewards, modified_dones)
            # teleporter.learn(observations, intervention, rewards, dones)
            collector.collect(actions)


run(Defaults, main)
