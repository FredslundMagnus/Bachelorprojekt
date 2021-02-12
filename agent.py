from torch import cat
import torch.nn as nn


class Meta(nn.Module):
    def __init__(self):
        super(Meta, self).__init__()
        self.model = nn.Sequential(nn.Conv2d(3, 8, 3), nn.ReLU(), nn.Conv2d(8, 12, 3), nn.ReLU(), nn.Conv2d(12, 16, 3), nn.ReLU(), nn.Conv2d(16, 2, 4), nn.Flatten(), nn.Softmax(1))

    def forward(self, x):
        return self.model(x)

    def add_category(self):
        for p in [self.model[-3]._parameters[x] for x in ['bias', 'weight']]:
            p.data = cat((p.data, p.data[-1:]))
