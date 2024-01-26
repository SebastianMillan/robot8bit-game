import pygame


class Screen(object):
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.clock = game.clock
        self.font = pygame.font.Font('assests/fonts/arial_narrow_7.ttf', 32)
