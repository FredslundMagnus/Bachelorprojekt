class Widget:
    pass


class Slider(Widget):
    def __init__(self, pygame) -> None:
        self.isHolding = False
        self.pygame = pygame
        self.circle_y = 100
        self.volume = 0
        self.sliderRect = pygame.Rect(1400, self.circle_y, 10, 800)

    def draw(self, screen):
        self.pygame.draw.rect(screen, (255, 255, 255), self.sliderRect)
        self.pygame.draw.circle(screen, (255, 240, 255), (self.sliderRect.w / 2 + self.sliderRect.x, self.circle_y), self.sliderRect.w * 1.5)

    def get_volume(self):
        return self.volume

    def set_volume(self, num):
        self.volume = num

    def update_volume(self, y):
        if y < self.sliderRect.y:
            self.volume = 0
        elif y > self.sliderRect.y + self.sliderRect.h:
            self.volume = 100
        else:
            self.volume = int((y - self.sliderRect.y) / float(self.sliderRect.h) * 100)

    def on_slider(self, x, y):
        if self.on_slider_hold(x, y) or self.sliderRect.x <= x <= self.sliderRect.x + self.sliderRect.w and self.sliderRect.y <= y <= self.sliderRect.y + self.sliderRect.h:
            return True
        else:
            return False

    def on_slider_hold(self, x, y):
        if ((x - self.sliderRect.x + self.sliderRect.w / 2) * (x - self.sliderRect.x + self.sliderRect.w / 2) + (y - self.circle_y) * (y - self.circle_y))\
                <= (self.sliderRect.w * 1.5) * (self.sliderRect.w * 1.5):
            return True
        else:
            return False

    def handle(self, event):
        if event.type == self.pygame.MOUSEBUTTONDOWN and self.on_slider_hold(*event.pos):
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
            self.update_volume(y)
            print(self.volume)
