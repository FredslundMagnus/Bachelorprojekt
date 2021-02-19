from torch import tensor, Tensor
from layers import Layers, LayerType
from typing import List, Tuple


class Game:
    def __init__(self, batch: int = 5, hours: float = 1, width: int = 10, height: int = 10) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        self.layers: Layers = Layers(batch, width, height, LayerType.Blocks, LayerType.Gold, LayerType.Goal, LayerType.Keys, LayerType.Door)
        self.layers.update()

    @property
    def board(self) -> Tensor:
        return tensor(self.layers.board)

    def step(self, action: List[int]) -> Tuple[Tensor, List[float], List[int], List[dict]]:
        self.layers.step(action)
