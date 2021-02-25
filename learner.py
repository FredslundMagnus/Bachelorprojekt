from auxillaries import device
import torch


class Learners():
    def __init__(self) -> None:
        self.counter = 1

    def DoubleQlearn(self, state_before, state_after, action, reward, done):
        vals = self.network(state_before)
        vals_next = self.network(state_after)
        vals_target_next = self.target_network(state_after)
        value_next = torch.gather(vals_target_next, 2, torch.argmax(vals_next, 2).unsqueeze(2))
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1)
        td_guess = torch.gather(vals, 2, action.long().view(-1, 1, 1)).view(-1)
        loss_value_network = self.criterion(td_guess, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        self.counter += 1

    def Qlearn(self, state_before, state_after, action, reward, done):
        vals = self.network(state_before)
        vals_target_next = self.target_network(state_after)
        value_next = torch.max(vals_target_next, 1)
        td_target = (value_next.view(-1) * self.gamma * (1 - done) + reward).view(-1)
        td_guess = torch.gather(vals, 2, action.long().view(-1, 1, 1)).view(-1)
        loss_value_network = self.criterion(td_guess, td_target)
        loss_value_network.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        self.counter += 1
