from typing import Iterator, Tuple
import pygame
from game import Game
from auxillaries import States
from colors import Color, Colors
from contextlib import contextmanager


@contextmanager
def screen(background: Color) -> None:
    Paint.screen.fill(background.color)
    try:
        yield
    finally:
        Paint.pygame.display.update()
        Paint.pygame.time.delay(round(1000 / 60))


class Paint:
    size = 50

    @staticmethod
    def __init__(game: Game) -> None:
        with screen(Colors.gray.c300):
            for color, size, x, y in game.layers.getColorable():
                Paint.drawRect(color, size, x, y)

    @staticmethod
    def drawRect(color: Color, size: int, x: int, y: int) -> None:
        Paint.pygame.draw.rect(Paint.screen, color.color, Paint.pygame.Rect(x*Paint.size + (Paint.size - size*Paint.size) // 2, y*Paint.size + (Paint.size - size*Paint.size) // 2, size*Paint.size, size*Paint.size))

    @staticmethod
    def start(width: int, height: int) -> None:
        Paint.screen = pygame.display.set_mode([width * Paint.size, height * Paint.size], vsync=True)
        States.draw = True

    @staticmethod
    def stop() -> None:
        States.draw = False
        Paint.pygame.quit()
        Paint.screen = None

    @staticmethod
    def switch(width: int, height: int) -> None:
        if States.draw:
            Paint.stop()
        else:
            Paint.start(width, height)


Paint.pygame = pygame
Paint.pygame.init()
