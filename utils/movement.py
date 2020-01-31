def is_moving_top_right(velocity):
    return velocity.x > 0 and velocity.y < 0


def is_moving_bottom_right(velocity):
    return velocity.x > 0 and velocity.y > 0


def is_moving_bottom_left(velocity):
    return velocity.x < 0 and velocity.y > 0


def is_moving_top_left(velocity):
    return velocity.x < 0 and velocity.y < 0


def is_moving_vertically(velocity):
    return velocity.y != 0


def is_moving_horizontally(velocity):
    return velocity.x != 0