from random import random
from helper import device
from torch.nn.functional import softmax
from numpy.random import choice
from enum import Enum
import torch
from torch import Tensor


class Explorations(Enum):
    greedy = 0
    epsilonGreedy = 1
    softmaxer = 2


class Exploration:
    def __init__(self, exploration: Explorations, K: float = None, **kwargs) -> None:
        self.counter = 1
        self.K = K
        if exploration == Explorations.greedy:
            self.explore = self.greedy
        elif exploration == Explorations.epsilonGreedy:
            self.explore = self.epsilonGreedy
        elif exploration == Explorations.softmaxer:
            self.explore = self.softmaxer

    def explore(self, vals: Tensor) -> Tensor:
        pass

    @property
    def epsilon(self):
        return max(0.1, 1 - self.counter / self.K)

    @property
    def K_(self):
        return max(1, self.K / self.counter)

    def greedy(self, vals):
        vals.detach()
        self.counter += 1
        if self.counter % 1000 == 1:
            print(f"({str(float(torch.min(vals[0])))[:4]}, {str(float(torch.max(vals[0])))[:4]})", end=", ")
        return torch.argmax(vals, dim=1)

    def epsilonGreedy(self, vals):
        self.counter += 1
        if self.counter % 10000 == 0:
            print(f"({str(float(torch.min(vals[0])))[:4]}, {str(float(torch.max(vals[0])))[:4]})", end=", ")
        return torch.argmax(vals, dim=1) if random() > self.epsilon else torch.tensor(choice(vals.shape[1], vals.shape[0]), device=device).long()

    def softmaxer(self, vals):
        self.counter += 1
        if self.counter % 10000 == 1:
            print(f"({str(float(torch.min(vals[0])))[:4]}, {str(float(torch.max(vals[0])))[:4]})", end=", ")
        return torch.flatten(torch.multinomial(softmax(vals / self.K_, dim=1), 1, replacement=True))