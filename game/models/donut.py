import pygame
import random
from pygame.sprite import Sprite
from game.constants import SCREEN_HT, SCREEN_RECT


class Donut(Sprite):
    # Donuts from this class will be appear randomly on the screen.
    # Can be collected by the unicorn.

    def __init__(self):
        super().__init__()
        image = pygame.image.load("game/assets/img/donut.png")
        self.image = image
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        max_x = SCREEN_RECT.width - self.rect.width
        max_y = 400
        self.rect.x = random.randint(0, max_x)
        self.rect.y = random.randint(0, max_y)
        self.speed = random.randint(5, 7)

    def update(self):
        self.rect.y += self.speed
        if len(self.groups()[0]) < 4:
            self.groups()[0].add(self.__class__())
        if self.rect.y > SCREEN_HT:
            self.kill()
        
