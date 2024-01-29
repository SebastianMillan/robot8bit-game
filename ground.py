import pygame
from config import *
from spritesheet import Spritesheet


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game=game
        self._layer=GROUND_LAYER

        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.ground_spritesheet = Spritesheet('assests/images/floor_sprite.png')
        self.image = self.ground_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
