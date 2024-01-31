import sys
import pygame

from config import SOUND_MUSIC
from game import Game
from intro_screen import IntroScreen

g = Game()
i=IntroScreen(g)
i.display()
SOUND_MUSIC.play(-1).set_volume(0.5)
g.new()
while g.running:
    g.main()
pygame.quit()
sys.exit()