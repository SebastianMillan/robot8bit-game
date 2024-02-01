import pygame.sprite

from armour import Armour
from block import Block
from bomb import Bomb
from diamond import Diamond
from ground import Ground
from player import *
from potion import Potion
from spritesheet import Spritesheet
from ui import UI
from game_over_screen import GameOverScreen
from water import Water
import random

from win_screen import WinScreen


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = None

    def createTileMap(self):
        empty_spaces = []
        for i, row in enumerate(first_tilemap):
            for j, column in enumerate(row):
                if column == ".":
                    Ground(self, j, i)
                    empty_spaces.append((j, i))
                if column == "B":
                    block = Block(self, j, i)
                    print(block.rect.x)
                    print(block.rect.y)
                if column == "P":
                    Ground(self, j, i)
                    self.player = Player(self, j, i)
                if column == "W":
                    Water(self, j, i)

        if empty_spaces:
            random_space = random.choice(empty_spaces)
            Armour(self, random_space[0], random_space[1])
            for i in range(NUM_POTIONS):
                self.check_empty_space(empty_spaces)
                random_space = random.choice(empty_spaces)
                Potion(self, random_space[0], random_space[1])
            for i in range(NUM_BOMBS):
                self.check_empty_space(empty_spaces)
                random_space = random.choice(empty_spaces)
                print(random_space)
                Bomb(self, random_space[0], random_space[1])
            for i in range(NUM_DIAMONDS):
                self.check_empty_space(empty_spaces)
                random_space = random.choice(empty_spaces)
                Diamond(self, random_space[0], random_space[1])

    def check_empty_space(self, empty_spaces):
        for i, row in enumerate(first_tilemap):
            for j, column in enumerate(row):
                if column == ".":
                    empty_spaces.append((j, i))

    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.water = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.potions = pygame.sprite.LayeredUpdates()
        self.armour = pygame.sprite.LayeredUpdates()
        self.bombs = pygame.sprite.LayeredUpdates()
        self.diamonds = pygame.sprite.LayeredUpdates()
        self.createTileMap()
        self.ui = UI()

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.ui.display(self.player)
        self.ui.count_diamons(self.player.num_diamonds)
        self.ui.count_bombs(len(self.player.num_bombs))
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # main loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.player.movement()

    def game_over(self):
        game_over_screen = GameOverScreen(self)
        game_over_screen.display()

    def win(self):
        win_screen = WinScreen(self)
        win_screen.display()

    def check_empty_space(self, empty_spaces):
        for i, row in enumerate(first_tilemap):
            for j, column in enumerate(row):
                if column == ".":
                    empty_spaces.append((j, i))
