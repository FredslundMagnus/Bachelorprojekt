from network import Net, Networks
from game import Game
from learner import Learner, Learners
from torch import Tensor, random
import torch
from typing import List
from abc import ABCMeta, abstractmethod
from exploration import Exploration, Explorations
import torch
from helper import device


class Agent(metaclass=ABCMeta):
    def __init__(self, game: Game, network: Networks, learner: Learners, exploration: Explorations, width: int = None, height: int = None, batch: int = None, _extra_dim: int = 0, **kwargs) -> None:
        self.batch = batch
        self.height = height
        self.width = width
        self.net = Net(len(game.layers) + _extra_dim, width, height, network, **kwargs)
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


class Teleporter(Agent):
    def __init__(self, game: Game, network1: Networks = None, learner1: Learners = None, exploration1: Explorations = None, modified_done_chance: float = None, miss_intervention_cost: float = None, intervention_cost: float = None, **kwargs) -> None:
        super().__init__(game, network1, learner1, exploration1, **kwargs)
        self.current_boards = [None] * self.batch
        self.current_interventions = torch.zeros(self.batch, device=device)
        self.modified_done_chance = modified_done_chance
        self.miss_intervention_cost = miss_intervention_cost
        self.intervention_cost = intervention_cost
        self.counter = 0

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

    def modify(self, intervention, board, rewards, dones, info):
        modified_board = self.modify_board(intervention, board)
        modified_rewards = torch.sum(modified_board[:, 0] * modified_board[:, -1], (1, 2)) * (1 - rewards)
        for i in range(len(info)):
            if 'player_end' in info[i]:
                modified_rewards[i] += modified_board[i, -1][(info[i]['player_end'][1], info[i]['player_end'][0])]

        modified_dones = torch.clone(modified_rewards)
        modified_dones[dones == 1] = 1
        rands = torch.rand(len(modified_rewards))
        modified_dones[rands < self.modified_done_chance] = 1
        tele_rewards = self.miss_intervention_cost * torch.clone(modified_dones)
        tele_rewards[modified_rewards == 1] = self.intervention_cost
        tele_rewards[rewards == 1] = 1
        intervention_idx = torch.flatten(torch.nonzero(modified_dones.long()))
        return modified_board, modified_rewards, modified_dones, tele_rewards, intervention_idx

    def interveen(self, board, intervention_idx, modified_board):
        if len(intervention_idx) > 0:
            needs_intervention_board = board[intervention_idx]
            new_boards, intervention = self(needs_intervention_board)
        for i in range(len(intervention_idx)):
            batch_idx = intervention_idx[i]
            self.current_boards[batch_idx] = board[batch_idx]
            modified_board[batch_idx] = new_boards[i]
            self.current_interventions[batch_idx] = intervention[i]
        return modified_board

    def pre_process(self, env):
        return torch.flatten(torch.nonzero(torch.ones(env.layers.board.shape[0], device=device).long())), torch.zeros(env.layers.board.shape[0], env.layers.board.shape[1] + 1, env.layers.board.shape[2], env.layers.board.shape[3], device=device)


class Mover(Agent):
    def __init__(self, game: Game, network2: Networks = None, learner2: Learners = None, exploration2: Explorations = None, **kwargs) -> None:
        super().__init__(game, network2, learner2, exploration2, **kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        actions = self.exploration.explore(self.values.detach())
        return actions

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.learner.learn(self.values, state_after, action, reward, done)
