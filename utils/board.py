import settings


def board_left():
    return settings.BOARD_POSITION[0]


def board_right():
    return settings.BOARD_POSITION[0] + settings.BOARD_WIDTH


def board_top():
    return settings.BOARD_POSITION[1]


def board_bottom():
    return settings.BOARD_POSITION[1] + settings.BOARD_HEIGHT


def board_center_x():
    return (settings.BOARD_POSITION[0] + settings.BOARD_WIDTH) / 2


def board_center_y():
    return (settings.BOARD_POSITION[1] + settings.BOARD_HEIGHT) / 2
