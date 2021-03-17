import torch.nn as nn
from torch import Tensor
from torch.nn import MSELoss
from torch.optim import Adam
import torch

class Simulator(nn.Module):
    def __init__(self, dim: int, width: int, height: int):
        self.width = width
        self.height = height
        self.boardmodel = nn.Sequential(nn.Conv2d(dim, 64, 3, padding=1), nn.LeakyReLU(), nn.Conv2d(64, 128, 3, padding=1), nn.Conv2d(128, dim, 3, padding=1), nn.Flatten())
        self.rewarddonemodel = nn.Sequential(nn.Flatten(), nn.Linear(dim, 50, 3), nn.LeakyReLU(), nn.Linear(dim, 50, 2), nn.LeakyReLU(), nn.Flatten())
        self.criterion = MSELoss()
        self.optimizer = Adam(self.net.network.parameters(), lr=1e-5, weight_decay=1e-5)
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
        label = torch.cat(((board_after - board_before).flatten(), reward, done), dim=1)
        loss = self.criterion(guess, label)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
