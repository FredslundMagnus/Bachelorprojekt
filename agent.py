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
from torch.nn.functional import softmax
import random


class Agent(metaclass=ABCMeta):
    def __init__(self, game: Game, network: Networks, learner: Learners, exploration: Explorations, gamma: float = None, K: float = None, width: int = None, height: int = None, batch: int = None, _extra_dim: int = 0, **kwargs) -> None:
        self.extradim = _extra_dim
        self.batch = batch
        self.height = height
        self.width = width
        self.net = Net(len(game.layers) + _extra_dim, width, height, network, **kwargs)
        self.learner = Learner(self.net, learner, gamma, **kwargs)
        self.exploration = Exploration(exploration, K, **kwargs)

    @abstractmethod
    def __call__(self, board: Tensor) -> Tensor:
        pass

    def learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor, *args):
        self.net.learn()
        self._learn(state_after, action, reward, done, *args)

    @abstractmethod
    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor, *args):
        pass


class Teleporter(Agent):
    def __init__(self, game: Game, network1: Networks = None, learner1: Learners = None, exploration1: Explorations = None, gamma1: float = None, K1 : float = None, modified_done_chance: float = None, miss_intervention_cost: float = None, intervention_cost: float = None, **kwargs) -> None:
        super().__init__(game, network1, learner1, exploration1, gamma1, K1, **kwargs)
        self.boards = [None] * self.batch
        self.interventions = torch.zeros(self.batch, device=device)
        self.modified_done_chance = modified_done_chance
        self.miss_intervention_cost = miss_intervention_cost
        self.intervention_cost = intervention_cost
        self.counter = 0
        self.K1 = K1

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        actions = self.exploration.explore(self.values.detach())
        return self.modify_board(actions, board), actions

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor, *args):
        if action != None:
            self(args[0])
            self.learner.learn(self.values, state_after, action, reward, done)

    def modify_board(self, actions, board, replace = True):
        intervention_layer = torch.nn.functional.one_hot(actions, self.height * self.width).reshape(actions.shape[0], self.height, self.width).unsqueeze(1)
        if self.extradim == 0 or not replace:
            modified_board = torch.cat((board, intervention_layer), 1)
        else:
            modified_board = torch.cat((board[:,:-1], intervention_layer), 1)
        return modified_board

    def modify(self, board, rewards, dones, info):
        self.counter += 1
        intervention = self.interventions.to(dtype=int)
        modified_board = self.modify_board(intervention, board)
        modified_rewards = torch.sum(modified_board[:, 0] * modified_board[:, -1], (1, 2))
        modified_rewards[rewards == 1] = 0
        for i in range(len(info)):
            if 'player_end' in info[i]:
                modified_rewards[i] += modified_board[i, -1][(info[i]['player_end'][1], info[i]['player_end'][0])]

        modified_dones = torch.clone(modified_rewards)
        modified_dones[dones == 1] = 1
        rands = torch.rand(len(modified_rewards))
        modified_dones[rands < max(self.modified_done_chance/4, self.modified_done_chance * (1 - self.counter/self.K1))] = 1
        tele_rewards = self.miss_intervention_cost * torch.clone(modified_dones)
        tele_rewards[modified_rewards == 1] = self.intervention_cost
        tele_rewards[rewards == 1] = 1
        tele_rewards[rewards == -1] = -1
        intervention_idx = torch.flatten(torch.nonzero(modified_dones.long()))
        return modified_board, modified_rewards, modified_dones, tele_rewards, intervention_idx

    def interveen(self, board, intervention_idx, modified_board):
        if self.extradim == 1:
            modified_board = torch.clone(modified_board)
            current_board = modified_board
        else:
            current_board = board

        if len(intervention_idx) > 0:
            needs_intervention_board = current_board[intervention_idx]
            new_boards, intervention = self(needs_intervention_board)
        for i in range(len(intervention_idx)):
            batch_idx = intervention_idx[i]
            self.boards[batch_idx] = current_board[batch_idx]
            modified_board[batch_idx] = new_boards[i]
            self.interventions[batch_idx] = intervention[i]
        return modified_board

    def pre_process(self, env):
        return torch.flatten(torch.nonzero(torch.ones(env.layers.board.shape[0], device=device).long())), torch.zeros(env.layers.board.shape[0], env.layers.board.shape[1] + 1, env.layers.board.shape[2], env.layers.board.shape[3], device=device)

class Mover(Agent):
    def __init__(self, game: Game, network2: Networks = None, learner2: Learners = None, exploration2: Explorations = None, gamma2: float = None, K2 : float = None, **kwargs) -> None:
        super().__init__(game, network2, learner2, exploration2, gamma2, K2, **kwargs)

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        actions = self.exploration.explore(self.values.detach())
        return actions

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor, *args):
        self.learner.learn(self.values, state_after, action, reward, done)

class MetaTeleporter(Teleporter):
    def metamodify(self, board, rewards, dones, info, interventions1):
        intervention1 = interventions1.to(dtype=int)
        modified_board1 = self.modify_board(intervention1, board, replace=False)
        modified_rewards1 = torch.sum(modified_board1[:, 0] * modified_board1[:, -1], (1, 2)) * (1 - rewards)
        for i in range(len(info)):
            if 'player_end' in info[i]:
                modified_rewards1[i][modified_board1[i, -1][(info[i]['player_end'][1], info[i]['player_end'][0])] == 1] = 1

        modified_dones1 = torch.clone(modified_rewards1)
        modified_dones1[dones == 1] = 1
        rands = torch.rand(len(modified_rewards1))
        modified_dones1[rands < self.modified_done_chance] = 1
        
        modified_rewards2 = self.miss_intervention_cost * torch.clone(modified_dones1)
        modified_rewards2[modified_rewards1 == 1] = self.intervention_cost
        intervention2 = self.interventions.to(dtype=int)
        modified_board2 = self.modify_board(intervention2, board)
        modified_rewards2[torch.sum(modified_board2[:, 0] * modified_board2[:, -1], (1, 2)) * (1 - rewards) == 1] = 1
        for i in range(len(info)):
            if 'player_end' in info[i]:
                modified_rewards2[i][modified_board2[i, -1][(info[i]['player_end'][1], info[i]['player_end'][0])] == 1] = 1
        modified_dones2 = torch.zeros(modified_rewards2.shape, device=device)
        modified_dones2[modified_rewards2 == 1] = 1
        modified_dones2[dones == 1] = 1
        rands = torch.rand(len(modified_rewards2))
        modified_dones2[rands < self.modified_done_chance/5] = 1
        modified_dones1[modified_dones2 == 1] = 1

        tele_rewards = self.miss_intervention_cost * torch.clone(modified_dones2)
        tele_rewards[modified_rewards2 == 1] = self.intervention_cost
        tele_rewards[rewards == 1] = 1
        intervention_idx1 = torch.flatten(torch.nonzero(modified_dones1.long()))
        intervention_idx2 = torch.flatten(torch.nonzero(modified_dones2.long()))
        
        return modified_board1, modified_board2, modified_rewards1, modified_rewards2, modified_dones1, modified_dones2, tele_rewards, intervention_idx1, intervention_idx2

class CFAgent(Agent):
    def __init__(self, game: Game, TopN: int = None, Counterfacts: int = None, CF_convert: int = None, network1: Networks = None, learner1: Learners = None, exploration2: Explorations = None, gamma1: float = None, K1 : float = None, **kwargs) -> None:
        super().__init__(game, network1, learner1, exploration2, gamma1, K1, **kwargs)
        self.boards = [None] * self.batch
        self.counterfactuals = torch.zeros(self.batch, device=device)
        self.counter = 0
        self.K1 = K1
        self.convert_function = CF_convert
        self.counterfacts = Counterfacts
        self.TopN = TopN - 1
        self.running_dones = [0 for _ in range(10000)]
        self.done_number = 0
        self.CF_count = 0

    def __call__(self, board: Tensor) -> Tensor:
        self.values: Tensor = self.net.network(board)
        return self.values

    def choose_action(self, board: Tensor, teleporter) -> Tensor:
        self.counter += 1
        teleporter(board)
        tele_values = teleporter.values.detach()
        values = self.net.network(board)
        # if self.counter % 100 == 0:
        #    print(values)
        learning_scores = self.convert_values(values.detach(), tele_values)
        actions = torch.argsort(learning_scores, dim=1, descending=True)[:,random.randint(0,self.TopN)]
        return actions

    def convert_values(self, values, tele_values):
        values = (values + 1)/2
        values[values > 1] = 1
        values[values < 0] = 0
        if self.convert_function == 1:
            learning_scores = values
        elif self.convert_function == 2:
            learning_scores = values * softmax(tele_values, dim=1)
        elif self.convert_function == 3:
            learning_scores = values * softmax(tele_values * 3, dim=1)
        elif self.convert_function == 4:
            learning_scores = values * softmax(tele_values * 10, dim=1)
        elif self.convert_function == 5:
            learning_scores = (1 - abs(values - 0.75)) * softmax(tele_values, dim=1)
        elif self.convert_function == 6:
            learning_scores = (1 - abs(values - 0.75)) * softmax(tele_values * 3, dim=1)
        elif self.convert_function == 7:
            learning_scores = (1 - abs(values - 0.75)) * softmax(tele_values * 10, dim=1)
        elif self.convert_function == 8:
            learning_scores = softmax(tele_values, dim=1)
        elif self.convert_function == 9:
            learning_scores = softmax(tele_values * 3, dim=1)
        elif self.convert_function == 10:
            learning_scores = softmax(tele_values * 10, dim=1)
        return learning_scores

    def _learn(self, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor, *args):
        if action != None:
            self(args[0])
            self.learner.learn(self.values, state_after, action, reward, done)

    def pre_process(self, env):
        return torch.ones(env.layers.board.shape[0], device=device).long()

    def counterfact(self, env, dones, teleporter):
        CF_dones, cfs = self.counterfact_check(dones, env, check=0)
        for _ in range(cfs):
            counterfactuals = []
            if len(CF_dones) > 0:
                needs_intervention_board = env.board[CF_dones]
                actions = self.choose_action(needs_intervention_board, teleporter)
                for action in actions:
                    counterfactuals.append((action.item() % self.width, action.item()// self.height))
                for i in range(len(CF_dones)):
                    batch_idx = CF_dones[i]
                    self.boards[batch_idx] = env.board[batch_idx]
                    self.counterfactuals[batch_idx] = actions[i]
                    for layer in env.layers.layers:
                        if counterfactuals[i] in layer._positions[batch_idx] and counterfactuals[i][0] > 0 and counterfactuals[i][1] > 0 and counterfactuals[i][0] < self.width - 1 and counterfactuals[i][1] < self.height - 1:
                            layer.remove(batch_idx, counterfactuals[i])
                            env.layers.board[batch_idx, :, counterfactuals[i][1], counterfactuals[i][0]] = 0
            if any([x.name == "Rock" for x in env.layers.types]):
                for layer in env.layers.layers:
                    layer.update(env.board, [1 for _ in range(self.batch)], env.layers.all_items)
            else:
                for layer in env.layers.layers:
                    layer.NoRock_update(env.board, [1 for _ in range(self.batch)])
        return dones

    def counterfact2(self, env, dones, teleporter, simulator):
        CF_dones, cfs = self.counterfact_check(dones, env, check=0)
        for _ in range(cfs):
            counterfactuals = [set() for _ in range(len(CF_dones))]
            if len(CF_dones) > 0:
                needs_intervention_board = env.board[CF_dones]
                actions = self.choose_action(needs_intervention_board, teleporter)
                cf_boards = simulator.simulate(needs_intervention_board, actions)
                print(cf_boards)
                limit = 0.5
                cf_boards[cf_boards < limit] = 0
                for i in range(len(CF_dones)):
                    batch_idx = CF_dones[i]
                    changes = torch.nonzero(cf_boards[i])
                    for change in changes:
                        layer = change.item() // (env.board.shape[1] * self.width)
                        width = (change.item() - (env.board.shape[1] * self.width) * layer) // self.width
                        height = change.item() - layer * (env.board.shape[1] * self.width) - width * self.width
                        counterfactuals[i].add(((width, height), layer))
                    self.boards[batch_idx] = env.board[batch_idx]
                    self.counterfactuals[batch_idx] = actions[i]
                    for counterfact in counterfactuals[i]:
                        for i in range(len(env.layers.layers)):
                            layer = env.layers.layers[i]
                            if not (counterfact[0][0] > 0 and counterfact[0][1] > 0 and counterfact[0][0] < self.width - 1 and counterfact[0][1] < self.height - 1):
                                continue
                            elif counterfact[0] in layer._positions[batch_idx]:
                                layer.remove(batch_idx, counterfact[0])
                                env.layers.board[batch_idx, i, counterfact[0][1], counterfact[0][0]] = 0
                            else:
                                layer.add(batch_idx, counterfact[0])
                                env.layers.board[batch_idx, i, counterfact[0][1], counterfact[0][0]] = 1                            

            if any([x.name == "Rock" for x in env.layers.types]):
                for layer in env.layers.layers:
                    layer.update(env.board, [1 for _ in range(self.batch)], env.layers.all_items)
            else:
                for layer in env.layers.layers:
                    layer.NoRock_update(env.board, [1 for _ in range(self.batch)])
        return dones

    def counterfact_check(self, dones, env, check=1):
        self.CF_count += 1
        if check == 0:
            return torch.flatten(torch.nonzero(dones)), self.counterfacts
        elif check == 1:
            average_dones = (torch.sum(dones)/len(dones)).item()
            self.done_number += (average_dones - self.running_dones[self.CF_count % 10000])/10000
            self.running_dones[self.CF_count % 10000] = average_dones
            if random.random() < self.done_number * self.counterfacts or self.CF_count == 1:
                return torch.flatten(torch.nonzero(torch.ones(env.layers.board.shape[0], device=device).long())), 1
            return torch.flatten(torch.nonzero(torch.zeros(env.layers.board.shape[0], device=device).long())), 1





