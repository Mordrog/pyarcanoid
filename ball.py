import pygame
import settings
import utils.collision
import utils.movement


class Ball(pygame.sprite.Sprite):


    def __init__(self, screen, start_position_vector):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.velocity = pygame.Vector2(0, -settings.BALL_SPEED)
        self.start_position = start_position_vector
        self.image = pygame.image.load('assets/ball.png').convert()
        self.image = pygame.transform.scale(self.image, settings.BALL_SIZE)
        self.rect = self.image.get_rect()
        self.reset()

    def bounce_horizontally(self):
        self.velocity = self.velocity.reflect(pygame.Vector2(0, 1))

    def bounce_vertically(self):
        self.velocity = self.velocity.reflect(pygame.Vector2(1, 0))

    def bounce(self, hit_rect):
        top_diff = abs(self.rect.centery - hit_rect.top)
        bottom_diff = abs(self.rect.centery - hit_rect.bottom)
        right_diff = abs(self.rect.centerx - hit_rect.right)
        left_diff = abs(self.rect.centerx - hit_rect.left)

        if utils.movement.is_moving_top_right(self.velocity):
            if left_diff > bottom_diff:
                self.bounce_horizontally()
            else:
                self.bounce_vertically()
        elif utils.movement.is_moving_bottom_right(self.velocity):
            if left_diff > top_diff:
                self.bounce_horizontally()
            else:
                self.bounce_vertically()
        elif utils.movement.is_moving_bottom_left(self.velocity):
            if right_diff > top_diff:
                self.bounce_horizontally()
            else:
                self.bounce_vertically()
        elif utils.movement.is_moving_top_left(self.velocity):
            if right_diff > bottom_diff:
                self.bounce_horizontally()
            else:
                self.bounce_vertically()
        elif utils.movement.is_moving_vertically(self.velocity):
            self.bounce_horizontally()
        elif utils.movement.is_moving_horizontally(self.velocity):
            self.bounce_vertically()

    def bounce_of_player(self, player_rect):
        self.velocity = self.velocity.reflect(pygame.Vector2(0, 1))
        if self.rect.right > player_rect.centerx:
            angle = (self.rect.right - player_rect.centerx) / (
                        settings.PLAYER_SIZE[0] / 2) * settings.MAX_BOUNCE_OF_PLAYER_ANGLE
            self.velocity = self.velocity.rotate(angle)
        else:
            angle = (self.rect.left - player_rect.centerx) / (
                        settings.PLAYER_SIZE[0] / 2) * settings.MAX_BOUNCE_OF_PLAYER_ANGLE
            self.velocity = self.velocity.rotate(angle)

    def reset(self):
        self.velocity = pygame.Vector2(0, -settings.BALL_SPEED)
        self.rect.x = self.start_position.x
        self.rect.y = self.start_position.y

    def update(self):
        if utils.collision.test_right_wall_collide(self.rect):
            self.bounce_vertically()
        if utils.collision.test_left_wall_collide(self.rect):
            self.bounce_vertically()
        if utils.collision.test_top_wall_collide(self.rect):
            self.bounce_horizontally()

        self.rect = self.rect.move(self.velocity)
        self.screen.blit(self.image, self.rect)
