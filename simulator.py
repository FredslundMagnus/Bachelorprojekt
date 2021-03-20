import torch.nn as nn
from torch import Tensor
from torch.nn import MSELoss
from torch.optim import Adam
import torch
from game import Game
from helper import device

class Network(nn.Module):
    def __init__(self, game: Game, width: int, height: int):
        super(Network, self).__init__()
        self.dim = len(game.layers) + 1
        self.width = width
        self.height = height
        self.boardmodel = nn.Sequential(nn.Conv2d(self.dim, 64, 3, padding=1), nn.LeakyReLU(), nn.Conv2d(64, 128, 3, padding=1), nn.LeakyReLU(), nn.Conv2d(128, self.dim - 1, 3, padding=1), nn.Flatten())
        self.rewarddonemodel = nn.Sequential(nn.Conv2d(self.dim, 32, 5, padding=2), nn.LeakyReLU(), nn.Flatten(), nn.Linear(self.height * self.width * 32, 10), nn.LeakyReLU(), nn.Linear(10, 2), nn.LeakyReLU(), nn.Flatten())
        self.criterion = MSELoss()
        self.optimizer_boardmodel = Adam(self.boardmodel.parameters(), lr=1e-5, weight_decay=1e-5)
        self.optimizer_rewarddonemodel = Adam(self.rewarddonemodel.parameters(), lr=1e-5, weight_decay=1e-5)
        self.counter = 0

    def boardforward(self, x: Tensor):
        return self.boardmodel(x)

    def RDforward(self, x: Tensor):
        return self.rewarddonemodel(x)

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.counter += 1
        intervention_layer = torch.nn.functional.one_hot(action, self.height * self.width).reshape(action.shape[0], self.height, self.width).unsqueeze(1)
        modified_board = torch.cat((board_before, intervention_layer), 1)
        modified_board_before_no_dones = modified_board[done == 0]
        guess_board = self.boardforward(modified_board_before_no_dones)
        label_board = ((board_after - board_before)**2)[done == 0].flatten(start_dim=1)
        guess_RD = self.RDforward(modified_board)
        label_RD = torch.cat((reward.unsqueeze(1), done.unsqueeze(1)), dim=1)
        loss_board = self.criterion(guess_board, label_board)
        loss_board.backward()
        self.optimizer_boardmodel.step()
        self.optimizer_boardmodel.zero_grad()
        loss_RD = self.criterion(guess_RD, label_RD)
        loss_RD.backward()
        self.optimizer_rewarddonemodel.step()
        self.optimizer_rewarddonemodel.zero_grad()
        return torch.sum(loss_RD).item(), torch.sum(loss_board).item()
    
    def simulate(self, board_before: Tensor, action: Tensor):
        intervention_layer = torch.nn.functional.one_hot(action, self.height * self.width).reshape(action.shape[0], self.height, self.width).unsqueeze(1)
        modified_board = torch.cat((board_before, intervention_layer), 1)
        guess_board = self.boardforward(modified_board)
        guess_RD = self.RDforward(modified_board)
        return guess_board, guess_RD



class Simulator:
    def __init__(self, dim: int, width: int, height: int, **kwargs):
        self.network = Network(dim, width, height).to(device)

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        return self.network.learn(board_before, board_after, action, reward, done)

    def simulate(self, board_before: Tensor, action: Tensor):
        return self.network.simulate(board_before, action)
