import random
from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda, float32
from helper import device

class replay_buffer:
    def __init__(self, size):
        self.counter = 0
        self.replay_size = size
        self.buffer = [None for _ in range(self.replay_size)]

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return tensor(arays[0]).unsqueeze(1).float().to(device), tensor(arays[1]).float().to(device), tensor(arays[2]).unsqueeze(1).float().to(device), tensor(arays[3]).float().to(device), tensor(arays[4]).float().to(device), tensor(arays[5]).float().to(device), tensor(arays[6]).to(device)

    def sample_data(self, batch):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(batch, self.counter)))
        return self.stacker(samples)
