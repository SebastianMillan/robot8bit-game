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

with open('assests/maps/map1.txt', 'r') as file:
    first_tilemap = [list(line.strip()) for line in file]

file=open('assests/maps/config_map1.txt','r').read()
NUM_BOMBS=int(file[2])
NUM_DIAMONDS=int(file[6])
NUM_POTIONS=int(file[10])

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






