import random
from torch import as_tensor as tensor, cat as concatenation, device as devicer, cuda, float32
from helper import device
import torch


class ReplayBuffer:
    def __init__(self, replay_size: int = None, sample_size: int = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]
        self.sample_size = sample_size

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0).long(), concatenation(arays[3], 0), concatenation(arays[4], 0)

    def sample_data(self):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(self.sample_size, self.counter)))
        if samples == []:
            return None, None, None, None, None
        return self.stacker(samples)

    def teleporter_save_data(self, board, obs, interventions, tele_rewards, tele_done, intervention_idx):
        for idx in intervention_idx:
            data = (torch.clone(board[idx]).unsqueeze(0), torch.clone(obs[idx]).unsqueeze(0), torch.clone(interventions[idx]).unsqueeze(0), torch.clone(tele_rewards[idx]).unsqueeze(0), torch.clone(tele_done[idx]).unsqueeze(0))
            self.buffer[self.counter % self.replay_size] = data
            self.counter += 1

class CFReplayBuffer:
    def __init__(self, replay_size: int = None, sample_size: int = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]
        self.sample_size = sample_size

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0).long(), concatenation(arays[3], 0), concatenation(arays[4], 0)

    def sample_data(self):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(self.sample_size, self.counter)))
        if samples == []:
            return None, None, None, None, None
        return self.stacker(samples)

    def CF_save_data(self, board, observations, counterfactuals, rewards, CF_dones):
        for idx in torch.flatten(torch.nonzero(CF_dones)):
            data = (torch.clone(board[idx]).unsqueeze(0), torch.clone(observations[idx]).unsqueeze(0), torch.clone(counterfactuals[idx]).unsqueeze(0), torch.clone(rewards[idx]).unsqueeze(0), torch.clone(CF_dones[idx]).unsqueeze(0))
            self.buffer[self.counter % self.replay_size] = data
            self.counter += 1

class SimBuffer:
    def __init__(self, replay_size: int = None, sample_size: int = None, miss_intervention_cost: float = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]
        self.sample_size = sample_size
        self.miss_internvention_cost = miss_intervention_cost

    def save_data(self, data):
        self.buffer[self.counter % self.replay_size] = data
        self.counter += 1

    def stacker(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0], 0), concatenation(arays[1], 0), concatenation(arays[2], 0).long()

    def sample_data(self):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(self.sample_size, self.counter)))
        if samples == []:
            return None, None, None
        return self.stacker(samples)

    def simulator_save_data(self, board, obs, interventions, tele_rewards, tele_done, intervention_idx):
        for idx in intervention_idx:
            if tele_rewards[idx] != self.miss_internvention_cost and tele_done[idx] != 1:
                data = (torch.clone(board[idx]).unsqueeze(0), torch.clone(obs[idx]).unsqueeze(0), torch.clone(interventions[idx]).unsqueeze(0))
                self.buffer[self.counter % self.replay_size] = data
                self.counter += 1