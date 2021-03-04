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

        self.Irewards = 10**(-6)
        self.Idones = 10**(-6)
        self.running_Irewards = []
        self.running_Idones = []
        self.Iwin_percent = []
        
    def show(self, game) -> None:
        fig = plt.figure()
        move_figure(fig, 0, 0)
        plt.plot(self.running_rewards, label="reward per action")
        plt.legend(loc="upper left")

        fig = plt.figure()
        move_figure(fig, 600, 0)
        plt.plot(self.running_dones, label="game length")
        plt.legend(loc="upper left")

        fig = plt.figure()
        move_figure(fig, 1200, 0)
        plt.plot(self.win_percent, label="reward per game")
        plt.legend(loc="upper left")

        fig = plt.figure()
        move_figure(fig, 0, 520)
        plt.plot(self.running_Irewards, label="modified reward per action")
        plt.legend(loc="upper left")

        fig = plt.figure()
        move_figure(fig, 600, 520)
        plt.plot(self.running_Idones, label="modified game length")
        plt.legend(loc="upper left")

        fig = plt.figure()
        move_figure(fig, 1200, 520)
        plt.plot(self.Iwin_percent, label="modified reward per modified game")
        plt.legend(loc="upper left")

        plt.pause(10)
        plt.close('all')

    def hide(self) -> None:
        plt.close('all')

    def collect(self, rewards: List[float], dones: List[int], Irewards: List[float], Idones: List[int]):
        self.counter += 1
        average_reward = sum(rewards)/len(rewards)
        average_done = sum(dones)/len(dones)

        average_Ireward = sum(Irewards)/len(Irewards)
        average_Idone = sum(Idones)/len(Idones)

        self.rewards += average_reward
        self.dones += average_done

        self.Irewards += average_Ireward
        self.Idones += average_Idone

        if self.counter % self.filter_size == 0:
            self.running_rewards.append(self.rewards/self.filter_size)
            self.running_dones.append(self.filter_size/self.dones)
            self.win_percent.append(self.rewards/self.dones)
            self.rewards = 10**(-6)
            self.dones = 10**(-6)

            self.running_Irewards.append(self.Irewards/self.filter_size)
            self.running_Idones.append(self.filter_size/self.Idones)
            self.Iwin_percent.append(self.Irewards/self.Idones)
            self.Irewards = 10**(-6)
            self.Idones = 10**(-6)