from pygame import *

from math import ceil
from values import *
from car import *
from box import *
from random import randint, choice
from button import Button

mixer.init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()

#mixer.music.load(BACKMUSIC)
#mixer.music.play()

menu_bgd = transform.scale(image.load(MENU_BGD), (900, 400))


b_start = Button(START, 250, 90, 310, 50)
b_menu = Button(MENU, 250, 90, 310, 160)
b_quit = Button(QUIT, 250, 90, 310, 270)

player = Car(CAR, 100, CENTER, 90, 60, 10)
parts = ceil(SCREEN_WIDTH / im_width) + 1


for i in range(parts):
    bg = transform.scale(image.load(BACKGROUND), (im_width, im_heigh))
    backgrounds.append(bg)

boxes = []
x = 170
for i in range(5):
    box = Box(BOX, x, choice(pose_y), 70, 70)
    boxes.append(box)
    x += 70


while running:
    i = 0
    for bg in backgrounds:
        window.blit(bg, (i*im_width + scroling, 0))
        i += 1

    keys = key.get_pressed()
    if keys[K_q]:
        running = False
    for e in event.get():
        if e.type == QUIT:
            running = False

    if screen_status == "menu":
       window.blit(menu_bgd, (0,0))
       b_start.reset()
       b_menu.reset()
       b_quit.reset()         
       if b_start.clicked():
           screen_status = "play"
       elif b_menu.clicked():
            print("MENU")
       elif b_quit.clicked():
            print("QUIT")
            running = False

    elif screen_status == "play":
        if abs(scroling) >= im_width:
            scroling = 0 
        else:
            scroling -= 7
        for box in boxes:
            if box.rect.x < 0:
                box.rect.x = randint(900, 970)
                box.rect.y = randint(UP, DOWN - 70)
        player.moving(UP,(DOWN - player.width))
        player.update()
        for b in boxes:
            b.moving(-5)
            b.update()
    

    display.update()
    clock.tick(FPS)

quit()