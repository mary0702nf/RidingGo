from pygame import *
from math import ceil
from values import *
from car import *
from box import *
from random import randint

mixer.init()


BACKMUSIC = 'menu.mp3'

#mixer.music.load(BACKMUSIC)
#mixer.music.play()

im_width = 400
im_heigh = 400
pose = 0
backgrounds = []




player = Car(CAR, 100, CENTER, 90, 60, 10)
clock = time.Clock()

parts = ceil(SCREEN_WIDTH / im_width) + 1
scroling = 0



for i in range(parts):
    bg = transform.scale(image.load(BACKGROUND), (im_width, im_heigh))
    backgrounds.append(bg)

boxes = []
x = 100

for i in range(5):
    box = Box(BOX, x, randint(UP, DOWN - 70), 70, 70)
    boxes.append(box)
    x += 200



while game:
    i = 0
    for bg in backgrounds:
        window.blit(bg, (i*im_width + scroling, 0))
        i += 1
    
    for e in event.get():
        if e.type == QUIT:
            game = False


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