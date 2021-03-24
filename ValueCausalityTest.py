from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges

with Load("causal2_9x9", num=2) as load:
    all_combinations = {}
    for i in range(4):
        for k in range(4):
            for p in range(4):
                for o in range(4):
                    all_combinations[(i,k,p,o)] = 0
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.extradim = 0
    teleporter.exploration.explore = teleporter.exploration.greedy
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        results = torch.zeros(*(shape := env.board.shape))
        for layer, x, y in ranges(shape[1:]):
            board = env.board
            pixel = board[:, layer, x, y]
            board[:, layer, x, y][pixel == 0], board[:, layer, x, y][pixel == 1], board[:, layer, x, y][pixel == 2] = 2, 0, 1
            results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
        board_size = (results.shape[2] * results.shape[3])
        results = results[:, 3:7]
        results = results.flatten(start_dim=1)
        all_orders = []
        for i in range(results.shape[0]):
            order = []
            for _ in range(4):
                maxers = torch.argmax(results[i])
                order.append((maxers//board_size).item())
                results[i][maxers] = -10**6
            all_combinations[tuple(order)] += 1
        
        li = [0] * env.layers.batch
        for batch in range(env.layers.batch):
            env.layers.restart(batch)
        for layer in env.layers.layers:
            layer.update(env.layers.board, li, env.layers.all_items)
        if frame == 100:
            break
    print(dict(sorted(all_combinations.items(), key=lambda item: item[1])))