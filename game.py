import pygame

from block import Block
from button import Button
from config import *
from ground import Ground
from player import *


class Game:
    def __init__(self):
        pygame.init()

        self.screen =  pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font=pygame.font.Font('assests/fonts/arial_narrow_7.ttf',32)
        self.intro_background=pygame.image.load("assests/images/intro_background.jpg")

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.createTileMap()

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        # Ejecutará el método update de todos los sprite contenidos aquí
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Dibujará cada uno de los sprites contenidos
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # main loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        intro=True
        title=self.font.render('Roque Like SCI- FI Game', True, WHITE)
        title_rect=title.get_rect(x=10, y=10)
        play_button=Button(100, 100, 100, 50, BLACK, WHITE, 'Play',32)

        while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    intro=False
                    self.running=False

            mouse_pos=pygame.mouse.get_pos()
            mouse_pressed=pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro=False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
