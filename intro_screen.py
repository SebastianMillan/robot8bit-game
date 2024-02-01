import pygame

from config import *
from button import Button
from screen import Screen


class IntroScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def display(self):
        intro = True
        title = self.font.render('Roque Like SCI- FI Game', True, WHITE)
        title_rect = title.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/2))
        description = self.font.render(f'Escape or get the {NUM_DIAMONDS} diamonds!', True, WHITE)
        description_rect=description.get_rect(center=(WIN_WIDTH/2,(WIN_HEIGHT/2)+240))
        play_button = Button((WIN_WIDTH/2)-70, (WIN_HEIGHT/2)+80, 100, 50, BLACK, WHITE, 'Play', 32)
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

            self.game.screen.fill((0,0,255))
            self.game.screen.blit(title, title_rect)
            self.game.screen.blit(description, description_rect)

            self.game.screen.blit(play_button.image, play_button.rect)
            self.game.clock.tick(FPS)
            pygame.display.update()
