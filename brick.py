import pygame

import settings


class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, position_vector, color):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('assets/brick.png').convert()
        self.image = pygame.transform.scale(self.image, settings.BRICK_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = position_vector.x
        self.rect.y = position_vector.y

        color_image = pygame.Surface(self.image.get_size()).convert_alpha()
        color_image.fill(color)
        self.image.blit(color_image, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    def update(self):
        self.screen.blit(self.image, self.rect)
