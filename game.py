import pygame

from block import Block
from ground import Ground
from player import *
from spritesheet import Spritesheet
from ui import UI
from game_over_screen import GameOverScreen
from watter import Watter


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.character_spritesheet = Spritesheet('assests/images/watter_sprite.png')
        self.terrain_spritesheet = Spritesheet('assests/images/wall_sprite.png')
        self.watter_spritesheet= Spritesheet('assests/images/wall_sprite.png')
        self.player=None

    def createTileMap(self):
        for i, row in enumerate(first_tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player=Player(self, j, i)
                if column == "W":
                    Watter(self,j,i)

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.watter = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.createTileMap()
        self.ui = UI()

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
        self.ui.display(self.player)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # main loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        game_over_screen=GameOverScreen(self)
        game_over_screen.display()




