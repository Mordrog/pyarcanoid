import os

import settings
import pygame
from game_controller import GameController
from background import Background


def main():
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    pygame.display.set_caption('pyarcanoid')
    pygame.display.set_icon(pygame.image.load('assets/brick.png'))
    screen = pygame.display.set_mode([settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT])
    pygame_clock = pygame.time.Clock()

    background = Background(screen)
    game_controller = GameController(screen)

    running = True
    while running:
        pygame_clock.tick(60)
        screen.fill([0, 0, 0])
        background.update()
        game_controller.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_controller.pause = not game_controller.pause

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
