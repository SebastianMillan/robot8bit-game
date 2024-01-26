import sys
import pygame
from game import Game
from intro_screen import IntroScreen

g = Game()
i=IntroScreen(g)
i.display()
g.new()
while g.running:
    g.main()
pygame.quit()
sys.exit()