from save import Save
from time import time
from typing import Iterator, List
from collector import Collector
from game import Game
from random import choice
from Utils.server import getvals, isServer, serverRun
import sys
from torch import Tensor, tensor


class States:
    running = True
    showPrint = False
    save = False
    draw = False
    slow = True
    switchPlot = False
    isPaused = False


def loop(game: Game, collector: Collector, save: Save = None, teleporter=None, teleporter2=None) -> Iterator[int]:
    if isServer:
        tid, f = time() + 3600 * game.hours - 300, 0
        while time() < tid:
            f += 1
            yield f

    else:
        from pynput.keyboard import Key, Listener, Events
        from paint import Paint

        current = set()
        order = [None, None, None]

        def waitForResume():
            action = None
            while action == None and States.running:
                with Events() as events:
                    event = events.get()
                    if event.__class__ == Events.Press:
                        if event.key == Key.pause:
                            action = True
                            States.isPaused = False
                        elif event.key in {Key.shift_l, Key.shift_r}:
                            action = True

        def on_press(key):
            current.add(key)
            order.append(key)
            ctrl: bool = Key.ctrl_l in current or Key.ctrl_r in current
            alt: bool = Key.alt_l in current
            speed = 300
            zoom = 15
            if [Key.esc, Key.esc, Key.esc] == order[-3:]:
                Paint.stop()
                States.running = False
            elif Key.f2 == key:
                States.switchPlot = True
            elif Key.f7 == key:
                States.save = True
            elif Key.f4 == key:
                Paint.switch(game.layers.width, game.layers.height)
            elif Key.left == key and ctrl:
                Paint.dim = (Paint.dim - 1) % game.layers.batch
            elif Key.right == key and ctrl:
                Paint.dim = (Paint.dim + 1) % game.layers.batch
            elif Key.f3 == key:
                States.slow = not States.slow
            elif Key.right == key and alt:
                Paint.move(speed, 0, game.layers.width, game.layers.height)
            elif Key.left == key and alt:
                Paint.move(-speed, 0, game.layers.width, game.layers.height)
            elif Key.down == key and alt:
                Paint.move(0, speed, game.layers.width, game.layers.height)
            elif Key.up == key and alt:
                Paint.move(0, -speed, game.layers.width, game.layers.height)
            elif Key.down == key and ctrl:
                Paint.zoom(-zoom, game.layers.width, game.layers.height)
            elif Key.up == key and ctrl:
                Paint.zoom(zoom, game.layers.width, game.layers.height)
            elif Key.pause == key:
                States.isPaused = True

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
                Paint(game, f, teleporter, teleporter2)
            if States.switchPlot:
                States.showPrint = not States.showPrint
                States.switchPlot = False
                collector.show(game)

            if States.save:
                if save != None:
                    save.save()
                States.save = False
            if States.isPaused:
                waitForResume()
            yield f


def person(batch: int) -> Tensor:
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
        return tensor([0 for _ in range(batch)])
    return tensor([action for _ in range(batch)])


def random_agent(batch: int) -> Tensor:
    return tensor([choice([0, 1, 2, 3]) for _ in range(batch)])


def run(Defaults):
    if sys.argv[0].split("\\")[-1].split("/")[-1] == "main.py":
        (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))


def player(defaults):
    env = Game(**defaults)
    for _ in loop(env, None):
        env.step(person(env.batch))


def random(defaults):
    env = Game(**defaults)
    for _ in loop(env, None):
        env.step(random_agent(env.batch))
