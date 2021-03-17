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
        self.boardmodel = nn.Sequential(nn.Conv2d(self.dim, 64, 3, padding=1), nn.LeakyReLU(), nn.Conv2d(64, 128, 3, padding=1), nn.Conv2d(128, self.dim - 1, 3, padding=1), nn.Flatten())
        self.rewarddonemodel = nn.Sequential(nn.Flatten(), nn.Linear(self.dim * self.height * self.width, 50), nn.LeakyReLU(), nn.Linear(50, 2), nn.LeakyReLU(), nn.Flatten())
        self.criterion = MSELoss()
        self.optimizer_boardmodel = Adam(self.boardmodel.parameters(), lr=1e-5, weight_decay=1e-5)
        self.optimizer_rewarddonemodel = Adam(self.rewarddonemodel.parameters(), lr=1e-5, weight_decay=1e-5)
        self.counter = 0

    def forward(self, x: Tensor):
        y = self.boardmodel(x)
        z = self.rewarddonemodel(x)
        x = torch.cat((y, z), dim=1)
        return x

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.counter += 1
        intervention_layer = torch.nn.functional.one_hot(action, self.height * self.width).reshape(action.shape[0], self.height, self.width).unsqueeze(1)
        modified_board = torch.cat((board_before, intervention_layer), 1)
        guess = self.forward(modified_board)
        label = torch.cat(((board_after - board_before).flatten(start_dim=1), reward.unsqueeze(1), done.unsqueeze(1)), dim=1)
        loss = self.criterion(guess, label)
        loss.backward()
        self.optimizer_boardmodel.step()
        self.optimizer_rewarddonemodel.step()
        self.optimizer_boardmodel.zero_grad()
        self.optimizer_rewarddonemodel.zero_grad()

class Simulator:
    def __init__(self, dim: int, width: int, height: int, update: int = None, **kwargs):
        self.network = Network(dim, width, height).to(device)

    def learn(self, board_before: Tensor, board_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.network.learn(board_before, board_after, action, reward, done)
