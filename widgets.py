from colors import MaterialColor


class Widget:
    pass


class Slider(Widget):
    def __init__(self, pygame, x, color: MaterialColor) -> None:
        self.isHolding = False
        self.pygame = pygame
        self.circle_y = 900
        self.color = color
        self.value = 0
        self.sliderRect = pygame.Rect(x, 100, 10, 800)

    def draw(self, screen):
        self.pygame.draw.circle(screen, self.color.c200.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.sliderRect.y), self.sliderRect.w / 2)
        self.pygame.draw.rect(screen, self.color.c200.color, self.pygame.Rect(self.sliderRect.x, self.sliderRect.y, self.sliderRect.w, self.circle_y-self.sliderRect.y))
        self.pygame.draw.circle(screen, self.color.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.sliderRect.y + self.sliderRect.h), self.sliderRect.w/2)
        self.pygame.draw.rect(screen, self.color.color, self.pygame.Rect(self.sliderRect.x, self.circle_y, self.sliderRect.w, self.sliderRect.h - self.circle_y+self.sliderRect.y))
        self.pygame.draw.circle(screen, self.color.color, (self.sliderRect.w / 2 + self.sliderRect.x, self.circle_y), self.sliderRect.w * 1.5)

    def update_value(self, y):
        if y < self.sliderRect.y:
            self.value = 100
        elif y > self.sliderRect.y + self.sliderRect.h:
            self.value = 0
        else:
            self.value = 100 - (y - self.sliderRect.y) / float(self.sliderRect.h) * 100

    def on_slider(self, x, y):
        if ((x - self.sliderRect.x + self.sliderRect.w / 2) * (x - self.sliderRect.x + self.sliderRect.w / 2) + (y - self.circle_y) * (y - self.circle_y))\
                <= (self.sliderRect.w * 1.5) * (self.sliderRect.w * 1.5):
            return True
        else:
            return False

    def handle(self, event):
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
        return self.value
