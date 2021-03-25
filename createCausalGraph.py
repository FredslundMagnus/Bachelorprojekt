from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges, array
from helper import restart


with Load("causal2_9x9", num=2) as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.extradim = 0  # fix
    teleporter.exploration.explore = teleporter.exploration.greedy
    flippables = [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]
    convert = [env.layers.types.index(layer) for layer in flippables]
    d = {}
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        movers = array([torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])])
        mask = array([layer in convert for layer in movers])
        results = torch.zeros((env.board.shape[0], *(shape := (len(flippables), *env.board.shape[2:]))))
        for layer, x, y in ranges(shape):
            board = env.board
            pixel = board[:, convert[layer], x, y]
            board[:, convert[layer], x, y][pixel == 0], board[:, convert[layer], x, y][pixel == 1], board[:, convert[layer], x, y][pixel == 2] = 2, 0, 1
            results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
        flip = list(results[mask].max(dim=3)[0].max(dim=2)[0].argsort(dim=1, descending=True))
        paths = [[] for _ in range(len(flip))]
        for i in range(len(flippables)):
            flippers = [convert[v[i]] for v in flip]
            for i, f in enumerate(flippers):
                paths[i].append(f)
            alive = [v1 != v2 for v1, v2 in zip(flippers, list(movers[mask]))]
            flip = [v for v, a in zip(flip, alive) if a]
            for p in [v for v, a in zip(paths, alive) if not a]:
                if tuple(p) in d:
                    d[tuple(p)] += 1
                else:
                    d[tuple(p)] = 1
            paths = [v for v, a in zip(paths, alive) if a]
            mask[mask] = alive
        # for k in list(sorted(d, key=d.get, reverse=True))[:10]:
        #     print(k, d[k], end=" : ")
        # print("")
        restart(env)
        print(frame, end=",")
        if frame == 100:
            print("")
            break
    counter_first = {k: 0 for k in convert}
    for path in d:
        counter_first[path[0]] += d[path]

    counter_total = {k: 0 for k in convert}
    for path in d:
        for k in counter_total:
            if k in path:
                counter_total[k] += d[path]

    for layer, k in zip(flippables, convert):
        print(f"{layer.name}: {100*counter_first[k]//counter_total[k]}%")
