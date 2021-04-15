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

    def save_option_critic(self, old_obses, current_options, rewards, next_obses, dones):
        for old_obs, current_option, reward, next_obs, done in zip(old_obses, current_options, rewards, next_obses, dones):
            self.save_data((old_obs.unsqueeze(0), current_option, reward, next_obs.unsqueeze(0), done))

    def stacker_option_critic(self, sample):
        arays = list(zip(*sample))
        return concatenation(arays[0]), torch.tensor(arays[1], device=device), torch.tensor(arays[2], device=device), concatenation(arays[3]), torch.tensor(arays[4], device=device)

    def sample_option_critic(self):
        samples = (random.sample(self.buffer[:min(self.counter, self.replay_size)], min(self.sample_size, self.counter)))
        if samples == []:
            return None, None, None, None, None
        return self.stacker_option_critic(samples)


class CFReplayBuffer:
    def __init__(self, replay_size: int = None, sample_size: int = None, batch: int = None, **kwargs):
        self.counter = 0
        self.replay_size = replay_size
        self.buffer = [None for _ in range(self.replay_size)]
        self.sample_size = sample_size
        self.batch = batch
        self.dones = torch.zeros(batch, device=device)
        self.rewards = torch.zeros(batch, device=device)

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

    def CF_save_data(self, board, observations, counterfactuals, rewards, dones, CF_dones):
        self.dones[dones == 1] = 1
        self.rewards[rewards == 1] = 1

        for idx in CF_dones:
            data = (torch.clone(board[idx]).unsqueeze(0), torch.clone(observations[idx]).unsqueeze(0), torch.clone(counterfactuals[idx]).unsqueeze(0), torch.clone(self.rewards[idx]).unsqueeze(0), torch.clone(self.dones[idx]).unsqueeze(0))
            self.buffer[self.counter % self.replay_size] = data
            self.counter += 1
            self.dones[idx] = 0
            self.rewards[idx] = 0


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
