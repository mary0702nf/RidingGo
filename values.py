from pygame import *
from functions import read_info

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
FPS = 60

running = True
active = True
musick = True
screen_status = "menu"
warning = False
window= display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

im_width = 400
im_heigh = 400
pose = 0
backgrounds = []
scroling = 0
data = read_info("info.json")
lifes = data["lifes"]
price = data["price"]
sum_coin = data["sum_coin"]
effort = lifes

r_x = 397
rects = []

BACKGROUND = 'Sprites\\road.png'
CAR = 'Sprites\\car.png'
BOX = 'Sprites\\box.png'
RULES = 'Sprites\\rules.png'
COIN = 'Sprites\\coin.png'
HEALTH = 'Sprites\\health.png'
HEALTH2 = 'Sprites\\health2.png'
COUNTER = 'Sprites\\coins.png'


#### BUTTONS SPRITES
START = 'Sprites\\start.png'
QUIT = 'Sprites\\quit.png'
MENU = 'Sprites\\menu.png'
UPGRADE = 'Sprites\\upgrade.png'
OK = 'Sprites\\ok.png'
WARNING = 'Sprites\\warning.png'

MENU_BGD = 'Sprites\\menu_bgd.png'
UPGRADE_BGD = 'Sprites\\UPGRADE_bgd.png'

INDICATOR = 'Sprites\\a.png'
BUTTON = 'Sprites\\button.png'


UP = 70
CENTER = 200
DOWN = 350
pos = [[1,0,0,0,1,0,2,0,1,1],
       [0,0,2,0,1,0,0,0,1,2],
       [0,0,1,0,2,0,1,0,0,2]]

#pos2 = [[1,1,0,0,0,0,0,1,0,1],
#       [0,0,2,1,0,0,2,0,1,2],
#       [0,2,0,0,0,1,1,0,0,0]]
#
#pos_list = []
#pos_list.append(pos1)
#pos_list.append(pos2)

################# BOXES and COINS
boxes = []
coins = []


##################### SOUNDS
BACKMUSIC = 'Sounds\\menu.mp3'
CRASH = 'Sounds\\car_crash.mp3'
GAME_OVER = 'Sounds\\game_over.mp3'
GET_COIN = 'Sounds\\coin.mp3'
CASH = 'Sounds\\cash_register.mp3'
CLICK = 'Sounds\\button_click.mp3'
WARNING_SOUND = 'Sounds\\warning.mp3'