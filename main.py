from game import Game
from agent import Meta
from collector import Collector
from auxillaries import loop, person

collector = Collector()
game = Game()
meta = Meta()

print(meta(game.board))
meta.add_category()
print(meta(game.board))


for frame in loop(game, collector):
    # print(meta(game.board))
    game.step(person(game))
    print(game.layers.board[0])
