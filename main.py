from game import Game
from agent import Meta
from auxillaries import loop

game = Game()
meta = Meta()

print(meta(game.board))
meta.add_category()
print(meta(game.board))
print(meta(game.board))
print(meta(game.board))
game.change()
print(meta(game.board))


for frame in game.loop:
    print(frame, meta(game.board))
