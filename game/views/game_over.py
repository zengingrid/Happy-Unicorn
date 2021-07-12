import pygame
from game.constants import *


class GameOverView:
    # Displays game over when the unicorn didn't reach the next level.
    # Shows player's last level played

    def __init__(self, level, player):
        self._level = level
        self._player = player

    def display(self, window):
        surface = pygame.Surface(WINDOW_SIZE)
        surface.fill((255,255, 255, 50))
        window.blit(surface, (0, 0))
        image = pygame.image.load("game/assets/img/game_over.png")

        font = pygame.font.SysFont(FONT, 24, bold=True)
        font2 = pygame.font.SysFont(FONT, 36, bold=True)
        text = font.render(f"{self._player} Level {self._level} Reached" , True, BLACK)
        text2 = font2.render(f" GAME OVER", True, BLACK)
        window.blit(image,(70,100))
        window.blit(text, (70, 300))
        window.blit(text2, (75, 330))
        pygame.display.flip()

        