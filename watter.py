import pygame
from config import *
class Watter(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = WATTER_LAYER
        self.groups= self.game.all_sprites, self.game.watter
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image =  pygame.image.load('assests/images/watter_sprite.png').convert()

        self.rect = self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y