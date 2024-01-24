import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init(self, pos_x, pos_y):
        super().__init__()
        self.position=[pos_x, pos_y]
        self.image = pygame.image.load('assests/images/basic_robot.png').convert()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    