import torch.nn as nn
from torch.nn import MSELoss
from torch.optim import Adam
from helper import device
import torch

class Network(nn.Module):
    def __init__(self, layers):
        super(Network, self).__init__()
        self.model = nn.Sequential(nn.Linear((len(layers)+1)*2, 128), nn.Dropout(0.3), nn.LeakyReLU(), nn.Linear(128, (len(layers)+1)*2), nn.Dropout(0.3), nn.LeakyReLU(), nn.Flatten())
        self.criterion = MSELoss()
        self.optimizer = Adam(self.model.parameters(), lr=1e-5, weight_decay=1e-5)
        self.counter = 0
        self.names = {}
        for key in layers:
            self.names[key.name] = len(self.names)

    def forward(self, data):
        return self.model(data)

    def learn(self, input, label):
        self.counter += 1
        guess = self.forward(input.unsqueeze(0))
        loss = self.criterion(guess, label.unsqueeze(0))
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()
        return loss.item()
        


class BayesionNN:
    def __init__(self, layers):
        self.network = Network(layers).to(device)
        self.names = {}
        for key in layers:
            self.names[key.name] = len(self.names)
        self.names["Goal"] = len(self.names)

    def convert_data(self, action, state, satisfied):
        input = torch.zeros(len(self.names)*2, device=device)
        label = torch.zeros(len(self.names)*2, device=device)
        for item in state:
            input[self.names[item.name]] = 1
            label[self.names[item.name]] = 1
        if satisfied == True:
            label[self.names[action.name]] = 1
        input[self.names[action.name] + len(self.names)] = 1


        return input, label


    def learn(self, action, state, satisfied):
        input, label = self.convert_data(action, state, satisfied)
        return self.network.learn(input, label)

    def predict(self, action, state, satisfied=True):
        input, label = self.convert_data(action, state, satisfied)
        return self.network.forward(input.unsqueeze(0)).detach()

    def predict_no_convert(self, action, state):
        state[0, self.names[action.name] + len(self.names)] = 1
        return self.network.forward(state).detach()
     