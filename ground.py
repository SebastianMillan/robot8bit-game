import pygame
from config import *
from item import Item
from spritesheet import Spritesheet


class Ground(pygame.sprite.Sprite, Item):
    def __init__(self, game, x, y):
        Item.__init__(self, game, x, y)
        self._layer=GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.ground_spritesheet = Spritesheet(SPRITE_FLOOR)
        self.image = self.ground_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
