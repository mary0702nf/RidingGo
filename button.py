from pygame import *
from values import *

class Button(sprite.Sprite):
    def __init__(self, img, w, h, x , y):
        self.width = w
        self.height = h
        self.img = transform.scale(image.load(img), (self.width, self.height))
        self.rect = self.img.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def reset(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

    def clicked(self):
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1:
                    pos = mouse.get_pos()
                    print(pos)
                    if self.rect.collidepoint(pos):
                        print("CLICKED")
                        return True