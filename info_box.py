import pygame

import settings


class InfoBox(object):
    def __init__(self, screen):
        self.screen = screen
        self.continue_font = pygame.font.Font("assets/arcade_fonts.TTF", 20)
        self.info_font = pygame.font.Font("assets/arcade_fonts.TTF", 30)
        self.text = ""
        self.score = 0

    def update(self):
        infotext = self.info_font.render(str(self.text), 1, (255, 255, 255))
        continuetext = self.continue_font.render("Press space to continue", 1, (255, 255, 255))
        self.screen.blit(infotext, infotext.get_rect(center=(settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT/2)))
        if self.text != "":
            self.screen.blit(continuetext, continuetext.get_rect(center=(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2 + 50)))
