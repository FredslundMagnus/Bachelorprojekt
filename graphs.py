from contextlib import contextmanager, redirect_stdout
from typing import List
from colors import Color, Colors
from helper import function
from layer import LayerType
from layer import LayerType
import threading
from abc import abstractproperty
from widgets import Menu, Slider
import math
with redirect_stdout(None):
    import pygame
    import pygame.gfxdraw


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


class Edge():
    def __init__(self, fra: Node, til: Node, index: float) -> None:
        self.fra = fra
        self.til = til
        self.value = index
        self.opacity = 1


class Graph():
    size = 80
    dim = 0
    images = {}

    def __init__(self,  mainloop: function) -> None:
        self.data: dict = {}
        self.mainloop = mainloop
        self.widgets = {
            "Slider0": Slider(Graph.pygame, 1350, Colors.brown, start=20),
            "Slider1": Slider(Graph.pygame, 1400, Colors.blue, start=40),
            "Slider2": Slider(Graph.pygame, 1450, Colors.orange, start=30),
            "Menu": Menu(Graph.pygame, self.updateEdges, self.updateNotes, Colors.green, 300, Colors.blue),
        }
        self.start()

    def start(self):
        pygame.event.get()
        Graph.screen = pygame.display.set_mode([1500, 1000], vsync=True)
        for layer in LayerType:
            try:
                Graph.images[name] = Graph.pygame.transform.scale(Graph.pygame.image.load(f"Drawings/{(name := layer.name)}.png"), (80, 80))
            except Exception as e:
                pass
        self.layers = self.mainloop({}, get_flippables=True)
        self.nodes = [Node(layer, i) for i, layer in enumerate(self.layers)]
        self.edges = [Edge(node1, node2, i) for i, node2 in enumerate(self.nodes) for node1 in self.nodes if node1.layer != node2.layer]
        x = threading.Thread(target=self.mainloop, kwargs={'data': self.data})
        x.start()
        self.draw()
        x.do_run = False
        quit()

    @abstractproperty
    def updateNotes(self) -> List[function]:
        pass

    @abstractproperty
    def updateEdges(self) -> List[function]:
        pass

    def draw(self):
        run = True
        while run:
            for event in pygame.event.get():
                for widget in self.widgets.values():
                    widget.handle(event)
                if event.type == pygame.QUIT:
                    run = False
            try:
                self.updateNotes[self.widgets["Menu"][0]].__call__(self.nodes)
                self.updateEdges[self.widgets["Menu"][1]].__call__(self.edges)
            except Exception as e:
                print(e)
            with screen(Colors.gray.c300):
                for widget in self.widgets.values():
                    widget.draw(Graph.screen)
                try:
                    Graph.drawEdges(self.edges, self.widgets["Slider1"].value/100, self.widgets["Slider0"].value/100, self.widgets["Slider2"].value/100)
                    Graph.drawNodes(self.nodes, self.widgets["Slider2"].value/100)
                except Exception as e:
                    print("d", e)

        Graph.pygame.quit()

    @staticmethod
    def drawNodes(nodes: List[Node], limit: float):
        start, end = 425, 1225
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
    def drawEdges(edges: List[Edge], limit: float, cutoff: float, diff: float):
        li = [edge.value for edge in edges]
        ma, mi = max(li), min(li)
        for edge in edges:
            if ma > mi:
                edge.opacity = edge.value / ma
            if edge.opacity > cutoff:
                Graph.drawEdge(edge, limit, diff)

    @staticmethod
    def drawEdge(edge: Edge, curve, diff):
        Graph.drawArc(edge.fra.x, edge.til.x, edge.fra.y, edge.til.y, curve * min(max((Graph.dist(edge.fra, edge.til)-400*diff) / (800*(1.01-diff)), 0), 1), edge.opacity * 10, Colors.red.transparrent(edge.opacity*255).color if edge.fra.x > edge.til.x else Colors.green.transparrent(edge.opacity*255).color)

    @staticmethod
    def drawArc(x1, x2, y1, y2, curve, width, color):
        # Graph.drawCircle(Colors.orange, 5, x1-200, y1-200)
        # Graph.drawCircle(Colors.black, 5, x2-200, y2-200)
        mid_x = (x1+x2)/2
        mid_y = (y1+y2)/2
        vector = [(y2-y1)/2, -(x2-x1)/2]
        # Graph.drawCircle(Colors.black, 5, mid_x-200, mid_y-200)
        # Graph.drawCircle(Colors.black, 5, mid_x+vector[0]*curve-200, mid_y+vector[1]*curve-200)
        if temp := Graph.calculateRadius((x1, y1), (x2, y2), (mid_x+vector[0]*curve, mid_y+vector[1]*curve)):
            r, x, y = temp
            r += width/2
            # Graph.drawCircle(Colors.brown, 5, x, y)
            start, stop = math.atan2(y1-y, x1-x), math.atan2(y2-y, x2-x)
            if start > stop:
                start -= math.pi*2
            points_outer = []
            points_inner = []
            n = round(r*abs(stop-start)/20)
            if n < 2:
                n = 2
            for i in range(n):
                delta = i/(n-1)
                phi0 = start + (stop-start)*delta
                x0 = round(x+r*math.cos(phi0))
                y0 = round(y+r*math.sin(phi0))
                points_outer.append([x0, y0])
                phi1 = stop + (start-stop)*delta
                x1 = round(x+(r-width)*math.cos(phi1))
                y1 = round(y+(r-width)*math.sin(phi1))
                points_inner.append([x1, y1])
            points = points_outer + points_inner

            Graph.pygame.gfxdraw.aapolygon(Graph.screen, points, color)
            Graph.pygame.gfxdraw.filled_polygon(Graph.screen, points, color)
        else:
            Graph.pygame.draw.line(Graph.screen, color, (int(x1), int(y1)), (int(x2), int(y2)), int(width))

    @staticmethod
    def calculateRadius(b, c, d):
        temp = c[0]**2 + c[1]**2
        bc = (b[0]**2 + b[1]**2 - temp) / 2
        cd = (temp - d[0]**2 - d[1]**2) / 2
        det = (b[0] - c[0]) * (c[1] - d[1]) - (c[0] - d[0]) * (b[1] - c[1])

        if abs(det) < 1.0e-10:
            return None

        # Center of circle
        cx = (bc*(c[1] - d[1]) - cd*(b[1] - c[1])) / det
        cy = ((b[0] - c[0]) * cd - (c[0] - d[0]) * bc) / det

        radius = ((cx - b[0])**2 + (cy - b[1])**2)**.5

        return radius, cx, cy

    @staticmethod
    def drawNode(node: Node):
        Graph.drawCircle(Colors.black, 110, node.x, node.y)
        Graph.drawCircle(Colors.white, 95, node.x, node.y)
        Graph.drawImage(node.x, node.y, node.layer.name, 80)

    @staticmethod
    def drawImage(x: int, y: int, name: str, size: int) -> None:
        rect = Graph.pygame.Rect(x-size//2, y-size//2, size, size)
        Graph.screen.blit(Graph.images[(name)], rect)

    @staticmethod
    def drawRect(color: Color, size: int, x: int, y: int) -> None:
        rect = Graph.pygame.Rect(x*Graph.size + (Graph.size - size*Graph.size) // 2, y*Graph.size + (Graph.size - size*Graph.size) // 2, size*Graph.size, size*Graph.size)
        shape_surf = Graph.pygame.Surface(rect.size, Graph.pygame.SRCALPHA)
        Graph.pygame.draw.rect(shape_surf, color.color, shape_surf.get_rect())
        Graph.screen.blit(shape_surf, rect)

    @staticmethod
    def drawCircle(color: Color, size: int, x: int, y: int) -> None:
        Graph.pygame.draw.circle(Graph.screen, color.color, (x, y), size // 2)

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
