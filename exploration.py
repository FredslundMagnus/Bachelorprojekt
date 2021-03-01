from random import random
from helper import device
from torch.nn.functional import softmax
from numpy.random import choice
from enum import Enum
import torch
from torch import Tensor


class Explorations(Enum):
    greedy = 1
    epsilonGreedy = 0


class Exploration:
    def __init__(self, exploration: Explorations, K: float = None, **kwargs) -> None:
        self.counter = 1
        self._K = K
        if exploration == Explorations.greedy:
            self.explore = self.greedy
        elif exploration == Explorations.epsilonGreedy:
            self.explore = self.epsilonGreedy

    def explore(self, vals: Tensor) -> Tensor:
        pass

    @property
    def epsilon(self):
        return max(0, 1 - self.counter / self.K)

    @property
    def K(self):
        return max(1, self._K / self.counter)

    def greedy(self, vals):
        self.counter += 1
        vals = torch.flatten(vals.detach(), start_dim=1)
        return torch.max(vals, dim=1)

    def epsilonGreedy(self, vals):
        self.counter += 1
        vals = torch.flatten(vals.detach(), start_dim=1)

        if random() > self.epsilon:
            return torch.max(vals, dim=1)
        else:
            idx = torch.tensor(choice(vals.shape[1], vals.shape[0]), device=device).long()
            return torch.gather(vals, 0, idx.unsqueeze(1)).squeeze(1), idx
