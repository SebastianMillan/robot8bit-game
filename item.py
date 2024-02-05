from config import TILESIZE


class Item(object):
    def __init__(self,game, x, y):
        self.game = game
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE


