import torch.nn as nn
from enum import Enum
from torch import cat, Tensor
import pickle
from helper import device


class Networks(Enum):
    Small = 0
    Large = 1


class Network(nn.Module):
    def __init__(self, dim: int, network: Networks):
        super(Network, self).__init__()
        if network == Networks.Small:
            self.model = nn.Sequential(nn.Conv2d(dim, 8, 3), nn.ReLU(), nn.Conv2d(8, 12, 3), nn.ReLU(), nn.Conv2d(12, 12, 3), nn.ReLU(), nn.Conv2d(12, 12, 3), nn.ReLU(), nn.Conv2d(12, 16, 3), nn.ReLU(), nn.Conv2d(16, 4, 5), nn.Flatten(), nn.Softmax(1))
        elif network == Networks.Large:
            self.model = nn.Sequential(nn.Conv2d(dim, 16, 3), nn.ReLU(), nn.Conv2d(16, 24, 3), nn.ReLU(), nn.Conv2d(24, 36, 3), nn.ReLU(), nn.Conv2d(36, 24, 3), nn.ReLU(), nn.Conv2d(24, 16, 3), nn.ReLU(), nn.Conv2d(16, 4, 5), nn.Flatten(), nn.Softmax(1))

    def forward(self, x: Tensor):
        return self.model(x)

    def add_category(self):
        for p in [self.model[-3]._parameters[x] for x in ['bias', 'weight']]:
            p.data = cat((p.data, p.data[-1:]))


class Net:
    def __init__(self, dim: int, network: Networks):
        self.network = Network(dim, network).to(device)
        self.placeholder = Network(dim, network).to(device)
        self.target = Network(dim, network).to(device)

    def update(self):
        self.target = pickle.loads(pickle.dumps(self.placeholder))
        self.placeholder = pickle.loads(pickle.dumps(self.network))
