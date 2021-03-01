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
    def __init__(self, net: Net, learner: Learners, gamma: float = None, **kwargs) -> None:
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
        vals_next = torch.flatten(self.net.network(state_after), start_dim=1)
        vals_target_next = torch.flatten(self.net.target(state_after), start_dim=1)
        value_next = torch.gather(vals_target_next, 0, torch.argmax(vals_next, 1).unsqueeze(1))
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1).detach()
        loss_value_network = self.criterion(value_before, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

    def Qlearn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        vals_target_next = torch.flatten(self.net.target(state_after), start_dim=1)
        value_next, _ = torch.max(vals_target_next, 1)
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1).detach()
        loss_value_network = self.criterion(value_before, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
