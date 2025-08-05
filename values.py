from pygame import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
FPS = 60

BACKMUSIC = 'menu.mp3'

running = True
window= display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BACKGROUND = 'Sprites\\road.png'

im_width = 400
im_heigh = 400
pose = 0
backgrounds = []
scroling = 0


CAR = 'Sprites\\car.png'
BOX = 'Sprites\\box.png'
#### BUTTONS SPRITES
START = 'Sprites\\start.png'
QUIT = 'Sprites\\quit.png'
MENU = 'Sprites\\menu.png'
UPGRADE = 'Sprites\\upgrade.png'
MENU_BGD = 'Sprites\\menu_bgd.png'
#### CAR POSITION
UP = 70
CENTER = 200
DOWN = 350

pose_y = [UP, CENTER - 35, DOWN - 100]
screen_status = "menu"