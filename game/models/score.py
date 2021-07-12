from game.constants import FONT, WHITE, BLACK
import pygame


class Score(pygame.sprite.Sprite):
    # Score will be kept throughout the game.
    # Will be submitted to api when the game finishes.

    def __init__(self):
        super().__init__()
        self.number = 0
        self.font = pygame.font.SysFont(FONT, 14, bold=True)
        self.update()
        

    def update(self):
        image = self.font.render("Score: " + str(self.number), True, WHITE)
        self.image = self.image = pygame.Surface((90,30))
        self.image.fill(BLACK)
        self.image.blit(image, (3, 3))


