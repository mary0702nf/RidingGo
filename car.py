from pygame import *
from values import *


class Car(sprite.Sprite):
    def __init__(self, sprite_img, x, y, size_x, size_y, step):
        self.step = step
        self.width = size_x
        self.height = size_y
        self.image = transform.scale(image.load(sprite_img), (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def moving(self, start_pose, end_pose):
        keys = key.get_pressed()
        if keys[K_a]:
            if self.rect.x > 0:
                self.rect.x -= self.step
        elif keys[K_d]:
            if self.rect.x < 820:
                self.rect.x += self.step
        elif keys[K_w]:
            if self.rect.y > start_pose:
                self.rect.y -= self.step
        elif keys[K_s]:
            if self.rect.y < end_pose:
                self.rect.y += self.step

