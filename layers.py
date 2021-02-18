from layer import Layer
from colors import Colors


class Player(Layer):
    color = Colors.green
    size = 1

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (2, 3))


class Blocks(Layer):
    color = Colors.gray
    size = 1

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        for x, y in self.grid():
            if x == 0 or x == self._width-1 or y == 0 or y == self._height-1:
                self.add(batch, (x, y))


class Gold(Layer):
    color = Colors.yellow
    size = 0.6

    def __init__(self, batch: int, width: int, height: int) -> None:
        super().__init__(batch, width, height)

    def reset(self, batch: int) -> None:
        self.add(batch, (4, 5))
