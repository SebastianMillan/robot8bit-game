import sys
import pygame
from player import Player

pygame.init()
pygame.display.set_caption("ROGUE LIKE")
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
bg_color = (41, 44, 53)

player = Player()

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
clock = pygame.time.Clock()

# Comenzamos el bucle del juego
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
