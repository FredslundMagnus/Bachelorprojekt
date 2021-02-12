from game import Game
from agent import Meta

game = Game()
meta = Meta()

print(meta(game.board))
meta.add_category()
print(meta(game.board))
