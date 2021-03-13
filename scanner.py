import torch
from main import *
from load import Load
from numpy import ndindex as ranges

with Load("gold_small") as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    intervention_idx, modified_board = teleporter.pre_process(env)
    counter = {layer: 0 for layer in env.layers.types}
    for frame in loop(env, collector, teleporter=teleporter):

        results = torch.empty(*(shape := env.board.shape))
        for layer, x, y in ranges(shape[1:]):
            board = env.board
            pixel = board[:, layer, x, y]
            board[:, layer, x, y][pixel == 0], board[:, layer, x, y][pixel == 1], board[:, layer, x, y][pixel == 2] = 2, 0, 1
            results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
        for i in list(results.max(dim=3)[0].max(dim=2)[0].argmax(dim=1)):
            counter[env.layers.types[i]] += 1
        print(counter)
        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        actions = mover(modified_board)
        observations, rewards, dones, info = env.step(actions)
        modified_board, _, _, _, intervention_idx = teleporter.modify(teleporter.interventions, observations, rewards, dones, info)
