import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # every cycle in a game loop is called a frame.

    running = True

    while running:
        for event in pygame.event.get():

            if event.type == KEYDOWN:   # any key based event.

                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False


if __name__ == "__main__":
    main()
