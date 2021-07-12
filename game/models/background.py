import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    # This is class for rolling background

    def __init__(self, image, speed=1.4):
        super().__init__()

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    
    def update(self):
        self.rect.x -= self.speed

        if self.rect.x <-500:
            self.rect.x = self.rect.width


        