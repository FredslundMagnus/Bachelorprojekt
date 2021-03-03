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
        plt.plot(self.running_dones, label="game per action")
        plt.plot(self.win_percent, label="reward per game")
        plt.legend(loc="upper left")
        plt.pause(5)
        plt.close('all')

        fig = plt.figure()
        move_figure(fig, 0, 0)
        plt.plot(self.running_Irewards, label="modifiedreward per action")
        plt.plot(self.running_Idones, label="modifiedgame per action")
        plt.plot(self.Iwin_percent, label="modifiedreward per game")
        plt.legend(loc="upper left")
        plt.pause(5)
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
            self.running_dones.append(self.dones/self.filter_size)
            self.win_percent.append(self.rewards/self.dones)
            self.rewards = 10**(-6)
            self.dones = 10**(-6)

            self.running_Irewards.append(self.Irewards/self.filter_size)
            self.running_Idones.append(self.Idones/self.filter_size)
            self.Iwin_percent.append(self.Irewards/self.Idones)
            self.Irewards = 10**(-6)
            self.Idones = 10**(-6)