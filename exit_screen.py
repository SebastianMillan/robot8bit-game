import pygame

from button import Button
from config import WIN_WIDTH, WIN_HEIGHT, WHITE, BLACK, FPS
from screen import Screen


class ExitScreen(Screen):
    def __init__(self, game):
        super().__init__(game)

    def display(self):
        text = self.font.render('GAME OVER', True, WHITE)
        text_rect=text.get_rect(center=(WIN_WIDTH/2,WIN_HEIGHT/2))
        restart_button=Button(10, WIN_HEIGHT -60, 120,50, WHITE, BLACK,'Restart',32)
        exit_button=Button(10, WIN_HEIGHT -60, 120,50, WHITE, BLACK,'Restart',32)
        while self.game.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.playing=False
                    self.game.running=False

            mouse_pos=pygame.mouse.get_pos()
            mouse_pressed=pygame.mouse.get_pressed()
            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.game.new()
                self.game.main()

            self.game.screen.fill((255,0,0))
            self.game.screen.blit(text, text_rect)
            self.game.screen.blit(restart_button.image, restart_button.rect)
            self.game.clock.tick(FPS)
            pygame.display.update()
