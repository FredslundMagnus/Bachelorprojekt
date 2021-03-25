from contextlib import contextmanager, redirect_stdout
from typing import List
from colors import Color, Colors
from helper import function
from layer import LayerType
from layer import LayerType
import threading
from abc import abstractproperty
from widgets import Slider

with redirect_stdout(None):
    import pygame


@contextmanager
def screen(background: Color) -> None:
    Graph.screen.fill(background.color)
    try:
        yield
    finally:
        try:
            Graph.pygame.display.update()
        except Exception as e:
            pass


class Node():
    def __init__(self, layer: LayerType) -> None:
        self.layer = layer
        self.x = 10 if layer.name == "Diamond1" else 5
        self.y = 10 if layer.name == "Diamond2" else 5
        self.name = layer.name


class Graph():
    size = 50
    dim = 0
    images = {}

    def __init__(self,  mainloop: function) -> None:
        self.data: dict = {}
        self.mainloop = mainloop
        self.slider = Slider(Graph.pygame)
        self.limit = 100
        self.start()

    def start(self):
        pygame.event.get()
        Graph.screen = pygame.display.set_mode([30 * Graph.size, 20 * Graph.size], vsync=True)
        for layer in LayerType:
            try:
                Graph.images[name] = Graph.pygame.transform.scale(Graph.pygame.image.load(f"Drawings/{(name := layer.name)}.png"), (Graph.size, Graph.size))
            except Exception as e:
                pass
        self.layers = self.mainloop({}, get_flippables=True)
        self.nodes = [Node(layer) for layer in self.layers]
        x = threading.Thread(target=self.mainloop, kwargs={'data': self.data})
        x.start()
        self.draw()
        x.do_run = False
        quit()

    @abstractproperty
    def updates(self) -> List[function]:
        pass

    def draw(self):
        run = True
        while run:
            for event in pygame.event.get():
                self.limit = self.slider.handle(event)
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    try:
                        self.updates[0].__call__()
                    except Exception as e:
                        print(e)
            with screen(Colors.gray.c300):
                self.slider.draw(Graph.screen)
                for node in self.nodes:
                    try:
                        Graph.drawImage(node.x, node.y, node.name)
                    except Exception as e:
                        pass
        Graph.pygame.quit()

    @staticmethod
    def drawImage(x: int, y: int, name: str) -> None:
        rect = Graph.pygame.Rect(x*Graph.size, y*Graph.size, Graph.size, Graph.size)
        Graph.screen.blit(Graph.images[(name)], rect)

    @staticmethod
    def drawRect(color: Color, size: int, x: int, y: int) -> None:
        rect = Graph.pygame.Rect(x*Graph.size + (Graph.size - size*Graph.size) // 2, y*Graph.size + (Graph.size - size*Graph.size) // 2, size*Graph.size, size*Graph.size)
        shape_surf = Graph.pygame.Surface(rect.size, Graph.pygame.SRCALPHA)
        Graph.pygame.draw.rect(shape_surf, color.color, shape_surf.get_rect())
        Graph.screen.blit(shape_surf, rect)

    @staticmethod
    def drawCircle(color: Color, size: int, x: int, y: int) -> None:
        Graph.pygame.draw.circle(Graph.screen, color.color, (x*Graph.size + Graph.size // 2, y*Graph.size + Graph.size // 2), size*Graph.size // 2)

    @staticmethod
    def write(text: str, x: float, y: float, size: int = 0.6, color: Color = Colors.gray.c900, center: bool = True) -> None:
        pygame.font.init()
        myfont = Graph.pygame.font.SysFont('Comic Sans MS', int(size * Graph.size))
        textsurface = myfont.render(text, True, color.color)
        width, height = textsurface.get_rect().right, textsurface.get_rect().bottom
        rect = Graph.pygame.Rect(x*Graph.size-width//2-Graph.size//10, y*Graph.size+Graph.size//10, width + Graph.size//5, height-Graph.size//10)
        shape_surf = Graph.pygame.Surface(rect.size, Graph.pygame.SRCALPHA)
        Graph.pygame.draw.rect(shape_surf, Colors.white.transparrent(150).color, shape_surf.get_rect())
        Graph.screen.blit(shape_surf, rect)
        Graph.screen.blit(textsurface, (x*Graph.size - (textsurface.get_width()/2)*center, y*Graph.size))


Graph.pygame = pygame
Graph.pygame.init()
Graph.clock = Graph.pygame.time.Clock()
