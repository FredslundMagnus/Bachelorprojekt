import time
import os
from layer import Shape
from typing import Iterator, Tuple
from game import Game
from auxillaries import States
from colors import Color, Colors
from contextlib import contextmanager, redirect_stdout
with redirect_stdout(None):
    import pygame


@contextmanager
def screen(background: Color) -> None:
    Paint.screen.fill(background.color)
    try:
        yield
    finally:
        try:
            Paint.pygame.display.update()
            # if States.slow:
            #     Paint.pygame.time.delay(round(200))
        except Exception as e:
            pass


class Paint:
    size = 50
    dim = 0
    x = 0
    y = 0

    @staticmethod
    def __init__(game: Game, frame: int, teleporter) -> None:
        with screen(Colors.gray.c300):
            for shape, color, size, x, y, name in game.layers.getColorable(Paint.dim):
                try:
                    Paint.drawImage(x, y, name)
                except Exception as e:
                    try:
                        if shape == Shape.Circle:
                            Paint.drawCircle(color, size, x, y)
                        elif shape == Shape.Square:
                            Paint.drawRect(color, size, x, y)
                    except Exception as e:
                        pass
            try:
                Paint.write(f"Frames: {frame}", game.layers.width/2, 0)
                Paint.write(f"Game: {Paint.dim}", game.layers.width/2, game.layers.height-1)
            except Exception as e:
                pass
            if teleporter != None:
                y, x = divmod(int(teleporter.interventions[Paint.dim]), game.layers.width)
                try:
                    Paint.drawImage(x, y, "Cheese")
                except Exception as e:
                    try:
                        Paint.drawRect(Colors.indigo.transparrent(180), 1, x, y)
                    except Exception as e:
                        pass

    @staticmethod
    def drawImage(x: int, y: int, name: str) -> None:
        if not States.slow:
            raise Exception()
        myimage = Paint.pygame.transform.scale(Paint.pygame.image.load(f"Drawings/{name}.png"), (Paint.size, Paint.size))
        rect = Paint.pygame.Rect(x*Paint.size + (Paint.size - Paint.size) // 2, y*Paint.size + (Paint.size - Paint.size) // 2, Paint.size, Paint.size)
        Paint.screen.blit(myimage, rect)

    @staticmethod
    def drawRect(color: Color, size: int, x: int, y: int) -> None:
        rect = Paint.pygame.Rect(x*Paint.size + (Paint.size - size*Paint.size) // 2, y*Paint.size + (Paint.size - size*Paint.size) // 2, size*Paint.size, size*Paint.size)
        shape_surf = Paint.pygame.Surface(rect.size, Paint.pygame.SRCALPHA)
        Paint.pygame.draw.rect(shape_surf, color.color, shape_surf.get_rect())
        Paint.screen.blit(shape_surf, rect)

    @staticmethod
    def drawCircle(color: Color, size: int, x: int, y: int) -> None:
        Paint.pygame.draw.circle(Paint.screen, color.color, (x*Paint.size + Paint.size // 2, y*Paint.size + Paint.size // 2), size*Paint.size // 2)

    @staticmethod
    def start(width: int, height: int) -> None:
        Paint.screen = pygame.display.set_mode([width * Paint.size, height * Paint.size], vsync=True)
        States.draw = True

    @staticmethod
    def write(text: str, x: float, y: float, size: int = 0.6, color: Color = Colors.gray.c900, center: bool = True) -> None:
        pygame.font.init()
        myfont = Paint.pygame.font.SysFont('Comic Sans MS', int(size * Paint.size))
        textsurface = myfont.render(text, True, color.color)
        if States.slow:
            width, height = textsurface.get_rect().right, textsurface.get_rect().bottom
            rect = Paint.pygame.Rect(x*Paint.size-width//2-Paint.size//10, y*Paint.size+Paint.size//10, width + Paint.size//5, height-Paint.size//10)
            shape_surf = Paint.pygame.Surface(rect.size, Paint.pygame.SRCALPHA)
            Paint.pygame.draw.rect(shape_surf, Colors.white.transparrent(150).color, shape_surf.get_rect())
            Paint.screen.blit(shape_surf, rect)
        Paint.screen.blit(textsurface, (x*Paint.size - (textsurface.get_width()/2)*center, y*Paint.size))

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

    @staticmethod
    def move(x: int, y: int, width: int, height: int) -> None:
        Paint.y += y
        Paint.x += x
        if States.draw:
            Paint.stop()
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Paint.x, Paint.y)
            Paint.pygame.init()
            Paint.start(width, height)
        else:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Paint.x, Paint.y)
            Paint.pygame.init()

    @staticmethod
    def zoom(zoom: int, width: int, height: int) -> None:
        if States.draw:
            Paint.stop()
            Paint.size += zoom
            Paint.pygame.init()
            Paint.start(width, height)
        else:
            Paint.size += zoom


Paint.pygame = pygame
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (Paint.x, Paint.y)
Paint.pygame.init()
