from network import Net, Networks
from game import Game
from learner import Learner, Learners
from torch import Tensor
import torch


class Agent:
    def __init__(self, game: Game, network: Networks = Networks.Small, learner: Learners = Learners.DoubleQlearn) -> None:
        self.net = Net(len(game.layers), network)
        self.learner = Learner(self.net, learner)

    def __call__(self, game: Game):
        values = self.net.network(game.board)
        actions = torch.argmax(values, dim=1)
        return actions.tolist()

    def learn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(value_before, state_after, action, reward, done)
