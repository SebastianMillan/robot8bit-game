from io import open

import pygame.mixer

pygame.mixer.init()

WIN_WIDTH=1312
WIN_HEIGHT=800
TILESIZE =32
FPS=15

WHITE=(255,255,255)
BLACK=(0,0,0)

PLAYER_LAYER=4
POTION_LAYER=3
DIAMOND_LAYER=3
BOMB_LAYER=3
ARMOUR_LAYER=3
BLOCK_LAYER=2
WATER_LAYER=2
GROUND_LAYER=1

PLAYER_SPEED=32
PLAYER_HEALTH=10
DAMAGE_COLLIDE=1
DAMAGE_WATER=3
POTION_HEALTH=3
GENERAL_FONT="assests/fonts/arial_narrow_7.ttf"


BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ITEM_BOX_SIZE=80
UI_FONT_SIZE=18

UI_BG_COLOR='#222222'
UI_BORDER_COLOR='#111111'
TEXT_COLOR='#EEEEEE'

HEALTH_COLOR='red'
UI_BORDER_COLOR_ACTIVE='gold'

file_path1 = 'assests/maps/map1.txt'
with open(file_path1, 'r') as file:
    first_tilemap = [list(line.strip()) for line in file]
with open(file_path1, 'r') as file:
    last_line = file.readlines()[-1]
NUM_BOMBS=int(last_line[2])
NUM_DIAMONDS=int(last_line[6])
NUM_POTIONS=int(last_line[10])

SOUND_TAKE_DIAMOND= pygame.mixer.Sound('assests/audio/diamond.mp3')
SOUND_THROW_BOMB= pygame.mixer.Sound('assests/audio/explosion.mp3')
SOUND_DAMAGE= pygame.mixer.Sound('assests/audio/damage.mp3')
SOUND_DEAD= pygame.mixer.Sound('assests/audio/dead.mp3')
SOUND_WIN= pygame.mixer.Sound('assests/audio/win.mp3')
SOUND_ARMOURED= pygame.mixer.Sound('assests/audio/armoured.mp3')
SOUND_GET_ARMOURED= pygame.mixer.Sound('assests/audio/get_armour.mp3')
SOUND_HEALTH=pygame.mixer.Sound('assests/audio/health.mp3')
SOUND_MUSIC=pygame.mixer.Sound('assests/audio/music.mp3')
SOUND_INTRO=pygame.mixer.Sound('assests/audio/intro.mp3')
SOUND_GAME_OVER=pygame.mixer.Sound('assests/audio/game_over.mp3')
SOUND_TAKE_BOMB=pygame.mixer.Sound('assests/audio/take_bomb.mp3')

SPRITE_BOMB='assests/images/bomb_sprite.png'
SPRITE_BLOCK='assests/images/wall_sprite.png'
SPRITE_ARMOUR='assests/images/armour.png'
SPRITE_DIAMOND='assests/images/diamond_sprite.png'
SPRITE_FLOOR='assests/images/floor_sprite.png'
SPRITE_BASIC_PLAYER='assests/images/basic_robot_sprite.png'
SPRITE_ARMOUR_PLAYER='assests/images/armoured_robot_sprite.png'
SPRITE_POTION='assests/images/health_sprite.png'
SPRITE_WATER='assests/images/water_sprite.png'






