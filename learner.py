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
        self.counter = 0

    def learn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        pass

    def DoubleQlearn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.counter += 1
        vals_next = self.net.network(state_after)
        vals_target_next = self.net.target(state_after)
        value_next = torch.gather(vals_target_next, 0, torch.argmax(vals_next, 1).unsqueeze(1)).squeeze(1)
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1).detach()
        action_value_before = torch.gather(value_before, 1, action.unsqueeze(1)).squeeze(1)
        loss_value_network = self.criterion(action_value_before, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

    def Qlearn(self, value_before: Tensor, state_after: Tensor, action: Tensor, reward: Tensor, done: Tensor):
        self.counter += 1
        vals_target_next = self.net.target(state_after)
        value_next, _ = torch.max(vals_target_next, 1)
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1).detach()
        #print(state_after[0])
        action_value_before = torch.gather(value_before, 1, action.unsqueeze(1)).squeeze(1)
        #if self.counter % 100 == 0:
        #    print(action.unsqueeze(1)[0], value_before[0], td_target[0])
        loss_value_network = self.criterion(action_value_before, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
