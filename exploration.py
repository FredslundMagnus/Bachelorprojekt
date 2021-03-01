from random import random
from torch.nn.functional import softmax
from numpy.random import choice


class Exploration():
    def __init__(self, K: float = None) -> None:
        self.counter = 1
        self.K = K

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
