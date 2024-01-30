import pygame
from config import *
from spritesheet import Spritesheet


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self._layer=PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE
        self.x_change = 0
        self.y_change = 0

        self.character_spritesheet = Spritesheet('assests/images/basic_robot_sprite.png')
        self.character_armoured_spritesheet = Spritesheet('assests/images/armoured_robot_sprite.png')
        self.image = self.character_spritesheet.get_sprite(1, 1, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.max_health = PLAYER_HEALTH
        self.actual_health = self.max_health
        self.is_armoured = False
        self.has_the_armour = False
        self.num_bombs=0
        self.num_diamonds=0

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
        self.dive_water()
        self.change_armoured()
        self.take_potion()
        self.take_armour()
        self.take_bomb()
        self.take_diamond()
        self.death()
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.playing = False
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change -= PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.x_change += PLAYER_SPEED
                elif event.key == pygame.K_UP:
                    self.y_change -= PLAYER_SPEED
                elif event.key == pygame.K_DOWN:
                    self.y_change += PLAYER_SPEED
                elif event.key == pygame.K_k:
                    if self.has_the_armour:
                        self.is_armoured = not self.is_armoured

    def collide_blocks(self, direction):
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            self.actual_health -= DAMAGE_COLLIDE
            if direction == "x":
                if hits:
                    if self.x_change > 0:
                        self.rect.x = hits[0].rect.left - self.rect.width
                    if self.x_change < 0:
                        self.rect.x = hits[0].rect.right
            if direction == "y":
                if hits:
                    if self.y_change > 0:
                        self.rect.y = hits[0].rect.top - self.rect.height
                    if self.y_change < 0:
                        self.rect.y = hits[0].rect.bottom

    def dive_water(self):
        dive = pygame.sprite.spritecollide(self, self.game.water, False)
        if not self.is_armoured:
            if dive:
                if self.x_change > 0:
                    self.actual_health -= DAMAGE_WATER
                if self.x_change < 0:
                    self.actual_health -= DAMAGE_WATER
                if self.y_change > 0:
                    self.actual_health -= DAMAGE_WATER
                if self.y_change < 0:
                    self.actual_health -= DAMAGE_WATER

    def death(self):
        if self.actual_health <= 0:
            self.game.game_over()

    def change_armoured(self):
        if self.is_armoured:
            self.image = self.character_armoured_spritesheet.get_sprite(1, 1, self.width, self.height)
        else:
            self.image = self.character_spritesheet.get_sprite(1, 1, self.width, self.height)

    def take_potion(self):
        hits = pygame.sprite.spritecollide(self, self.game.potions, True)
        if hits and not self.actual_health>=self.max_health:
            self.actual_health+=POTION_HEALTH

    def take_armour(self):
        hits = pygame.sprite.spritecollide(self, self.game.armour, True)
        if hits:
            self.has_the_armour=True
            self.is_armoured=True

    def take_bomb(self):
        hits = pygame.sprite.spritecollide(self, self.game.bombs, True)
        if hits:
            self.num_bombs+=1

    def take_diamond(self):
        hits = pygame.sprite.spritecollide(self, self.game.diamonds, True)
        if hits:
            self.num_diamonds+=1


