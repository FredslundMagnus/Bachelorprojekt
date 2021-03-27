from typing import List
from colors import MaterialColor, Color, Colors
from abc import abstractmethod
from helper import function


class Widget:
    @abstractmethod
    def handle(self, event) -> None:
        pass

    @abstractmethod
    def draw(self, screen) -> None:
        pass

    def write(self, screen, text: str, x: float, y: float, size: int = 20, color: Color = Colors.gray.c900, center: bool = True) -> None:
        self.pygame.font.init()
        myfont = self.pygame.font.SysFont('Comic Sans MS', int(size))
        textsurface = myfont.render(text, True, color.color)
        width, height = textsurface.get_rect().right, textsurface.get_rect().bottom
        rect = self.pygame.Rect(x-width//2, y, width, height)
        shape_surf = self.pygame.Surface(rect.size, self.pygame.SRCALPHA)
        screen.blit(shape_surf, rect)
        screen.blit(textsurface, (x - (textsurface.get_width()/2)*center, y))


class Slider(Widget):
    def __init__(self, pygame, x, color: MaterialColor, start=0) -> None:
        self.isHolding = False
        self.pygame = pygame
        self.circle_y = 900 - 8*start
        self.color = color
        self.value = start
        self.sliderRect = pygame.Rect(x, 100, 10, 800)

    def draw(self, screen) -> None:
        self.pygame.draw.circle(screen, self.color.c200.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.sliderRect.y), self.sliderRect.w / 2)
        self.pygame.draw.rect(screen, self.color.c200.color, self.pygame.Rect(self.sliderRect.x, self.sliderRect.y, self.sliderRect.w, self.circle_y-self.sliderRect.y))
        self.pygame.draw.circle(screen, self.color.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.sliderRect.y + self.sliderRect.h), self.sliderRect.w/2)
        self.pygame.draw.rect(screen, self.color.color, self.pygame.Rect(self.sliderRect.x, self.circle_y, self.sliderRect.w, self.sliderRect.h - self.circle_y+self.sliderRect.y))
        self.pygame.draw.circle(screen, self.color.c700.color if self.isHolding else self.color.c600.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.circle_y), self.sliderRect.w * 1.5)

    def update_value(self, y):
        if y < self.sliderRect.y:
            self.value = 100
        elif y > self.sliderRect.y + self.sliderRect.h:
            self.value = 0
        else:
            self.value = 100 - (y - self.sliderRect.y) / float(self.sliderRect.h) * 100

    def on_slider(self, x, y):
        if ((x - self.sliderRect.x - self.sliderRect.w / 2) * (x - self.sliderRect.x - self.sliderRect.w / 2) + (y - self.circle_y) * (y - self.circle_y))\
                <= (self.sliderRect.w * 1.5) * (self.sliderRect.w * 1.5):
            return True
        else:
            return False

    def handle(self, event) -> None:
        if event.type == self.pygame.MOUSEBUTTONDOWN and self.on_slider(*event.pos):
            self.isHolding = True
        elif event.type == self.pygame.MOUSEBUTTONUP:
            self.isHolding = False
        if self.isHolding and event.type == 1024:
            y = event.pos[1]
            if y < self.sliderRect.y:
                self.circle_y = self.sliderRect.y
            elif y > self.sliderRect.y + self.sliderRect.h:
                self.circle_y = self.sliderRect.y + self.sliderRect.h
            else:
                self.circle_y = y
            self.update_value(y)


class Button(Widget):
    def __init__(self, pygame, text: str, decription: str, color: MaterialColor, width: int, start: int, active: bool) -> None:
        self.pygame = pygame
        self.color = color
        self.text = text
        self.width = width
        self.start = start
        self.isHolding = False
        self.active = active
        self.isHover = False
        self.decription = decription

    def draw(self, screen) -> None:
        self.pygame.draw.rect(screen, self.color.c900.color if self.isHolding else (self.color.c800.color if self.active else self.color.color), self.pygame.Rect(self.width*0.18, self.start, self.width*0.64, 40))
        self.write(screen, self.text, self.width//2, self.start, size=25, color=(Colors.white if self.active or self.isHolding else Colors.gray.c900))
        try:
            if self.isHover:
                for i, line in enumerate(self.decription.split('\n')):
                    self.write(screen, line, self.width, self.start + i * 25, size=20, center=False)
        except Exception:
            pass

    def on_button(self, x, y):
        return x > self.width*0.18 and x < self.width*0.82 and y > self.start and y < self.start+40

    def handle(self, event) -> None:
        try:
            self.isHover = self.on_button(*event.pos)
        except Exception:
            pass
        if event.type == self.pygame.MOUSEBUTTONDOWN and self.on_button(*event.pos) or self.isHolding and event.type == 1024 and self.on_button(*event.pos):
            self.isHolding = True
        else:
            if self.isHolding and event.type == self.pygame.MOUSEBUTTONUP:
                self.isHolding = False
                self.active = True
                return True
            self.isHolding = False
        return False


class Row(Widget):
    def __init__(self, pygame, title: str, functions: List[function], color: MaterialColor, width: int, start: int) -> None:
        self.pygame = pygame
        self.color = color
        self.functions = functions
        self.title = title
        self.width = width
        self.start = start
        self.buttons: List[Button] = []
        self.active = len(functions)-1
        for i, function in enumerate(self.functions):
            self.buttons.append(Button(pygame, function.__name__, function.__doc__, color, width, self.start + int((i+1.5)*60), self.active == i))

    def draw(self, screen) -> None:
        self.write(screen, self.title, self.width//2, self.start, size=40)
        for button in self.buttons:
            button.draw(screen)

    def handle(self, event) -> None:
        for i, button in enumerate(self.buttons):
            if button.handle(event):
                self.active = i
                for j, button2 in enumerate(self.buttons):
                    if j != i:
                        button2.active = False


class Menu(Widget):
    def __init__(self, pygame, updateEdges: List[function], updateNotes: List[function], color: MaterialColor, width: int, buttonsColor: MaterialColor) -> None:
        self.pygame = pygame
        self.color = color
        self.updateEdges = updateEdges
        self.updateNotes = updateNotes
        self.width = width
        self.rows = [
            Row(pygame, "Update Notes", updateNotes, buttonsColor, width, 0),
            Row(pygame, "Update Edges", updateEdges, buttonsColor, width, 500),
        ]

    def draw(self, screen) -> None:
        self.pygame.draw.rect(screen, self.color.color, self.pygame.Rect(0, 0, self.width, 1000))
        self.pygame.draw.rect(screen, self.color.c700.color, self.pygame.Rect(0, 498, self.width, 4))
        for row in self.rows:
            row.draw(screen)

    def handle(self, event) -> None:
        for row in self.rows:
            row.handle(event)

    def __getitem__(self, index: int) -> int:
        return self.rows[index].active
