from main import *
from load import Load

with Load("Agent", isLocal=True, num=0) as load:
    collector, env, mover = load.items(Collector, Game, Mover)
    for frame in loop(env, collector):
        actions = mover(env.board)
        env.step(actions)
