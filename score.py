import pygame

import settings


class Score(object):
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/arcade_fonts.TTF", 30)
        self.score = 0

    def update(self):
        hightext = self.font.render("HIGH SCORE", 1, (255, 0, 0))
        scoretext = self.font.render(str(self.score), 1, (255, 255, 255))
        self.screen.blit(hightext, hightext.get_rect(center=(settings.SCREEN_WIDTH/2, 20)))
        self.screen.blit(scoretext, scoretext.get_rect(center=(settings.SCREEN_WIDTH/2, 55)))
