from allGraphs import *
from helper import device


def graphTrain(defaults, data=None):
    layers: List[LayerType] = environments[defaults['level']][2]
    explorationN = defaults['K1']
    if data == None:
        data = {}
    for layer in layers:
        data[layer] = {c: 1 for c in combinations(layer, layers)}
    data[LayerType.Goal] = {c: 1 for c in combinations(None, layers)}
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    collector = Collector(**defaults)

    with Save(env, collector, mover, data, **defaults) as save:
        convert = [env.layers.types.index(layer) for layer in layers]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        old_states = [state for state in states(env.board, convert, layers)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        eatCheese, interventions = ([True] * env.batch, [None] * env.batch)
        for frame in loop(env, collector, save, teleporter=teleporter):
            new_states = [state for state in states(env.board, convert, layers)]
            transform(old_states, new_states, dones, rewards, data, layers)
            transformNot(env.board, new_states, player, goal, convert, data, layers)
            stateChanged = [old != new for old, new in zip(old_states, new_states)]
            shouldInterviene = [cond1 or cond2 for cond1, cond2 in zip(stateChanged, eatCheese)]
            exploration = max((explorationN-frame)/explorationN, defaults['softmax_cap'])
            interventions = [(getInterventions(env, state, data, layers, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
            modification = env.board[tensor(interventions)].unsqueeze(1)
            teleporter.interventions = tensor([m.flatten().argmax().item() for m in list(modification)], device=device)
            modified_board = cat((env.board, modification), dim=1)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, _, _ = teleporter.modify(observations, rewards, dones, info)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            playerPositions = [(t := env.layers.dict[LayerType.Player].positions[i][0])[1] * env.layers.width + t[0] for i in range(env.batch)]
            eatCheese = [intervention == player_pos for intervention, player_pos in zip(teleporter.interventions, playerPositions)]
            old_states = new_states
            collector.collect([rewards, modified_rewards], [dones, modified_dones])
