import requests
import itertools
import pygame.locals

from game.constants import *
from game.models.bad_cloud import BadCloud
from game.models.countdown import Countdown
from game.models.donut import Donut
from game.models.unicorn import Unicorn
from game.models.background import Background
from game.models.score import Score
from game.models.countdown import Countdown
from game.views.level_done import LevelDoneView
from game.views.game_over import GameOverView


class GameController():
    def __init__(self, player_name):
        self.level = 1
        self.countdown = Countdown()
        self.player = player_name
        self.running = True

        # set up window
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        # set up sound
        pygame.mixer.music.load("game/assets/music/Unicorn Song.mp3")
        pygame.mixer.music.play(-1, 0.0)

        # set up unicorn (player)
        self.unicorn = Unicorn()

        # initiate score count
        self.score = Score()
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)

        # set up donut sprite group
        self.donuts = pygame.sprite.Group()
        self.donuts.add(Donut())

        # set up bad cloud spirit group
        self.clouds = pygame.sprite.Group()
        self.clouds.add(BadCloud())

        self.clock = pygame.time.Clock()
        self._scrolling_background()

        # set up views
        self.level_done_view = LevelDoneView(self.level)
        self.game_over_view = GameOverView(self.level, self.player)
    
    #method for creating scrolling background
    def _scrolling_background(self):
        bg1 = Background("game/assets/img/sky_night.png")
        bg2 = Background("game/assets/img/sky.png")
        bg2.rect.x = bg2.rect.width
        self.backgrounds = pygame.sprite.Group(bg1, bg2)
    
    # game 
    def run(self):
        while self.running == True:
            self.clock.tick(FRAME_PER_SEC)

            for s in [sprite for sprite in itertools.chain(self.donuts.sprites(), self.clouds.sprites()) if not sprite.alive()]:
                del s

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.locals.KEYDOWN:
                        if event.key == pygame.locals.K_ESCAPE:
                            self.running = False
                elif self.countdown.counter == 0:
                    if self.score.number >= self.level * DONUT_PER_LEVEL:
                        # if player reach the target score, level up
                        self.level += 1
                        self.level_done_view = LevelDoneView(self.level)
                        self.level_done_view.display(self.screen)
                        pygame.time.wait(2000)
                        self.countdown.counter = 12
                        for idx in range(self.level):
                            self.clouds.add(BadCloud())
                    elif self.score.number < self.level * DONUT_PER_LEVEL:
                        # if player didn't reach the target score, gameover
                        self.game_over_view = GameOverView(self.level,self.player)
                        self.game_over_view.display(self.screen)
                        pygame.time.wait(2000)
                        # send player's final score to api with the player's name.
                        requests.put("http://localhost:5000/api/score", json={"name": self.player, "score": self.score.number})
                        self.running = False

                elif event.type == self.timer_event:
                    self.countdown.counter -= 1

            keys = pygame.key.get_pressed()
            if keys[pygame.locals.K_UP]:
                self.unicorn.rect.y = min(self.unicorn.rect.y - 10, SCREEN_HT)
            elif keys[pygame.locals.K_DOWN]:
                self.unicorn.rect.y = max(self.unicorn.rect.y + 10, 0)
            elif keys[pygame.locals.K_RIGHT]:
                self.unicorn.rect.x = min(self.unicorn.rect.x + 10, SCREEN_WID)
            elif keys[pygame.locals.K_LEFT]:
                self.unicorn.rect.x = max(self.unicorn.rect.x - 10, 0)
            
            self.donuts.update()
            self.clouds.update()

            if pygame.sprite.spritecollide(self.unicorn, self.donuts, dokill=True):
                # when unicorn collides with donuts, unicorn gets a point
                self.score.number += 1
            if pygame.sprite.spritecollide(self.unicorn, self.clouds, dokill=True):
                # when unicorn collides with bad clouds, unicorn losses 10 points
                self.score.number -= 10
                
            self.score.update()
            self.countdown.update()
            self.backgrounds.update()
            self.backgrounds.draw(self.screen)
            self.screen.blit(self.unicorn.image, self.unicorn.rect)
            self.screen.blit(self.score.image, (0,0))
            self.screen.blit(self.countdown.image, (330, 0))
            self.donuts.draw(self.screen)
            self.clouds.draw(self.screen)
            pygame.display.update()

        
        

        