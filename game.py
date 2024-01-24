import pygame
from config import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock=pygame.time.Clock()
        self.running=True

    def new(self):
        self.playing=True

        self.all_sprites=pygame.sprite.LayeredUpdates()
        self.block=pygame.sprite.LayeredUpdates()
        self.player=Player()