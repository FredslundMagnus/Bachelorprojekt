from torch import tensor, Tensor
from helper import device
from layers import Layers, LayerType
from typing import List, Tuple


class Game:
    def __init__(self, batch: int = None, hours: float = None, width: int = None, height: int = None, reset_chance: float = None, **kwargs) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        self.layers: Layers = Layers(batch, width, height, reset_chance, LayerType.Player, LayerType.Goal)
        self.layers.update()

    @property
    def board(self) -> Tensor:
        return tensor(self.layers.board, device=device)

    def step(self, action: Tensor) -> Tuple[Tensor, Tensor, Tensor]:
        rewards, dones = self.layers.step(action.tolist())
        return self.board, tensor(rewards, device=device), tensor(dones, device=device)
