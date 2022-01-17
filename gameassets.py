import pygame
from pygame import mixer
import os

mixer.init()

#SCREEN properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spider-Man: Into The 8 Bit-Verse')

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define game variables
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 16
COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21
MAX_LEVELS = 2
screen_scroll = 0
bg_scroll = 0
level = 1
start_game = False
start_intro = False


#define player action variables
moving_left = False
moving_right = False
shoot = False
grenade = False
grenade_thrown = False

#---------------------------------------------------------------------------------------------------------------------------------------#
#ASSETS

#load music and sounds
pygame.mixer.music.load('audio/SpidermanTheme.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1, 0.0, 5000)
jump_fx = pygame.mixer.Sound('audio/jump.wav')
jump_fx.set_volume(0.05)
shot_fx = pygame.mixer.Sound('audio/shot.wav')
shot_fx.set_volume(0.05)
grenade_fx = pygame.mixer.Sound('audio/grenade.wav')
grenade_fx.set_volume(0.05)


#IMAGES
#button images
start_img = pygame.image.load('img/start_btn.png').convert_alpha()
exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()
restart_img = pygame.image.load('img/restart_btn.png').convert_alpha()
#game-background
city4_img = pygame.image.load('img/Background/city_background.jpg').convert_alpha()
city_img = pygame.image.load('img/Background/city_background.jpg').convert_alpha()
city2_img = pygame.image.load('img/Background/city_background.jpg').convert_alpha()
city3_img = pygame.image.load('img/Background/city_background.jpg').convert_alpha()
city4_img = pygame.image.load('img/Background/city_background.jpg').convert_alpha()
#menu-background
menu_web = pygame.image.load('img/Background/web wallpaper.jpg')
#store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'img/Tile/{x}.png')
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

#Spidey's Web image
web_img = pygame.image.load('img/icons/web.png').convert_alpha()
web_ammo = pygame.image.load('img/icons/webammo.png')

#Venom's Web image
venom_web_img = pygame.image.load('img/icons/venomweb.png')

#grenade
grenade_img = pygame.image.load('img/icons/grenade.png').convert_alpha()
#pick up boxes
health_box_img = pygame.image.load('img/icons/health_box.png').convert_alpha()
web_fluid = pygame.image.load('img/icons/web_fluid.png').convert_alpha()
grenade_box_img = pygame.image.load('img/icons/grenade_box.png').convert_alpha()
item_boxes = {
    'Health'    : health_box_img,
    'Ammo'      : web_fluid,
    'Grenade'   : grenade_box_img
}

#DEFINING COLORS
BG = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
