import random
from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda, float32
from helper import device
import torch


class ReplayBuffer:
    def __init__(self, replay_size: int = None, sample_size: int = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]
        self.first_teleporter_save = True
        self.sample_size = sample_size

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0).long(), concatenation(arays[3], 0), concatenation(arays[4], 0), concatenation(arays[5], 0)

    def sample_data(self):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(self.sample_size, self.counter)))
        return self.stacker(samples)

    def teleporter_save_data(self, board, obs, interventions, tele_rewards, tele_done, intervention_idx, rewards):
        for idx in intervention_idx:
            data = (torch.clone(board[idx]).unsqueeze(0), torch.clone(obs[idx]).unsqueeze(0), torch.clone(interventions[idx]).unsqueeze(0), torch.clone(tele_rewards[idx]).unsqueeze(0), torch.clone(tele_done[idx]).unsqueeze(0), torch.clone(rewards[idx]).unsqueeze(0))
            self.buffer[self.counter % self.replay_size] = data
            self.counter += 1
