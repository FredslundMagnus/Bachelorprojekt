from typing import List


class Collector:
    def __init__(self) -> None:
        self.rewards = []
        self.dones = []

    def show(self, game) -> None:
        pass

    def collect(self, rewards: List[float], dones: List[int]):
        self.rewards.append(sum(rewards)/len(rewards))
        self.dones.append(sum(dones)/len(dones))
        pass
