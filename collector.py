from typing import List
import matplotlib.pyplot as plt
import numpy as np

class Collector:
    def __init__(self) -> None:
        self.counter = 0
        self.filter_size = 1000
        self.rewards = []
        self.dones = []
        self.running_rewards = []
        self.running_dones = []

    def show(self, game) -> None:
        plt.plot(self.running_rewards)
        plt.show(block=True)
        plt.plot(self.running_dones)
        plt.show(block=True)

    def collect(self, rewards: List[float], dones: List[int]):
        self.counter += 1
        average_reward = sum(rewards)/len(rewards)
        average_done = sum(dones)/len(dones)

        self.rewards.append(average_reward)
        self.dones.append(average_done)

        if self.counter == self.filter_size:
            self.running_rewards.append(sum(self.rewards)/self.filter_size)
            self.running_dones.append(sum(self.dones)/self.filter_size)   
        elif self.counter > self.filter_size:     
            self.running_rewards.append(self.running_rewards[-1] + (average_reward - self.rewards[-self.filter_size])/self.filter_size)