#
# testing how to build a button
# src: https://stackoverflow.com/questions/40336960/creating-rect-buttons-with-pygame
#

import pygame
import sys


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    size = [200, 200]
    bg = [255, 255, 255]

    screen = pygame.display.set_mode(size)
    button = pygame.Rect(100, 100, 50, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos


                if button.collidepoint(mouse_pos):
                    print('button pressed at {0}'.format(mouse_pos))

        screen.fill(bg)
        pygame.draw.rect(screen, [255, 0, 0], button)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit


if __name__ == '__main__':
    main()
