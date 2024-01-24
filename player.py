import pygame
from config import *
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game=game
        self.layer=PLAYER_LAYER
        self.image=pygame.image.load('assests/images/basic_robot.png').convert()
        self.rect=self.image.get_rect()
        self.rect.center=(400,300)
        self.speed=10
        self.health=10
        self.armoured=False

    def move_right(self):
        self.rect[0]+=self.speed

    def move_left(self):
        self.rect[0]-=self.speed

    def move_up(self):
        self.rect[1]-=self.speed

    def move_down(self):
        self.rect[1]+=self.speed

    def damage_collision(self, obstacle, damage):
        if(self.rect[0]==obstacle.position[0]):
            self.health-=damage

    def change_armoured(self):
        if(self.armoured):
            self.image = pygame.image.load('assests/images/basic_robot_sprite.png').convert()
        else:
            self.image=pygame.image.load('assests/images/armoured_robot_sprite.png').convert()


