import pygame

from config import *
from button import Button
from screen import Screen


class IntroScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.intro_background = pygame.image.load("assests/images/intro_background.jpg")

    def display(self):
        intro = True
        title = self.font.render('Roque Like SCI- FI Game', True, WHITE)
        title_rect = title.get_rect(x=10, y=10)
        play_button = Button(100, 100, 100, 50, BLACK, WHITE, 'Play', 32)
        SOUND_INTRO.play(-1).set_volume(0.5)

        while intro:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.game.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                SOUND_INTRO.stop()

            self.game.screen.blit(self.intro_background, (0, 0))
            self.game.screen.blit(title, title_rect)
            self.game.screen.blit(play_button.image, play_button.rect)
            self.game.clock.tick(FPS)
            pygame.display.update()
