import numpy as np
from torch import tensor, Tensor


class Game:
    def __init__(self, batch: int = 1, hours: float = 1) -> None:
        super().__init__()
        self.batch: int = batch
        self.hours: float = hours
        self._board = np.zeros((batch, 3, 10, 10), dtype=np.float32)
        self._board[:, 0, 0, :] = 1
        self._board[:, 0, -1, :] = 1
        self._board[:, 0, :, 0] = 1
        self._board[:, 0, :, -1] = 1

    @property
    def board(self) -> Tensor:
        return tensor(self._board)
