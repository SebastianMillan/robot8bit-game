import pygame

from armour import Armour
from block import Block
from config import *
from ground import Ground
from spritesheet import Spritesheet


class Bomb(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BOMB_LAYER
        self.groups = self.game.all_sprites, self.game.bombs
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.bomb_spritesheet = Spritesheet('assests/images/bomb_sprite.png')
        self.image = self.bomb_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def explote(self):
        offsets = [(-1, -1), (-1, 0), (-1, 1),
                   (0, -1), (0, 1),
                   (1, -1), (1, 0), (1, 1)]
        for offset in offsets:
            check_x = self.rect.x // TILESIZE + offset[0]
            check_y = self.rect.y // TILESIZE + offset[1]

            block_to_destroy = self.get_block_at(check_x, check_y)
            bomb_explote_bomb = self.get_bomb_at(check_x, check_y)
            armour_to_destroy = self.get_armour_at(check_x, check_y)
            if isinstance(block_to_destroy, Block):
                block_to_destroy.kill()
                new_ground = Ground(self.game, block_to_destroy.rect.x // TILESIZE, block_to_destroy.rect.y // TILESIZE)
            elif isinstance(bomb_explote_bomb, Bomb):
                bomb_explote_bomb.kill()
                bomb_explote_bomb.explote()
            elif isinstance(armour_to_destroy, Armour):
                armour_to_destroy.kill()
        SOUND_THROW_BOMB.play()
        self.kill()

    def get_block_at(self, x, y):
        for block in self.game.blocks:
            if block.rect.x == x * TILESIZE and block.rect.y == y * TILESIZE:
                return block
        return None

    def get_bomb_at(self, x, y):
        for bomb in self.game.bombs:
            if bomb.rect.x == x * TILESIZE and bomb.rect.y == y * TILESIZE:
                return bomb
        return None

    def get_armour_at(self, x, y):
        for armour in self.game.armour:
            if armour.rect.x == x * TILESIZE and armour.rect.y == y * TILESIZE:
                return armour
        return None
