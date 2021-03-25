import torch.nn as nn
from enum import Enum
from torch import cat, Tensor
import pickle
from helper import device


class Networks(Enum):
    Small = 0
    Teleporter = 1
    Mini = 2


class Network(nn.Module):
    def __init__(self, dim: int, width: int, height: int, network: Networks):
        super(Network, self).__init__()
        if network == Networks.Small:
            self.model = nn.Sequential(nn.Conv2d(dim, 8, 3), nn.LeakyReLU(), nn.Conv2d(8, 12, 3), nn.LeakyReLU(), nn.Conv2d(12, 12, 3), nn.LeakyReLU(), nn.Conv2d(12, 12, 3), nn.LeakyReLU(), nn.Conv2d(12, 16, 3), nn.LeakyReLU(), nn.Conv2d(16, 4, 1), nn.Flatten())
        elif network == Networks.Teleporter:
            self.model = nn.Sequential(nn.Conv2d(dim, 128, 5), nn.LeakyReLU(), nn.Conv2d(128, 64, 3), nn.LeakyReLU(), nn.Flatten(), nn.Linear(64 * (width - 6) * (height - 6), 128), nn.LeakyReLU(), nn.Linear(128, 128), nn.LeakyReLU(), nn.Linear(128, height * width), nn.Flatten())
        elif network == Networks.Mini:
            self.model = nn.Sequential(nn.Conv2d(dim, 128, 5), nn.LeakyReLU(), nn.Conv2d(128, 64, 3), nn.LeakyReLU(), nn.Flatten(), nn.Linear(64 * (width - 6) * (height - 6), 128), nn.LeakyReLU(), nn.Linear(128, 128), nn.LeakyReLU(), nn.Linear(128, 4), nn.Flatten())

    def forward(self, x: Tensor):
        return self.model(x)

    def add_category(self):
        for p in [self.model[-3]._parameters[x] for x in ['bias', 'weight']]:
            p.data = cat((p.data, p.data[-1:]))


class Net:
    def __init__(self, dim: int, width: int, height: int, network: Networks, update: int = None, **kwargs):
        self.network = Network(dim, width, height, network).to(device)
        self.placeholder = Network(dim, width, height, network).to(device)
        self.target = Network(dim, width, height, network).to(device)
        self.i = 1
        self.n = update

    def update(self):
        self.target = pickle.loads(pickle.dumps(self.placeholder))
        self.placeholder = pickle.loads(pickle.dumps(self.network))

    def learn(self):
        self.i += 1
        if self.i % self.n == 0:
            self.update()
