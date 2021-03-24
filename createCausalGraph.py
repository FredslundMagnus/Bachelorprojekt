from layer import LayerType
import torch
from main import *
from load import Load
from numpy import ndindex as ranges

with Load("causal2_9x9", num=2) as load:
    collector, env, mover, teleporter = load.items(Collector, Game, Mover, Teleporter)
    teleporter.extradim = 0
    teleporter.exploration.explore = teleporter.exploration.greedy
    counter = {layer: 0 for layer in env.layers.types}
    counter2 = {layer: 0 for layer in env.layers.types}
    counter3 = {(layer1, layer2): 0 for layer1 in env.layers.types for layer2 in env.layers.types}
    rounds = 0
    for frame in loop(env, collector, teleporter=teleporter):
        intervention_idx, modified_board = teleporter.pre_process(env)
        results = torch.empty(*(shape := env.board.shape))
        for layer, x, y in ranges(shape[1:]):
            board = env.board
            pixel = board[:, layer, x, y]
            board[:, layer, x, y][pixel == 0], board[:, layer, x, y][pixel == 1], board[:, layer, x, y][pixel == 2] = 2, 0, 1
            results[:, layer, x, y] = teleporter.net.network(board).max(dim=1)[0]
        flippers = [int(v) for v in list(results.max(dim=3)[0].max(dim=2)[0].argmax(dim=1))]
        for i in flippers:
            counter[env.layers.types[i]] += 1
        # print(counter)
        modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
        actions = mover(modified_board)
        observations, rewards, dones, info = env.step(actions)
        movers = [torch.sum(torch.sum(modified_board[batch, :-1] * modified_board[batch, -1], dim=1), dim=1).argmax().item() for batch in range(modified_board.shape[0])]
        for i in movers:
            counter2[env.layers.types[i]] += 1
        # print(counter2)
        counter2 = {layer: 0 for layer in env.layers.types}
        for å in range(100):
            for i in range(len(env.layers.types)):
                counter2[env.layers.types[i]] += int(torch.sum(modified_board[å, i] * modified_board[å, -1]).item())
        for flipper, mover_ in zip(flippers, movers):
            counter3[(env.layers.types[flipper], env.layers.types[mover_])] += 1

       # print(env.board[0])
        for batch in range(env.layers.batch):
            env.layers.restart(batch)
            # print(env.board[0])
        rounds += 1
        print(rounds, end=",")
        if rounds == 10:
            break

    for k1, k2 in [v for v in sorted(counter3, key=counter3.get, reverse=True) if counter3[v] and v[0].name != "Player" and v[0].name != "Goal"]:
        print(f"{k2.name} -> {k1.name}:", counter3[(k1, k2)])
    for layer in [LayerType.Diamond1, LayerType.Diamond2, LayerType.Diamond3, LayerType.Diamond4]:
        print(layer, counter[layer]/(counter[layer]+counter2[layer]))
