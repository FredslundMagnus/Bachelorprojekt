
from torch import device as devicer, cuda
import matplotlib

device = devicer('cuda' if cuda.is_available() else 'cpu')


def move_figure(f, pos):
    x, y = pos
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)


class function:
    __name__: str


def restart(env):
    li = [0] * env.layers.batch
    for batch in range(env.layers.batch):
        env.layers.restart(batch)
    for layer in env.layers.layers:
        layer.update(env.layers.board, li, env.layers.all_items)
