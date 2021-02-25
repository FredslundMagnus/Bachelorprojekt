from game import Game
from agent import Agent, Networks
from collector import Collector
from auxillaries import loop, person, random

collector = Collector()
game = Game()
meta = Agent(game, Networks.Small)


for frame in loop(game, collector):
    print(meta(game.board))
    game.step(person(game))
    print(frame)
