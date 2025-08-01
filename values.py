from pygame import *

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
FPS = 60

game = True

BACKGROUND = 'Sprites\\road.png'
CAR = 'Sprites\\car.png'
BOX = 'Sprites\\box.png'

window = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#### CAR POSITION
UP = 70
CENTER = 200
DOWN = 350