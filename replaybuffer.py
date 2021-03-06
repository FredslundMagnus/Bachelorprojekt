import random
from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda, float32
from helper import device


class ReplayBuffer:
    def __init__(self, replay_size: int = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0), concatenation(arays[3], 0), concatenation(arays[4], 0)

    def sample_data(self, batch):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(batch, self.counter)))
        return self.stacker(samples)
