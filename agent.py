from network import Net, Networks
from game import Game


class Agent:
    def __init__(self, game: Game, network: Networks = Networks.Small) -> None:
        self.net = Net(len(game.layers), network)

    def __call__(self, frame):
        return self.net.network(frame)
