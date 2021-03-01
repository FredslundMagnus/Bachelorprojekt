from network import Net, Networks
from game import Game
from learner import Learner, Learners
from torch import Tensor
import torch
from typing import List
from abc import ABCMeta, abstractmethod


class Agent(metaclass=ABCMeta):
    def __init__(self, game: Game, network: Networks, learner: Learners, kwargs) -> None:
        self.net = Net(len(game.layers), network)
        self.learner = Learner(self.net, learner, kwargs)

    @abstractmethod
    def __call__(self, board: Tensor) -> Tensor:
        pass

    @abstractmethod
    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        pass


class Teleport_intervention(Agent):
    def __init__(self, game: Game, network1: Networks = None, learner1: Learners = None, **kwargs) -> None:
        super().__init__(game, network1, learner1, kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        temp: Tensor = self.net.network(board)
        self.values, actions = torch.max(temp, dim=1)
        return actions

    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)


class Mover(Agent):
    def __init__(self, game: Game, network2: Networks = None, learner2: Learners = None, **kwargs) -> None:
        super().__init__(game, network2, learner2, kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        temp: Tensor = self.net.network(board)
        self.values, actions = torch.max(temp, dim=1)
        return actions

    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)
