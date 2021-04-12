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
        self.criterion = MSELoss()
        self.optimizer_boardmodel = Adam(self.boardmodel.parameters(), lr=1e-5, weight_decay=1e-5)
        self.counter = 0

    def boardforward(self, x: Tensor):
        return self.boardmodel(x)

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor):
        if action != None:
            self.counter += 1
            intervention_layer = torch.nn.functional.one_hot(action, self.height * self.width).reshape(action.shape[0], self.height, self.width).unsqueeze(1)
            modified_board = torch.cat((board_before, intervention_layer), 1)
            guess_board = self.boardforward(modified_board)
            label_board = ((board_after - board_before)).flatten(start_dim=1).detach()
            loss_board = self.criterion(guess_board, label_board)
            loss_board.backward()
            self.optimizer_boardmodel.step()
            self.optimizer_boardmodel.zero_grad()
            return torch.sum(loss_board).item()
        else:
            return 0
    
    def simulate(self, board_before: Tensor, action: Tensor):
        intervention_layer = torch.nn.functional.one_hot(action, self.height * self.width).reshape(action.shape[0], self.height, self.width).unsqueeze(1)
        modified_board = torch.cat((board_before, intervention_layer), 1)
        guess_board = self.boardforward(modified_board)
        return guess_board



class Simulator:
    def __init__(self, dim: int, width: int, height: int, **kwargs):
        self.network = Network(dim, width, height).to(device)

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor):
        return self.network.learn(board_before, board_after, action)

    def simulate(self, board_before: Tensor, action: Tensor):
        return self.network.simulate(board_before, action)
