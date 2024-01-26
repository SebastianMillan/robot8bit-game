import pygame
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.max_health = PLAYER_HEALTH
        self.actual_health= self.max_health
        self.armoured = False

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.death()
        self.x_change = 0
        self.y_change = 0


    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED

    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            self.actual_health-=DAMAGE_COLLIDE
            if direction == "x":
                if hits:
                    if self.x_change > 0:
                        self.rect.x = hits[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hits[0].rect.right
            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hits[0].rect.top - self.rect.height
                    if self.y_change < 0:
                        self.rect.y = hits[0].rect.bottom

    def death(self):
        if self.actual_health<=0:
            self.game.game_over()

    def change_armoured(self):
        if (self.armoured):
            self.image = pygame.image.load('assests/images/basic_robot_sprite.png').convert()
        else:
            self.image = pygame.image.load('assests/images/armoured_robot_sprite.png').convert()
