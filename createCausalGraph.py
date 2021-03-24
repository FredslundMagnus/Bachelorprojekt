from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges

with Load("causal2_9x9", num=2) as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.extradim = 0  # fix
    teleporter.exploration.explore = teleporter.exploration.greedy
    flippables = [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]
    convert = [env.layers.types.index(layer) for layer in flippables]
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        results = torch.empty(*(shape := env.board.shape))
        for layer, x, y in ranges((len(flippables), *shape[2:])):
            board = env.board
            pixel = board[:, convert[layer], x, y]
            board[:, convert[layer], x, y][pixel == 0], board[:, convert[layer], x, y][pixel == 1], board[:, convert[layer], x, y][pixel == 2] = 2, 0, 1
            results[:, convert[layer], x, y] = teleporter.net.network(board).max(dim=1)[0]
        flippers = [int(v) for v in list(results.max(dim=3)[0].max(dim=2)[0].argmax(dim=1))]
        print(flippers)
        print(list(results.max(dim=3)[0].max(dim=2)[0]))
        # for i in flippers:
        #     counter[env.layers.types[i]] += 1

        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        actions = mover(modified_board)
        observations, rewards, dones, info = env.step(actions)
        movers = [torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])]
        print(movers)
        quit()
        # for i in movers:
        #     counter2[env.layers.types[i]] += 1

        # counter2 = {layer: 0 for layer in env.layers.types}
        # for å in range(100):
        #     for i in range(len(env.layers.types)):
        #         counter2[env.layers.types[i]] += int(torch.sum(modified_board[å, i] * modified_board[å, -1]).item())

        for batch in range(env.layers.batch):
            env.layers.restart(batch)
