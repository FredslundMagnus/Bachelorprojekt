from typing import List
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from helper import move_figure


class Collector:
    def __init__(self) -> None:
        self.counter = 0
        self.filter_size = 1000
        self.rewards = 10**(-6)
        self.dones = 10**(-6)
        self.running_rewards = []
        self.running_dones = []
        self.win_percent = []
        
    def show(self, game) -> None:
        fig = plt.figure()
        move_figure(fig, 0, 0)
        plt.plot(self.running_rewards, label="reward per action")
        plt.plot(self.running_dones, label="game per action")
        plt.plot(self.win_percent, label="reward per game")
        plt.legend(loc="upper left")
        plt.pause(5)
        plt.close('all')

    def hide(self) -> None:
        plt.close('all')

    def collect(self, rewards: List[float], dones: List[int]):
        self.counter += 1
        average_reward = sum(rewards)/len(rewards)
        average_done = sum(dones)/len(dones)

        self.rewards += average_reward
        self.dones += average_done

        if self.counter % self.filter_size == 0:
            self.running_rewards.append(self.rewards/self.filter_size)
            self.running_dones.append(self.dones/self.filter_size)
            self.win_percent.append(self.rewards/self.dones)
            self.rewards = 10**(-6)
            self.dones = 10**(-6)