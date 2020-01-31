import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("assets/arcanoid_board.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.screen.blit(self.image, self.rect)
