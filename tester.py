from collector import Collector
from game import Game
from load import Load
from agent import Mover
from auxillaries import loop


with Load("Agent", Collector, Game, Mover) as load:
    collector, env, mover = load
    for frame in loop(env, collector):
        actions = mover(env.board)
        env.step(actions)
