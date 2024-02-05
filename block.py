import pygame
from config import *
from item import Item
from spritesheet import Spritesheet


class Block(pygame.sprite.Sprite, Item):
    def __init__(self, game, x, y):
        Item.__init__(self, game, x, y)
        self._layer=BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.wall_spritesheet = Spritesheet(SPRITE_BLOCK)
        self.image = self.wall_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x=self.x
        self.rect.y=self.y
