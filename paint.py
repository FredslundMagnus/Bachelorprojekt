import pygame
from game import Game
from auxillaries import States


class Paint:
    @staticmethod
    def __init__(game: Game) -> None:
        Paint.screen.fill((100, 0, 200))
        Paint.pygame.display.update()
        Paint.pygame.time.delay(round(1000 / 60))

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
