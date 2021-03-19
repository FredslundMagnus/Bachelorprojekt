import torch
from main import *
from load import Load
from numpy import ndindex as ranges

with Load("causal1_9x9", num=2) as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.exploration.explore = teleporter.exploration.greedy
    counter = {layer: 0 for layer in env.layers.types}
    counter2 = {layer: 0 for layer in env.layers.types}
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        results = torch.empty(*(shape := env.board.shape))
        for layer, x, y in ranges(shape[1:]):
            board = env.board
            pixel = board[:, layer, x, y]
            board[:, layer, x, y][pixel == 0], board[:, layer, x, y][pixel == 1], board[:, layer, x, y][pixel == 2] = 2, 0, 1
            results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
        for i in list(results.max(dim=3)[0].max(dim=2)[0].argmax(dim=1)):
            counter[env.layers.types[i]] += 1

        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        actions = mover(modified_board)
        observations, rewards, dones, info = env.step(actions)
        
        for i in range(len(env.layers.types)):
            counter2[env.layers.types[i]] += torch.sum(modified_board[:, i] * modified_board[:, -1]).item()
        print(counter)
        print(counter2)
        #print(env.board[0])
        for batch in range(env.layers.batch):
            env.layers.restart(batch)
        #print(env.board[0])