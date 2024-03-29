import pygame.display
from config import *


class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(GENERAL_FONT, UI_FONT_SIZE)
        self.health_bar_rect = pygame.Rect(10, WIN_HEIGHT-40, HEALTH_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def count_diamons(self, diamond_count):
        text=self.font.render(f"Diamantes: {diamond_count}", True, WHITE)
        self.display_surface.blit(text,(WIN_WIDTH-120,WIN_HEIGHT-40))

    def count_bombs(self, bombs_count):
        text = self.font.render(f"Bombas: {bombs_count}", True, WHITE)
        self.display_surface.blit(text, (WIN_WIDTH-230, WIN_HEIGHT-40))

    def display(self, player):
        self.show_bar(player.actual_health, player.max_health, self.health_bar_rect, HEALTH_COLOR)



