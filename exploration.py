from random import random
from torch.nn.functional import softmax
from numpy.random import choice
from enum import Enum


class Explorations(Enum):
    softmax = 0
    greedy = 1
    epsilonGreedy = 0

class Exploration():
    def __init__(self, exploration: Explorations, K: float = None, **kwargs) -> None:
        self.counter = 1
        self.K = K
        if exploration == Explorations.softmax:
            self.explore = self.softmax
        elif exploration == Explorations.greedy:
            self.explore = self.greedy
        elif exploration == Explorations.epsilonGreedy:
            self.explore = self.epsilonGreedy

    @property
    def epsilon(self):
        return max(0, 1 - self.counter / self.K)

    @property
    def K(self):
        return max(1, self.K / self.counter)

    def softmax(self, vals):
        self.counter += 1
        return int(choice(44, 1, p=softmax(vals.view(-1) / self.K, dim=0).detach().cpu().numpy()))

    def greedy(self, vals):
        self.counter += 1
        return vals.detach().cpu().numpy().argmax()

    def epsilonGreedy(self, vals):
        self.counter += 1
        return int(choice(44, 1)) if random() < self.epsilon else vals.detach().cpu().numpy().argmax()
