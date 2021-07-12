import pygame
from pygame.sprite import Sprite


class Unicorn(Sprite):
    # this is the player class, the player is a unicorn.
    # it will apper on the left side of the screen and can't off screen to the left.
    # because the unicorn is flying forward ofc.

    def __init__(self):
        super().__init__()

        image = pygame.image.load("game/assets/img/unicorn.png")
        self.image = pygame.transform.scale(image, (100, 95))
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 300

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
    