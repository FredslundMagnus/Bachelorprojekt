from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges, array

with Load("causal2_9x9", num=2) as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.extradim = 0  # fix
    teleporter.exploration.explore = teleporter.exploration.greedy
    flippables = [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]
    convert = [env.layers.types.index(layer) for layer in flippables]
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        movers = array([torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])])
        mask = array([layer in convert for layer in movers])
        while any(mask):
            results = torch.zeros((env.board.shape[0], *(shape := (len(flippables), *env.board.shape[2:]))))
            for layer, x, y in ranges(shape):
                board = env.board
                pixel = board[:, layer, x, y]
                board[:, layer, x, y][pixel == 0], board[:, layer, x, y][pixel == 1], board[:, layer, x, y][pixel == 2] = 2, 0, 1
                results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
            flippers = array([convert[v] for v in list(results[mask].max(dim=3)[0].max(dim=2)[0].argmax(dim=1))])
            print(flippers)
            print(movers[mask])
            mask[mask] = flippers != movers[mask]

        li = [0] * env.layers.batch
        for batch in range(env.layers.batch):
            env.layers.restart(batch)
        for layer in env.layers.layers:
            layer.update(env.layers.board, li, env.layers.all_items)
