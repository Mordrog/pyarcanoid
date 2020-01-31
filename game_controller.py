import pygame
import settings

from skimage.draw import random_shapes
from ball import Ball
from brick import Brick
from info_box import InfoBox
from player import Player
from score import Score
from utils.board import board_left, board_right, board_top, board_bottom, board_center_x

PLAYER_START_POSITION = pygame.Vector2(board_center_x() - (settings.PLAYER_SIZE[0]) / 2,
                                       board_bottom() - settings.PLAYER_SIZE[1])
BALL_START_POSITION = pygame.Vector2(board_center_x() - (settings.BALL_SIZE[0]) / 2, board_bottom() * 3 / 4)


class GameController(object):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.score = Score(screen)
        self.info_box = InfoBox(screen)
        self.ball = Ball(screen, BALL_START_POSITION)
        self.player = Player(screen, PLAYER_START_POSITION)
        self.bricks = pygame.sprite.Group()
        self.pause = True
        self.generate_level()

    def generate_level(self):
        level_setup = random_shapes(
            image_shape=settings.BRICKS_DIMENSION,
            min_shapes=10,
            max_shapes=20,
            min_size=3,
            max_size=10,
            allow_overlap=True,
            intensity_range=((30, 255),))[0]
        for x in range(settings.BRICKS_DIMENSION[0]):
            for y in range(settings.BRICKS_DIMENSION[1]):
                if all(color != 255 for color in level_setup[x][y]):
                    position = pygame.Vector2(board_left() + settings.BRICKS_POSITION[0] + x * settings.BRICK_SIZE[0],
                                              board_top() + settings.BRICKS_POSITION[1] + y * settings.BRICK_SIZE[1])
                    self.bricks.add(Brick(self.screen, position, level_setup[x][y]))

    def is_game_over(self):
        return self.ball.rect.top > board_bottom()

    def is_level_complete(self):
        return len(self.bricks) == 0

    def has_ball_hit_player(self):
        return self.player.rect.colliderect(self.ball.rect) and self.ball.velocity.y > 0

    def reset(self):
        self.ball.reset()
        self.player.reset()
        self.generate_level()

    def update(self):
        self.score.update()
        self.info_box.update()

        if not self.pause:
            self.info_box.text = ""

            if self.is_level_complete():
                self.pause = True
                self.reset()
                self.info_box.text = "LEVEL COMPLETE"

            self.player.update()
            self.ball.update()
            self.bricks.update()

            if self.has_ball_hit_player():
                self.ball.bounce_of_player(self.player.rect)

            collide_bricks = pygame.sprite.spritecollide(self.ball, self.bricks, False)
            if collide_bricks:
                self.ball.bounce(collide_bricks[0].rect)
                self.bricks.remove(collide_bricks)
                self.score.score += 10 * len(collide_bricks)

            if self.is_game_over():
                self.pause = True
                self.score.score = 0
                self.reset()
                self.info_box.text = "GAME OVER"
        elif self.info_box.text == "":
            self.info_box.text = "PAUSE"
