from pygame import *
from math import ceil
from values import *
from car import *
from box import *
from random import randint, choice


mixer.init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()

#mixer.music.load(BACKMUSIC)
#mixer.music.play()


screen_status = "Menu"

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

while game:

    i = 0
    for bg in backgrounds:
        screen.blit(bg, (i*im_width + scroling, 0))
        i += 1
    
    keys = key.get_pressed()
    if keys[K_q]:
        game = False
    for e in event.get():
        if e.type == QUIT:
            game = False

    if abs(scroling) >= im_width:
        scroling = 0 
    else:
        scroling -= 7

    for box in boxes:
        if box.rect.x < -40:
            box.rect.x = randint(900, 970)
            box.rect.y = choice(pose_y)


    player.moving(UP,(DOWN - player.width))
    player.update()

    for b in boxes:
        b.moving(-5)
        b.update()
    

    display.update()
    clock.tick(FPS)


quit()