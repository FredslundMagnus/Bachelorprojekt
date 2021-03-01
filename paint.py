from layer import Shape
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
    def __init__(game: Game, frame: int) -> None:
        with screen(Colors.gray.c300):
            for shape, color, size, x, y in game.layers.getColorable():
                if shape == Shape.Circle:
                    Paint.drawCircle(color, size, x, y)
                elif shape == Shape.Square:
                    Paint.drawRect(color, size, x, y)
            Paint.write(f"Frames: {frame}", game.layers.width/2, 0)

    @staticmethod
    def drawRect(color: Color, size: int, x: int, y: int) -> None:
        Paint.pygame.draw.rect(Paint.screen, color.color, Paint.pygame.Rect(x*Paint.size + (Paint.size - size*Paint.size) // 2, y*Paint.size + (Paint.size - size*Paint.size) // 2, size*Paint.size, size*Paint.size))

    @staticmethod
    def drawCircle(color: Color, size: int, x: int, y: int) -> None:
        Paint.pygame.draw.circle(Paint.screen, color.color, (x*Paint.size + Paint.size // 2, y*Paint.size + Paint.size // 2), size*Paint.size // 2)

    @staticmethod
    def start(width: int, height: int) -> None:
        Paint.screen = pygame.display.set_mode([width * Paint.size, height * Paint.size], vsync=True)
        States.draw = True

    @staticmethod
    def write(text: str, x: float, y: float, size: int = 30, color: Color = Colors.gray.c900, center: bool = True) -> None:
        pygame.font.init()
        myfont = Paint.pygame.font.SysFont('Comic Sans MS', size)
        textsurface = myfont.render(text, True, color.color)
        Paint.screen.blit(textsurface, (x*Paint.size - (textsurface.get_width()/2)*center, y*Paint.size))

    @ staticmethod
    def stop() -> None:
        States.draw = False
        Paint.pygame.quit()
        Paint.screen = None

    @ staticmethod
    def switch(width: int, height: int) -> None:
        if States.draw:
            Paint.stop()
        else:
            Paint.start(width, height)


Paint.pygame = pygame
Paint.pygame.init()
