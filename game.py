from numpy import stack, zeros, float32
from torch import tensor


class Game:
    def __init__(self) -> None:
        super().__init__()
        self._board = zeros((3, 10, 10), dtype=float32)

    @property
    def board(self):
        return tensor(stack([self._board]))
