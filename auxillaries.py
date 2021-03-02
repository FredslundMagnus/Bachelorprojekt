from save import Save
from time import time
from typing import Iterator, List
from collector import Collector
from game import Game
from random import choice
from Utils.server import getvals, isServer, serverRun
import sys
from torch import tensor


class States:
    running = True
    showPrint = False
    save = False
    draw = False
    slow = False
    switchPlot = False


def loop(game: Game, collector: Collector, save: Save) -> Iterator[int]:
    if isServer:
        tid, f = time() + 3600 * game.hours - 300, 0
        while time() < tid:
            f += 1
            yield f

    else:
        from pynput.keyboard import Key, Listener
        from paint import Paint

        current = set()

        def on_press(key):
            current.add(key)
            ctrl: bool = Key.ctrl_l in current or Key.ctrl_r in current
            if Key.esc == key:
                Paint.stop()
                States.running = False
            elif Key.f2 == key:
                States.switchPlot = True
            elif Key.f7 == key:
                States.save = True
            elif Key.f4 == key:
                Paint.switch(game.layers.width, game.layers.height)
            elif Key.left == key and ctrl:
                Paint.dim -= 1
            elif Key.right == key and ctrl:
                Paint.dim += 1
            elif Key.f3 == key:
                States.slow = not States.slow

        def on_release(key):
            try:
                current.remove(key)
            except KeyError:
                pass

        Listener(on_press=on_press, on_release=on_release).start()
        f = 0
        while States.running:
            f += 1
            if States.draw:
                Paint(game, f)
            if States.switchPlot:
                States.showPrint = not States.showPrint
                States.switchPlot = False
                collector.show(game)

            if States.save:
                save.save()
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
        return tensor([0 for _ in range(game.batch)])
    return tensor([action for _ in range(game.batch)])


def random(game: Game) -> List[int]:
    return tensor([choice([0, 1, 2, 3]) for _ in range(game.batch)])


def run(Defaults, main):
    if sys.argv[0].split("\\")[-1].split("/")[-1] == "main.py":
        (serverRun if isServer else main).__call__(getvals(Defaults))
