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
        self.widht = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0

        self.image = pygame.image.load('assests/images/basic_robot_sprite.png').convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.health = 10
        self.armoured = False

    def update(self):
        self.movement()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            self.rect.y += PLAYER_SPEED

    def damage_collision(self, obstacle, damage):
        if (self.rect[0] == obstacle.position[0]):
            self.health -= damage

    def change_armoured(self):
        if (self.armoured):
            self.image = pygame.image.load('assests/images/basic_robot_sprite.png').convert()
        else:
            self.image = pygame.image.load('assests/images/armoured_robot_sprite.png').convert()
