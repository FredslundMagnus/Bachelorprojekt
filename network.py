import torch.nn as nn
from enum import Enum
from torch import cat, Tensor


class Networks(Enum):
    Small = 0


class Network(nn.Module):
    def __init__(self, dim: int, networks: Networks = Networks.Small):
        super(Network, self).__init__()
        if networks == Networks.Small:
            self.model = nn.Sequential(nn.Conv2d(dim, 8, 3), nn.ReLU(), nn.Conv2d(8, 12, 3), nn.ReLU(), nn.Conv2d(12, 16, 3), nn.ReLU(), nn.Conv2d(16, 2, 4), nn.Flatten(), nn.Softmax(1))

    def forward(self, x: Tensor):
        return self.model(x)

    def add_category(self):
        for p in [self.model[-3]._parameters[x] for x in ['bias', 'weight']]:
            p.data = cat((p.data, p.data[-1:]))
