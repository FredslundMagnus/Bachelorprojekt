from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np
from time import sleep
from helper import move_figure
import torch


class Collector:
    def __init__(self, batch: int = None, **kwargs) -> None:
        self.batch = batch
        self.counter = 0
        self.filter_size = 1000
        self.rewards = []
        self.dones = []
        self.data = {}
        self.lossBoard = [0]
        self.lossRD = [0]
        
    def show(self, game) -> None:
        plot_positions = [(0,0), (600,0), (1200, 0), (0, 520), (600, 520), (1200, 520)]

        i = 0
        for key in self.data:
            fig = plt.figure()
            move_figure(fig, plot_positions[i % len(plot_positions)])
            plt.plot(self.data[key], label=str("reward type: " + str(key[0]) + " done type: " + str(key[1])))
            plt.xlabel("Seen frames in " + str(self.batch * self.filter_size))
            plt.ylabel("reward over dones")
            plt.legend(loc="upper left")
            i += 1

        plt.pause(10)
        plt.close('all')

        plt.plot(self.lossBoard[:-1])
        plt.plot(self.lossRD[:-1])

        plt.pause(5)
        plt.close('all')

    def hide(self) -> None:
        plt.close('all')

    def collect(self, rewards, dones):
        self.counter += 1
        if self.rewards == [] and self.dones == []:
            self.rewards = [10**(-6)] * len(rewards)
            self.dones = [10**(-6)] * len(dones)
        for i in range(len(rewards)):
            self.rewards[i] += torch.sum(rewards[i])/len(rewards[i])
        for i in range(len(dones)):
            self.dones[i] += torch.sum(dones[i])/len(dones[i])
            

        if self.counter % self.filter_size == 0:
            for i in range(len(rewards)):
                for k in range(len(dones)):
                    if (i,k) not in self.data:
                        self.data[(i,k)] = []
                    self.data[(i,k)].append(self.rewards[i].item()/self.dones[k].item())
            self.rewards = []
            self.dones = []
    
    def collect_loss(self, lossboard: int, lossRD: int):
        self.counter += 1
        self.lossBoard[-1] += lossboard
        self.lossRD[-1] += lossRD

        if self.counter % self.filter_size == 0:
            self.lossBoard[-1] /= self.filter_size
            self.lossRD[-1] /= self.filter_size
            self.lossBoard.append(0)
            self.lossRD.append(0)