import pygame
from game.constants import *


class LevelDoneView:
    # Displays a message when the player completes a level
    # Tells player the next level goal

    def __init__(self, level):
        self._level = level

    def display(self, window):
        surface = pygame.Surface(WINDOW_SIZE)

        # 50 is the alpha value here
        surface.fill((0, 0, 0, 50))
        window.blit(surface, (0, 0))

        pygame.draw.rect(window, LEVEL_DONE_COLOR, LEVEL_DONE_MSG_RECT)
        font = pygame.font.SysFont(FONT, 20, bold=True)
        font2 = pygame.font.SysFont(FONT, 16, bold=True)
        text = font.render(f"Level {self._level-1} completed!" , True, WHITE)
        text2 = font2.render(f" Next level goal: {(self._level) * DONUT_PER_LEVEL}", True, WHITE)
        window.blit(text, LEVEL_DONE_TXT_OFFSET)
        window.blit(text2, LEVEL_DONE_TXT_OFFSET2)
        pygame.display.flip()
