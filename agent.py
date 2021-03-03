from network import Net, Networks
from game import Game
from learner import Learner, Learners
from torch import Tensor
import torch
from typing import List
from abc import ABCMeta, abstractmethod
from exploration import Exploration, Explorations


class Agent(metaclass=ABCMeta):
    def __init__(self, game: Game, network: Networks, learner: Learners, exploration: Explorations, width: int = None, height: int = None, **kwargs) -> None:
        self.height = height
        self.width = width
        self.net = Net(len(game.layers), width, height, network, **kwargs)
        self.learner = Learner(self.net, learner, **kwargs)
        self.exploration = Exploration(exploration, **kwargs)

    @abstractmethod
    def __call__(self, board: Tensor) -> Tensor:
        pass

    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.net.learn()
        self._learn(state_after, action, reward, done)

    @abstractmethod
    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        pass


class Teleport_intervention(Agent):
    def __init__(self, game: Game, network1: Networks = None, learner1: Learners = None, exploration1: Explorations = None, **kwargs) -> None:
        super().__init__(game, network1, learner1, exploration1, **kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        actions = self.exploration.explore(self.values.detach())
        return self.modify_board(actions, board), actions

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)

    def modify_board(self, actions, board):
        intervention_layer = torch.nn.functional.one_hot(actions, self.height * self.width).reshape(actions.shape[0], self.height, self.width).unsqueeze(1)
        modified_board = torch.cat((board, intervention_layer), 1)
        return modified_board
    
    def modify(self, intervention, board, rewards, dones):
        modified_board = self.modify_board(intervention, board)
        modified_rewards = rewards + torch.sum(modified_board[:,0,:,:] * modified_board[:,-1,:,:], (1, 2))
        modified_dones = dones
        return modified_board, modified_rewards, modified_dones





class Mover(Agent):
    def __init__(self, game: Game, network2: Networks = None, learner2: Learners = None, exploration2: Explorations = None, **kwargs) -> None:
        super().__init__(game, network2, learner2, exploration2, **kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        actions = self.exploration.explore(self.values.detach())
        return actions

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)
