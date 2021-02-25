from auxillaries import device
import torch
import torch.nn as nn
from torch.optim import Adam, SGD
import pickle
from torch import Tensor

class DoubleQNet:
    def __init__(self):
        self.network = Network().to(device)
        self.target_network = Network().to(device)
        self.placeholder_network = Network().to(device)
        self.gamma = 0.99
        self.criterion = nn.MSELoss()
        self.optimizer = Adam(self.network.parameters(), lr=1e-4, weight_decay=1e-5)

    def take_action(self, x: Tensor):
        vals = self.network(x)
        return vals

    def DoubleQlearn(self, state_before, state_after, action, reward, done):
        vals = self.network(state_before)
        vals_next = self.network(state_after)
        vals_target_next = self.target_network(state_after)
        value_next = torch.gather(vals_target_next, 2, torch.argmax(vals_next, 2).unsqueeze(2))
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1)
        td_guess = torch.gather(vals, 2, action.long().view(-1, 1, 1)).view(-1)
        loss_value_network = self.criterion(td_guess, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

    def update_target_network(self):
        self.target_network = pickle.loads(pickle.dumps(self.placeholder_network))
        self.placeholder_network = pickle.loads(pickle.dumps(self.network))

class Network(nn.Module):
    def __init__(self, dim: int):
        super(Network, self).__init__()
        self.model = nn.Sequential(nn.Conv2d(dim, 8, 3), nn.ReLU(), nn.Conv2d(8, 12, 3), nn.ReLU(), nn.Conv2d(12, 16, 3), nn.ReLU(), nn.Conv2d(16, 2, 4), nn.Flatten(), nn.Softmax(1))

    def forward(self, x: Tensor):
        return self.model(x)
