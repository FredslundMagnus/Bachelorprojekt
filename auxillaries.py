from time import time
from typing import Iterator, List
from collector import Collector
from game import Game
from random import choice
from Utils.server import getvals, isServer, serverRun
import sys


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
                Paint.switch(game.layers.width, game.layers.height)

        keyboard.Listener(on_press=on_press).start()
        f = 0
        while States.running:
            f += 1
            if States.draw:
                Paint(game, f)
            if States.showPrint:
                collector.show(game)
                States.showPrint = False
            if States.save:
                States.save = False
            yield f


def person(game: Game) -> List[int]:
    from pynput import keyboard
    d = {keyboard.Key.right: 0, keyboard.Key.down: 1, keyboard.Key.left: 2, keyboard.Key.up: 3}
    action = None
    while action == None and States.running:
        with keyboard.Events() as events:
            event = events.get()
            if event.__class__ == keyboard.Events.Press:
                if event.key in d:
                    action = d[event.key]
    if action == None:
        return [0 for _ in range(game.batch)]
    return [action for _ in range(game.batch)]


def random(game: Game) -> List[int]:
    return [choice([0, 1, 2, 3]) for _ in range(game.batch)]


def run(Defaults, main):
    if sys.argv[0].split("\\")[-1].split("/")[-1] == "main.py":
        (serverRun if isServer else main).__call__(getvals(Defaults))
