from game import Game
from agent import Meta
from collector import Collector

collector = Collector()
game = Game()
meta = Meta()

print(meta(game.board))
meta.add_category()
print(meta(game.board))


for frame in game.loop(collector):
    print(frame, meta(game.board))
