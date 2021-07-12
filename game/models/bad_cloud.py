import pygame
import random
from pygame.sprite import Sprite
from game.constants import SCREEN_HT, SCREEN_RECT, WHITE


class BadCloud(Sprite):
    # This is the class for bad clouds.
    # When it collides with the unicorn, it will cause point reduction.

    def __init__(self):
        super().__init__()
        image = pygame.image.load("game/assets/img/bad_cloud.png")
        self.image = image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        max_x = SCREEN_RECT.width - self.rect.width
        max_y = 200
        self.rect.x = random.randint(0, max_x)
        self.rect.y = random.randint(0, max_y)
        self.speed = random.randint(2,4)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_HT:
            self.kill()
        
