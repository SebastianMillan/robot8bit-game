import pygame
class Map(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('assests/images/basic_robot.png').convert()
        self.rect=self.image.get_rect()
        self.rect.center=(400,300)

