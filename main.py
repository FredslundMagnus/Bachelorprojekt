from game import Game
from agent import Meta
from collector import Collector
from auxillaries import loop, person, random

collector = Collector()
game = Game()
meta = Meta(len(game.layers))


for frame in loop(game, collector):
    game.step(person(game))
    print(frame)
