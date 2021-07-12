import pygame
from game.constants import *
from pygame.locals import *
from game.controllers.game import GameController


class GameInitiator():
    # This is class for the game menu.

    def __init__(self, player_name):
        pygame.init()
        self.player = player_name

        # window set up
        pygame.mouse.set_visible(True)
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.window.fill(BLUE)
        image = pygame.image.load("game/assets/img/start.png")
        self.window.blit(image, (110,50))
        donut = pygame.image.load("game/assets/img/donut.png")
        self.window.blit(donut, (100,230))

        # instruction
        self.font_small = pygame.font.SysFont(FONT, 14, bold=True)
        text = self.font_small.render("Hello player, this is the happy unicorn game!", True, BLACK)
        text1 = self.font_small.render("Use the arrow keys to collect donuts", True, BLACK)
        text2 = self.font_small.render("And avoid the bad clouds", True, BLACK)
        self.window.blit(text, (30, 35))
        self.window.blit(text1, (30, 50))
        self.window.blit(text2, (30, 65))

        # START BUTTON
        rectangle_surface = pygame.Surface((200, 100))
        self.window.blit(rectangle_surface.convert(), (100, 300))
        self.font = pygame.font.SysFont(FONT, 48, bold=True)
        text4 = self.font.render("Start", True, WHITE)
        self.button = pygame.Surface((90,30))
        self.button.fill(BLACK)
        self.window.blit(text4, (135, 310))

        pygame.display.update()
        
        # input music
        pygame.mixer.music.load("game/assets/music/Agnes.mp3")
        pygame.mixer.music.play(-1, 0.0)

    # runs the main game when the player click start.
    def run(self):
        running = True
        while running:            
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    return False
                elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_ESCAPE:
                            return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 100 < event.pos[0] < 300 and 300 < event.pos[1] < 400:
                       self.game = GameController(self.player)
                       self.game.run()
                       if self.game.running == False:
                           return False