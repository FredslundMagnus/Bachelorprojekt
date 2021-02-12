from time import time


class States:
    running = True
    showPrint = False
    save = False
    draw = False


def loop(hours, game):
    if False:  # is server
        tid, f = time() + 3600 * hours - 300, 0
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
        tid, f = time() + 3600 * hours - 300, 0
        while States.running:
            f += 1
            if States.draw:
                Paint(game)
            yield f
