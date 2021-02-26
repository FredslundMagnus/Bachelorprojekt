from helper import device
import torch
from network import Net
from enum import Enum
from torch.nn import MSELoss
from torch.optim import Adam
from torch import Tensor


class Learners(Enum):
    DoubleQlearn = 0
    Qlearn = 1


class Learner():
    def __init__(self, net: Net, learner: Learners, gamma: float = 0.99) -> None:
        self.net = net
        self.gamma = gamma
        self.criterion = MSELoss()
        self.optimizer = Adam(self.net.network.parameters(), lr=1e-4, weight_decay=1e-5)
        if learner == Learners.DoubleQlearn:
            self.learn = self.DoubleQlearn
        elif learner == Learners.Qlearn:
            self.learn = self.Qlearn

    def learn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        pass

    def DoubleQlearn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        vals_next = self.net.network(state_after)
        vals_target_next = self.net.target(state_after)
        value_next = torch.gather(vals_target_next, 2, torch.argmax(vals_next, 2).unsqueeze(2))
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1)
        td_guess = torch.gather(value_before, 2, action.long().view(-1, 1, 1)).view(-1)
        loss_value_network = self.criterion(td_guess, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

    def Qlearn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        vals_target_next = self.net.target(state_after)
        value_next = torch.max(vals_target_next, 1)
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1)
        td_guess = torch.gather(value_before, 2, action.long().view(-1, 1, 1)).view(-1)
        loss_value_network = self.criterion(td_guess, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
