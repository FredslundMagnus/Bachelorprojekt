# Causal Graphs in Reinforcement Learning

Project of creating causal graphs in reinforcement learning

# Requirements

```bash
python -m pip install torch torchvision pygame matplotlib pynput
```

# Import classes

```python
from game import *
from agent import *
from collector import *
from auxillaries import *
from helper import *
from replaybuffer import *
```
# Setup simple loop

```python
def simple(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, **defaults)

    with Save(env, collector, mover, **defaults) as save:
        for frame in loop(env, collector, save):
            actions = mover(env.board)
            observations, rewards, dones, info = env.step(actions)
            mover.learn(observations, actions, rewards, dones)
            collector.collect([rewards], [dones])
```

# Setup teleport loop

```python
def teleport(defaults):
    collector = Collector(**defaults)
    env = Game(**defaults)
    mover = Mover(env, _extra_dim=1, **defaults)
    teleporter = Teleporter(env, **defaults)
    buffer = ReplayBuffer(**defaults)

    with Save(env, collector, mover, teleporter, **defaults) as save:
        intervention_idx, modified_board = teleporter.pre_process(env)
        for frame in loop(env, collector, save, teleporter):
            modified_board = teleporter.interveen(env.board, intervention_idx, modified_board)
            actions = mover(modified_board)
            observations, rewards, dones, info = env.step(actions)
            modified_board, modified_rewards, modified_dones, teleport_rewards, intervention_idx = teleporter.modify(observations, rewards, dones, info)
            buffer.teleporter_save_data(teleporter.boards, observations, teleporter.interventions, teleport_rewards, dones, intervention_idx, rewards)
            mover.learn(modified_board, actions, modified_rewards, modified_dones)
            board_before, board_after, intervention, tele_rewards, tele_dones, normal_rewards = buffer.sample_data()
            teleporter.learn(board_after, intervention, tele_rewards, tele_dones, board_before)
            collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
```

# Setup default variables

```python
class Defaults:
    name: str = "Agent"
    main: function = teleport
    level: Levels = Levels.Causal3
    hours: float = 12
    batch: int = 100
    width: int = 9
    height: int = 9

    network1: Networks = Networks.Teleporter
    K1: float = 5000000
    learner1: Learners = Learners.Qlearn
    exploration1: Explorations = Explorations.softmaxer
    gamma1: float = 0.98

    network2: Networks = Networks.Mini
    K2: float = 1000000
    learner2: Learners = Learners.Qlearn
    exploration2: Explorations = Explorations.epsilonGreedy
    gamma2: float = 0.95

    layer_Blocks: bool = True
    layer_Goal: bool = True
    layer_Gold: bool = True
    layer_Keys: bool = True
    layer_Door: bool = True
    layer_Holder: bool = True
    layer_Putter: bool = True
    layer_Rock: bool = True
    layer_Dirt: bool = True
    layer_Diamond1: bool = True
    layer_Diamond2: bool = True
    layer_Diamond3: bool = True
    layer_Diamond4: bool = True
    layer_Reddoors: bool = True
    layer_Redkeys: bool = True
    layer_Bluedoors: bool = True
    layer_Bluekeys: bool = True

    epsilon_cap: float = 0.2
    softmax_cap: float = 0.02
    update: int = 10000
    reset_chance: float = 0.001
    modified_done_chance: float = 0.05
    miss_intervention_cost: float = -0.15
    intervention_cost: float = -0.05
    replay_size: int = 100000
    sample_size: int = 50
```

# Run the selected loop

```python
run(Defaults)
```