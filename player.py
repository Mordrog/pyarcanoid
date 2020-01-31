import pygame
import settings
import utils.collision


class Player(pygame.sprite.Sprite):

    def __init__(self, screen, start_position_vector):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.velocity = pygame.Vector2(0, 0)
        self.start_position = start_position_vector
        self.image = pygame.image.load('assets/player.png').convert()
        self.image = pygame.transform.scale(self.image, settings.PLAYER_SIZE)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.velocity = pygame.Vector2(0, 0)
        self.rect.x = self.start_position.x
        self.rect.y = self.start_position.y

    def update(self):
        keys = pygame.key.get_pressed()

        new_velocity = pygame.Vector2(settings.PLAYER_SPEED, 0)

        if keys[pygame.K_LEFT] and not utils.collision.test_left_wall_collide(self.rect.move(-new_velocity)):
            self.velocity = -new_velocity
        elif keys[pygame.K_RIGHT] and not utils.collision.test_right_wall_collide(self.rect.move(new_velocity)):
            self.velocity = new_velocity
        else:
            self.velocity = pygame.Vector2(0, 0)

        self.rect = self.rect.move(self.velocity)
        self.screen.blit(self.image, self.rect)
