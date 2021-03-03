from collector import Collector
from game import Game
from load import Load
from agent import Mover
from auxillaries import loop

with Load("Agent", isLocal=True) as load:
    collector, env, mover = load.items(Collector, Game, Mover)
    for frame in loop(env, collector):
        actions = mover(env.board)
        env.step(actions)
