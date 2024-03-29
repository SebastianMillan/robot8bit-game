import pygame

from config import WHITE
from screen import Screen
from button import Button
from config import *


class GameOverScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def display(self):
        text = self.font.render('GAME OVER', True, WHITE)
        text_rect=text.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/2))
        restart_button=Button(10, WIN_HEIGHT -60, 120,50, WHITE, BLACK,'Restart',32)
        SOUND_MUSIC.stop()
        SOUND_GAME_OVER.play(-1).set_volume(0.5)
        while self.game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.playing=False
                    self.game.running=False

            mouse_pos=pygame.mouse.get_pos()
            mouse_pressed=pygame.mouse.get_pressed()
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                SOUND_MUSIC.play(-1).set_volume(0.5)
                SOUND_GAME_OVER.stop()
                self.game.new()
                self.game.main()

            self.game.screen.fill((255,0,0))
            self.game.screen.blit(text, text_rect)
            self.game.screen.blit(restart_button.image, restart_button.rect)
            self.game.clock.tick(FPS)
            pygame.display.update()




