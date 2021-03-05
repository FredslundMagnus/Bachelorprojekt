from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from helper import move_figure


class Collector:
    def __init__(self, batch: int = None, **kwargs) -> None:
        self.batch = batch
        self.counter = 0
        self.filter_size = 1000
        self.rewards = []
        self.dones = []
        self.data = {}
        
    def show(self, game) -> None:
        plot_positions = [(0,0), (600,0), (1200, 0), (0, 520), (600, 520), (1200, 520)]

        i = 0
        plotter = [[]] * len(self.data)
        for key in self.data:
            fig = plt.figure()
            move_figure(fig, plot_positions[i % len(plot_positions)])
            for j in range(len(self.data[key])):
                if j > 10:
                    plotter[i].append(sum(self.data[key][(j - 10):j]) / 10)
            plt.plot(plotter[i], label=str("reward type: " + str(key[0]) + " done type: " + str(key[1])))
            plt.xlabel("Seen frames in " + str(self.batch * self.filter_size))
            plt.ylabel("reward over dones")
            plt.legend(loc="upper left")
            i += 1

        plt.pause(15)
        plt.close('all')

    def hide(self) -> None:
        plt.close('all')

    def collect(self, rewards, dones):
        self.counter += 1
        if self.rewards == [] and self.dones == []:
            self.rewards = [10**(-6)] * len(rewards)
            self.dones = [10**(-6)] * len(dones)
        for i in range(len(rewards)):
            self.rewards[i] += sum(rewards[i])/len(rewards[i])
        for i in range(len(dones)):
            self.dones[i] += sum(dones[i])/len(dones[i])
            

        if self.counter % self.filter_size == 0:
            for i in range(len(rewards)):
                for k in range(len(dones)):
                    if (i,k) not in self.data:
                        self.data[(i,k)] = []
                    self.data[(i,k)].append(self.rewards[i]/self.dones[k])
            self.rewards = []
            self.dones = []