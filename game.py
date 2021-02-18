import numpy as np
from torch import tensor, Tensor
from layers import Blocks, Player, Layer, Gold
from typing import List, Tuple


class Game:
    def __init__(self, batch: int = 5, hours: float = 1, width: int = 10, height: int = 10) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        self.layers: List[Layer] = [Player(batch, width, height), Blocks(batch, width, height), Gold(batch, width, height)]
        self._board = np.zeros((batch, len(self.layers), width, height), dtype=np.float32)
        for layer in self.layers:
            layer.update(self._board)

    @property
    def board(self) -> Tensor:
        return tensor(self._board)

    def step(action: List[int]) -> Tuple[Tensor, List[float], List[int], List[dict]]:
        pass
