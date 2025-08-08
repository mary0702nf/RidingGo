from pygame import *
from values import *

class Objects(sprite.Sprite):
    def __init__(self, sprite_img, x, y, size_x, size_y, start_x = None, start_y =None):
        self.width = size_x
        self.height = size_y
        self.image = transform.scale(image.load(sprite_img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = start_x
        self.start_y = start_y

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def moving(self, step):
        self.rect.x += step