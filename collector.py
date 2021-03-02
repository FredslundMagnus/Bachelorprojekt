from typing import List
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from helper import move_figure
from collections import deque


class Collector:
    def __init__(self) -> None:
        self.counter = 0
        self.filter_size = 10000
        self.rewards = []
        self.dones = []
        self.running_rewards = []
        self.running_dones = []
        
    def show(self, game) -> None:
        fig = plt.figure()
        move_figure(fig, 0, 0)
        plt.plot(self.running_rewards)
        plt.plot(self.running_dones)
        plt.pause(5)
        plt.close('all')

    def hide(self) -> None:
        plt.close('all')

    def collect(self, rewards: List[float], dones: List[int]):
        self.counter += 1
        average_reward = sum(rewards)/len(rewards)
        average_done = sum(dones)/len(dones)

        self.rewards.append(average_reward)
        self.dones.append(average_done)

        if self.counter % self.filter_size == 0:
            self.running_rewards.append(sum(self.rewards)/self.filter_size)
            self.running_dones.append(sum(self.dones)/self.filter_size)
            self.rewards = []
            self.dones = []