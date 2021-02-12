import pygame
from game import Game
from auxillaries import States
from colors import Color, Colors
from contextlib import contextmanager


@contextmanager
def screen(background: Color):
    Paint.screen.fill(background.color)
    try:
        yield
    finally:
        Paint.pygame.display.update()
        Paint.pygame.time.delay(round(1000 / 60))


class Paint:
    @staticmethod
    def __init__(game: Game) -> None:
        with screen(Colors.gray.c300):
            Paint.drawRect(Colors.red, 5, 5)
            Paint.drawRect(Colors.blue, 5, 5, 40)

    @staticmethod
    def drawRect(color: Color, x: int, y: int, size: int = 50):
        Paint.pygame.draw.rect(Paint.screen, color.color, Paint.pygame.Rect(x*50 + (50 - size) // 2, y*50 + (50 - size) // 2, size, size))

    @staticmethod
    def start():
        Paint.screen = pygame.display.set_mode([500, 500])
        States.draw = True

    @staticmethod
    def stop():
        States.draw = False
        Paint.pygame.quit()
        Paint.screen = None

    @staticmethod
    def switch():
        if States.draw:
            Paint.stop()
        else:
            Paint.start()


Paint.pygame = pygame
Paint.pygame.init()
