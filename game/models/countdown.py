from game.constants import WHITE, BLACK, FONT
import pygame


class Countdown(pygame.sprite.Sprite):
    # The countdown class serves as a timer, it limits every level to 10s.

    def __init__(self):
        super().__init__()
        self.counter = 10
        self.font = pygame.font.SysFont(FONT, 14, bold=True)
        self.update()
        

    def update(self):
        image = self.font.render("Time: " + str(self.counter), True, WHITE)
        self.image = pygame.Surface((90,30))
        self.image.fill(BLACK)
        self.image.blit(image, (3, 3))


