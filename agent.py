from network import Net, Networks
from game import Game
from learner import Learner, Learners
from torch import Tensor
import torch
from typing import List


class Agent:
    def __init__(self, game: Game, network: Networks = Networks.Small, learner: Learners = Learners.DoubleQlearn) -> None:
        self.net = Net(len(game.layers), network)
        self.learner = Learner(self.net, learner)

    def __call__(self, game: Game) -> Tensor:
        temp: Tensor = self.net.network(game.board)
        self.values, actions = torch.max(temp, dim=1)
        return actions

    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)
