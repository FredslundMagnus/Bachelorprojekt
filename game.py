import numpy as np
from torch import tensor


class Game:
    def __init__(self, n=1) -> None:
        super().__init__()
        self.n = n
        self._board = np.zeros((n, 3, 10, 10), dtype=np.float32)

    def change(self):
        for i in range(self.n):
            self._board[i, :, :, :] = np.zeros((3, 10, 10), dtype=np.float32) + 1

    @property
    def board(self):
        return tensor(self._board)
