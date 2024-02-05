import pygame
from config import *
from item import Item
from spritesheet import Spritesheet


class Diamond(pygame.sprite.Sprite, Item):
    def __init__(self, game, x, y):
        Item.__init__(self, game, x, y)
        self._layer=DIAMOND_LAYER
        self.groups= self.game.all_sprites, self.game.diamonds
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.potion_spritesheet = Spritesheet(SPRITE_DIAMOND)
        self.image = self.potion_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y