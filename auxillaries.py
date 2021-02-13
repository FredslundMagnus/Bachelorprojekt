from time import time
from typing import Iterator
from collector import Collector
from game import Game


class States:
    running = True
    showPrint = False
    save = False
    draw = False


def loop(game: Game, collector: Collector) -> Iterator[int]:
    if False:  # is server
        tid, f = time() + 3600 * game.hours - 300, 0
        while time() < tid:
            f += 1
            yield f

    else:
        from pynput import keyboard
        from paint import Paint

        def on_press(key):
            if keyboard.Key.esc == key:
                Paint.stop()
                States.running = False
            if keyboard.Key.f2 == key:
                States.showPrint = True
            if keyboard.Key.f3 == key:
                States.save = True
            if keyboard.Key.f4 == key:
                Paint.switch()

        keyboard.Listener(on_press=on_press).start()
        f = 0
        while States.running:
            f += 1
            if States.draw:
                Paint(game)
            if States.showPrint:
                collector.show(game)
                States.showPrint = False
            if States.save:
                States.save = False
            yield f
