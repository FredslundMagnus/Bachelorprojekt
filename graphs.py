from contextlib import contextmanager, redirect_stdout
from typing import List
from colors import Color, Colors
from helper import function
from layer import LayerType
from layer import LayerType
import threading
from abc import abstractproperty
from widgets import Menu, Slider, Toggle
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

    def __init__(self,  mainloop: function, layers: List[LayerType], usePlayer=True) -> None:
        self.data: dict = {}
        self.layers = layers + ([LayerType.Player, LayerType.Goal] if usePlayer else [LayerType.Goal])
        self.mainloop = mainloop
        self.isMinimised = False
        self.widgets = {
            "Slider0": Slider(Graph.pygame, 1350, Colors.brown, start=20),
            "Slider1": Slider(Graph.pygame, 1400, Colors.blue, start=40),
            "Slider2": Slider(Graph.pygame, 1450, Colors.orange, start=14),
            "Menu": Menu(Graph.pygame, self.updateEdges, self.updateNotes, Colors.green, 300, Colors.blue),
            "Toggle": Toggle(Graph.pygame, Colors.green)
        }
        self.start()

    def minimize(self, nodes):
        if self.widgets["Toggle"].active:
            maxi = max([node.value for node in nodes])
            li = [[] for _ in range(maxi+1)]
            for node in nodes:
                li[node.value].append(node)

            li = [e for e in li if e]
            for i, _nodes in enumerate(li):
                for node in _nodes:
                    node.value = i

    def start(self):
        pygame.event.get()
        Graph.screen = pygame.display.set_mode([1500, 1000], vsync=True)
        for layer in LayerType:
            try:
                Graph.images[name] = Graph.pygame.transform.scale(Graph.pygame.image.load(f"Drawings/{(name := layer.name)}.png"), (80, 80))
            except Exception as e:
                pass
        self.nodes = [Node(layer, i) for i, layer in enumerate(self.layers)]
        self.edges = [Edge(node1, node2, i) for i, node2 in enumerate(self.nodes) for node1 in self.nodes if node1.layer != node2.layer]
        self.x = threading.Thread(target=self.mainloop, kwargs={'data': self.data})
        self.x.start()
        self.draw()
        self.x.do_run = False
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
            self.isMinimised = self.widgets["Toggle"].active
            for event in pygame.event.get():
                for widget in self.widgets.values():
                    widget.handle(event)
                if event.type == pygame.QUIT:
                    run = False
            try:
                self.updateNotes[self.widgets["Menu"][0]].__call__(self.nodes)
                self.updateEdges[self.widgets["Menu"][1]].__call__(self.edges)
            except Exception as e:
                pass
            with screen(Colors.white):
                if (frame := getattr(self.x, 'frame', 0)) != 0:
                    Graph.write(f"Iteration {frame}", 825, 20, size=50)
                for widget in self.widgets.values():
                    widget.draw(Graph.screen)
                try:
                    Graph.drawEdges(self.edges, self.widgets["Slider1"].value/100, self.widgets["Slider0"].value/100, self.widgets["Slider2"].value/100)
                    Graph.drawNodes(self.nodes, self.widgets["Slider2"].value/100)
                except Exception as e:
                    pass

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
                    node1.y += (diff_check - diff)/2 * 2
                    node2.y -= (diff_check - diff)/2 * 2
                else:
                    node1.y -= (diff_check - diff)/2 * 2
                    node2.y += (diff_check - diff)/2 * 2

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
                edge.opacity = edge.value
            if edge.opacity > cutoff:
                Graph.drawEdge(edge, limit, diff)

    @staticmethod
    def drawEdge(edge: Edge, curve, diff):
        Graph.drawArc(edge.fra.x, edge.til.x, edge.fra.y, edge.til.y, curve * min(max((Graph.dist(edge.fra, edge.til)-400*diff) / (800*(1.01-diff)), 0), 1), edge.opacity * 10, Colors.gray.c900.transparrent(edge.opacity*255).color)  # Colors.red.transparrent(edge.opacity*255).color if edge.fra.x > edge.til.x else Colors.green.transparrent(edge.opacity*255).color

    @staticmethod
    def drawArc(x1, x2, y1, y2, curve, width, color):
        size = 20
        # Graph.drawCircle(Colors.orange, 5, x1, y1)
        # Graph.drawCircle(Colors.black, 5, x2, y2)
        mid_x = (x1+x2)/2
        mid_y = (y1+y2)/2
        vector = [(y2-y1)/2, -(x2-x1)/2]
        # Graph.drawCircle(Colors.black, 5, mid_x, mid_y)
        # Graph.drawCircle(Colors.black, 5, mid_x+vector[0]*curve, mid_y+vector[1]*curve)
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
            r = (r-width/2)
            phi = stop-(55) / r
            x = round(x+r*math.cos(phi))
            y = round(y+r*math.sin(phi))
            # Graph.drawCircle(Colors.pink, 10, x, y)
            # Graph.drawCircle(Colors.pink, 10, x + 40 * math.cos(phi), y + 40 * math.sin(phi))
            # Graph.drawCircle(Colors.pink, 10, x - 40 * math.cos(phi), y - 40 * math.sin(phi))
            # Graph.drawCircle(Colors.pink, 10, x + 40 * math.sin(phi), y - 40 * math.cos(phi))
            # Graph.drawCircle(Colors.pink, 10, x + size * (math.cos(phi) + math.sin(phi)), y + size * (math.sin(phi) - math.cos(phi)))
            # Graph.drawCircle(Colors.pink, 10, x - size * (math.cos(phi) - math.sin(phi)), y - size * (math.sin(phi) + math.cos(phi)))
            Graph.drawLine(color, x, y, x + size * (math.cos(phi) + math.sin(phi)), y + size * (math.sin(phi) - math.cos(phi)), int(width))
            Graph.drawLine(color, x, y, x - size * (math.cos(phi) - math.sin(phi)), y - size * (math.sin(phi) + math.cos(phi)), int(width))
        else:
            Graph.pygame.draw.line(Graph.screen, color, (int(x1), int(y1)), (int(x2), int(y2)), int(width))
            v = [x1-x2, y1-y2]
            l = sum([c*c for c in v])**(1/2)
            try:
                v = [c/l for c in v]
                Graph.drawLine(color, x2 + 55 * v[0], y2 + 55 * v[1], x2 + (size + 55) * v[0] + size * v[1], y2 + (size + 55) * v[1] - size * v[0], int(width))
                Graph.drawLine(color, x2 + 55 * v[0], y2 + 55 * v[1], x2 + (size + 55) * v[0] - size * v[1], y2 + (size + 55) * v[1] + size * v[0], int(width))
            except Exception as e:
                pass

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
        Graph.drawCircle(Colors.gray.c900, 110, node.x, node.y)
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
    def write(text: str, x: float, y: float, size: int = 20, color: Color = Colors.gray.c900, center: bool = True) -> None:
        Graph.pygame.font.init()
        myfont = Graph.pygame.font.SysFont('Comic Sans MS', int(size))
        textsurface = myfont.render(text, True, color.color)
        width, height = textsurface.get_rect().right, textsurface.get_rect().bottom
        rect = Graph.pygame.Rect(x-width//2, y, width, height)
        shape_surf = Graph.pygame.Surface(rect.size, Graph.pygame.SRCALPHA)
        Graph.screen.blit(shape_surf, rect)
        Graph.screen.blit(textsurface, (x - (textsurface.get_width()/2)*center, y))

    @staticmethod
    def drawLine(color, x0: float, y0: float, x1: float, y1: float, width: float) -> None:
        v = [x0-x1, y0-y1]
        l = sum([c*c for c in v])**(1/2)
        v = [c/l for c in v]
        w = width/2
        v1 = [x0 + w * (v[0] + v[1]), y0 + w * (v[1] - v[0])]
        v2 = [x0 + w * (v[0] - v[1]), y0 + w * (v[1] + v[0])]
        v3 = [x1 - w * (v[0] + v[1]), y1 - w * (v[1] - v[0])]
        v4 = [x1 - w * (v[0] - v[1]), y1 - w * (v[1] + v[0])]
        Graph.pygame.gfxdraw.aapolygon(Graph.screen, (v1, v2, v3, v4), color)
        Graph.pygame.gfxdraw.filled_polygon(Graph.screen, (v1, v2, v3, v4), color)
        # Graph.pygame.draw.polygon(Graph.screen, color, )
        # Graph.pygame.draw.aaline(Graph.screen, color, (x0, y0), (x1, y1), width)


Graph.pygame = pygame
Graph.pygame.init()
Graph.clock = Graph.pygame.time.Clock()
