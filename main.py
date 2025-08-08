from pygame import *
from functions import save_info
from math import ceil
from values import *
from car import *
from objects import Objects
from random import choice
from button import Button

mixer.init()
font.init()

screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()

mixer.music.load(BACKMUSIC)
mixer.music.set_volume(0.1)
mixer.music.play()
crash = mixer.Sound(CRASH)
coin_= mixer.Sound(GET_COIN)
game_over = mixer.Sound(GAME_OVER)
cash = mixer.Sound(CASH)
click = mixer.Sound(CLICK)
s_warning = mixer.Sound(WARNING_SOUND)
coin_.set_volume(0.3)
crash.set_volume(0.3)
click.set_volume(1.7)
cash.set_volume(0.5)
s_warning.set_volume(1.5)

data = read_info("info.json")
lifes = data["lifes"]
price = data["price"]
sum_coin = data["sum_coin"]

player = Car(CAR, 100, CENTER, 90, 55, 7)
parts = ceil(SCREEN_WIDTH / im_width) + 1

for i in range(parts):
    bg = transform.scale(image.load(BACKGROUND), (im_width, im_heigh))
    backgrounds.append(bg)

g_txt = font.Font(None, 150)
c_txt = font.Font(None, 50)
s_txt = font.Font(None, 70)

b_start = Button(START, 250, 90, 510, 50)
b_upgrade = Button(UPGRADE, 250, 90, 510, 160)
b_quit = Button(QUIT, 250, 90, 510, 270)
b_menu = Button(MENU, 250, 90, 30, 40)
heal_price = Button(BUTTON, 120, 40, 720, 30)
ok = Button(OK, 120, 80, 420, 180)

for i in range(lifes):
    fill_rect = Rect(r_x, 33, 28, 34)
    rects.append(fill_rect)
    r_x += 40

for p in pos:
    x = 900
    for i in p:
        if pos.index(p) == 0 and i == 1:
            box = Objects(BOX, x, UP, 60, 60, x, UP)
            boxes.append(box)
        elif pos.index(p) == 1 and i == 1:
           box = Objects(BOX, x, CENTER, 60, 60, x, CENTER)
           boxes.append(box)
        elif pos.index(p) == 2 and i == 1:
            box = Objects(BOX, x, DOWN, 60, 60, x, DOWN-90)
            boxes.append(box)
        x += 90
for p in pos:
    x = 900
    for i in p:
        if pos.index(p) == 0 and i == 2:
            coin = Objects(COIN, x, CENTER, 30, 30, x, UP + 30)
            coins.append(coin)
        elif pos.index(p) == 2 and i == 2:
            coin = Objects(COIN, x, CENTER, 30, 30, x, CENTER)
            coins.append(coin)
        elif pos.index(p) == 2 and i == 2:
            coin = Objects(COIN, x, CENTER, 30, 30, x, DOWN - 130)
            coins.append(coin)
        x += 90

while running:    
    i = 0
    for bg in backgrounds:
        window.blit(bg, (i*im_width + scroling, 0))
        i += 1
    keys = key.get_pressed()
    if keys[K_q]:
        running = False
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                if active:
                    pos = mouse.get_pos()
                    if b_start.rect.collidepoint(pos):
                        if musick == False:
                            mixer.music.play()
                        click.play()
                        screen_status = "play"
                        player.rect.x = 100
                        player.rect.y = CENTER
                        count_coins = 0
                        death = lifes
                        effort = lifes
                        for b in boxes:
                            b.rect.x = b.start_x
                            b.rect.y = b.start_y
                        for c in coins:
                            c.rect.x = c.start_x
                            c.rect.y = c.start_y
                    elif b_upgrade.rect.collidepoint(pos):
                        click.play()
                        screen_status = "upgrade"
                        b_menu.rect.x = 30
                        b_menu.rect.y = 40
                    elif b_quit.rect.collidepoint(pos):
                        click.play()
                        running = False
                    elif b_menu.rect.collidepoint(pos):
                        if musick == False:
                            mixer.music.play()
                        click.play()
                        screen_status = "menu"
                        b_start.rect.x = 510
                        b_start.rect.y = 50
                        b_quit.rect.x = 510
                        b_quit.rect.y = 270
                    elif heal_price.rect.collidepoint(pos):
                        if lifes < 8:
                            if sum_coin >= price:
                                cash.play()
                                lifes += 1
                                fill_rect = Rect(r_x, 33, 28, 34)
                                rects.append(fill_rect)
                                sum_coin -= price
                                price = price * 2
                                r_x += 40
                                death = lifes
                                effort = lifes
                                data["lifes"] = lifes 
                                data["price"] = price
                                data["sum_coin"] = sum_coin
                                save_info("info.json", data)
                            else:
                                s_warning.play()
                                warning = True

                    elif ok.rect.collidepoint(pos):
                        click.play()
                        warning = False


################################## МЕНЮ
##################################
    if screen_status == "menu":
        window.blit(transform.scale(image.load(MENU_BGD), (900, 400)), (0,0))
        window.blit(transform.scale(image.load(RULES), (SCREEN_HEIGHT - 10, SCREEN_HEIGHT - 10)), (5,5))
        b_start.reset()
        b_upgrade.reset()
        b_quit.reset()         


################################## ГРА
##################################
    elif screen_status == "play":
        active = False
        if abs(scroling) >= im_width:
            scroling = 0 
        else:
            scroling -= 7

        if player.collide(coin):
            coin_.play()
            count_coins +=1
            for c in coins:
                c.rect.x = c.start_x
                c.rect.y = c.start_y
        for b in boxes:
            if player.collide(b) and effort == 1:
                musick = False
                mixer.music.stop()
                game_over.play()
                screen_status = "game over"
                sum_coin += count_coins
                data["sum_coin"] = sum_coin
                save_info("info.json", data)
                g_over = g_txt.render("GAME", True, (255,0,0))
                g_over2 = g_txt.render("OVER", True, (255,0,0))
                b_menu.rect.x = 100
                b_menu.rect.y = 300
                b_start.rect.x = 550
                b_start.rect.y = 300
                active = True
            elif player.collide(b) and effort >= 0:
                crash.play()
                effort -= 1
                b.rect.x = b.start_x
                b.rect.y = b.start_y
        
        for b in boxes:
            if b.rect.x < -10:
                b.rect.x = b.start_x
                b.rect.y = b.start_y
        for c in coins:
            if coin.rect.x < -20:
                c.rect.x = c.start_x
                c.rect.y = c.start_y
        player.moving(UP,(DOWN - player.width +5))
        player.update()
        coin.moving(-5)
        coin.update()
        for b in boxes:
            b.moving(-5)
            b.update()
        window.blit((transform.scale(image.load(COUNTER), (160, 40))), (5,5))
        window.blit(c_txt.render(str(count_coins), True, (255,255,255)), (45, 10))
        x_l = x_d = 850
        for i in range(death):
            window.blit((transform.scale(image.load(HEALTH2), (40, 40))), (x_d, 0))
            x_d -= 50
        for i in range(effort):
            window.blit((transform.scale(image.load(HEALTH), (40, 40))), (x_l, 0))
            x_l -= 50

################################## КІНЕЦЬ ГРИ
##################################
    if screen_status == "game over":
        window.blit(transform.scale(image.load(MENU_BGD), (900, 400)), (0,0))
        window.blit(g_over, (270, 20))
        window.blit(g_over2, (290, 100))
        b_menu.reset()
        b_start.reset()

################################## ОНОВЛЕННЯ/ВДОСКОНАЛЕННЯ
##################################
    elif screen_status == "upgrade":
        b_start.rect.x = 900
        b_start.rect.y = 40
        b_quit.rect.x = 900
        b_quit.rect.y = 40
        window.blit(transform.scale(image.load(UPGRADE_BGD), (900, 400)), (0, 0))
        window.blit(transform.scale(image.load(INDICATOR),(320, 40)), (390, 30))
        window.blit(transform.scale(image.load(HEALTH),(50, 50)), (330, 30))
        window.blit((transform.scale(image.load(COUNTER), (240, 60))), (30,150))
        window.blit(s_txt.render(str(sum_coin), True, (255,255,255)), (90, 157))
        b_menu.reset()
        if lifes < 8:
            heal_price.reset()
            window.blit(c_txt.render(str(price), True, (255,255,255)), (730, 30))
            
        for r in rects:
            draw.rect(window, (255,0,0), r)
        if warning:
            window.blit(transform.scale(image.load(WARNING),(380, 270)), (290, 40))
            ok.reset()

    display.update()
    clock.tick(FPS)
quit()