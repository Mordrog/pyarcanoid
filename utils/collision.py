import settings
from utils.board import board_right, board_left, board_top


def test_right_wall_collide(rect):
    return rect.x + rect.width > board_right()


def test_left_wall_collide(rect):
    return rect.x < board_left()


def test_top_wall_collide(rect):
    return rect.y < board_top()
