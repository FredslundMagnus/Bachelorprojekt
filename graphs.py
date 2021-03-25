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
    def __init__(self, layer: LayerType, index: float) -> None:
        self.layer = layer
        self.value = index
        self.x = 10
        self.y = 500


class Graph():
    size = 80
    dim = 0
    images = {}

    def __init__(self,  mainloop: function) -> None:
        self.data: dict = {}
        self.mainloop = mainloop
        self.slider = Slider(Graph.pygame, 1400, Colors.blue)
        self.slider2 = Slider(Graph.pygame, 1450, Colors.green)
        self.limit = 100
        self.start()

    def start(self):
        pygame.event.get()
        Graph.screen = pygame.display.set_mode([1500, 1000], vsync=True)
        for layer in LayerType:
            try:
                Graph.images[name] = Graph.pygame.transform.scale(Graph.pygame.image.load(f"Drawings/{(name := layer.name)}.png"), (Graph.size, Graph.size))
            except Exception as e:
                pass
        self.layers = self.mainloop({}, get_flippables=True)
        self.nodes = [Node(layer, i) for i, layer in enumerate(self.layers)]
        x = threading.Thread(target=self.mainloop, kwargs={'data': self.data})
        x.start()
        self.draw()
        x.do_run = False
        quit()

    @abstractproperty
    def updateNotes(self) -> List[function]:
        pass

    def draw(self):
        run = True
        while run:
            for event in pygame.event.get():
                self.limit = self.slider.handle(event)
                self.diff = self.slider2.handle(event)
                if event.type == pygame.QUIT:
                    run = False
            try:
                self.updateNotes[0].__call__(self.nodes)
            except Exception as e:
                pass
            with screen(Colors.gray.c300):
                self.slider.draw(Graph.screen)
                self.slider2.draw(Graph.screen)
                try:
                    Graph.drawNodes(self.nodes, self.diff/100)
                except Exception as e:
                    print("d", e)

        Graph.pygame.quit()

    @staticmethod
    def drawNodes(nodes: List[Node], limit):
        start, end = 350, 1150
        values = [node.value for node in nodes]
        for node in nodes:
            node.y = 500
            node.x = ((node.value - min(values))/(max(values)-min(values))) * (end - start) + start
        diff_check = (end - start)*limit

        li = list(sorted(nodes, key=lambda x: x.x, reverse=True))
        for node1, node2 in zip(li[:-1], li[1:]):
            if (diff := Graph.dist(node1, node2)) < diff_check:
                if node1.y > 500:
                    node1.y += (diff_check - diff)/2
                    node2.y -= (diff_check - diff)/2
                else:
                    node1.y -= (diff_check - diff)/2
                    node2.y += (diff_check - diff)/2

        for node in nodes:
            node.y -= (node.y - 500)*0.05

        for node in nodes:
            Graph.drawNode(node)

    @staticmethod
    def dist(node1: Node, node2: Node) -> float:
        return ((node1.x - node2.x)**2 + (node1.y - node2.y)**2)**(1/2)

    @staticmethod
    def drawNode(node: Node):
        Graph.drawImage(node.x, node.y, node.layer.name)

    @staticmethod
    def drawImage(x: int, y: int, name: str) -> None:
        rect = Graph.pygame.Rect(x, y, Graph.size, Graph.size)
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
