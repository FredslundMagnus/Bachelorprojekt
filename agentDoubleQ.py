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

    def update_target_network(self):
        self.target_network = pickle.loads(pickle.dumps(self.placeholder_network))
        self.placeholder_network = pickle.loads(pickle.dumps(self.network))

class Network(nn.Module):
    def __init__(self, dim: int):
        super(Network, self).__init__()
        self.model = nn.Sequential(nn.Conv2d(dim, 8, 3), nn.ReLU(), nn.Conv2d(8, 12, 3), nn.ReLU(), nn.Conv2d(12, 16, 3), nn.ReLU(), nn.Conv2d(16, 2, 4), nn.Flatten(), nn.Softmax(1))

    def forward(self, x: Tensor):
        return self.model(x)
