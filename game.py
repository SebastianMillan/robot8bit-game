from armour import Armour
from block import Block
from ground import Ground
from player import *
from potion import Potion
from spritesheet import Spritesheet
from ui import UI
from game_over_screen import GameOverScreen
from water import Water
import random


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player=None

    def createTileMap(self):
        empty_spaces = []
        for i, row in enumerate(first_tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    self.player=Player(self, j, i)
                if column == "W":
                    Water(self,j,i)
                if column == ".":
                    empty_spaces.append((j, i))
        if empty_spaces:
            first_random_space = random.choice(empty_spaces)
            Potion(self, first_random_space[0], first_random_space[1])
            second_random_space = random.choice(empty_spaces)
            while first_random_space == second_random_space:
                second_random_space = random.choice(empty_spaces)
            Potion(self, second_random_space[0], second_random_space[1])
            third_random_space = random.choice(empty_spaces)
            while second_random_space == third_random_space:
                third_random_space = random.choice(empty_spaces)
            Potion(self, third_random_space[0], third_random_space[1])
            fourth_random_space = random.choice(empty_spaces)
            while third_random_space == fourth_random_space:
                fourth_random_space = random.choice(empty_spaces)
            Armour(self, third_random_space[0], third_random_space[1])


    def new(self):
        self.playing = True
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.water = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.potions=pygame.sprite.LayeredUpdates()
        self.armour = pygame.sprite.LayeredUpdates()
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
        game_over_screen=GameOverScreen(self)
        game_over_screen.display()




