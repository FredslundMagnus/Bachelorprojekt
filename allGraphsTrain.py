from allGraphs import *
from helper import device
from agent import Mover, Teleporter
from collector import Collector
from save import Save
from torch import tensor, cat
from auxillaries import loop
from BayesianNN import BayesionNN
import sys
from load import Load


def graphTrain(defaults):
    layers: List[LayerType] = environments[defaults['level']][2]
    explorationN = defaults['K1']
    data = Data(layers, defaults['graphMode'])
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    collector = Collector(**defaults)
    model = BayesionNN(layers, depth=3, exploration=1, samples=5)
    use_model=False

    with Save(env, collector, mover, data, **defaults) as save:
        convert = [env.layers.types.index(layer) for layer in layers]
        player = env.layers.types.index(LayerType.Player)
        goal = env.layers.types.index(LayerType.Goal)
        old_states = [state for state in states(env.board, convert, layers)]
        dones = tensor([0 for _ in range(env.batch)])
        rewards = tensor([0 for _ in range(env.batch)])
        eatCheese, interventions = ([True] * env.batch, [None] * env.batch)
        for frame in loop(env, collector, save, teleporter=teleporter):
            data.t = frame
            new_states = [state for state in states(env.board, convert, layers)]
            loss = transform(old_states, new_states, dones, rewards, data, layers, model, use_model=use_model)
            loss = transformNot(env.board, new_states, player, goal, convert, data, layers, model, use_model=use_model)
            stateChanged = [old != new for old, new in zip(old_states, new_states)]
            shouldInterviene = [cond1 or cond2 for cond1, cond2 in zip(stateChanged, eatCheese)]
            exploration = max((explorationN-frame)/explorationN, defaults['softmax_cap'])
            if use_model:
                interventions = [(getInterventionsmodel(state, env.layers.types, layers, model, env, data.layers_not_in(state), frame) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
            else:
                interventions = [(getInterventions(env, state, data, exploration) if should else old) for state, should, old in zip(new_states, shouldInterviene, interventions)]
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
            collector.collect_loss(loss)
