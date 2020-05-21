#
# learning pygame part 1
# src: Chapter 17 of 'Invent Your Own Games With Python', by Al Sweigart
#

import pygame
import sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('window title display goes here')

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up fonts
basicFont = pygame.font.SysFont(None, 64)

# set up text
text = basicFont.render('howdy', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw white background
windowSurface.fill(WHITE)

# draw green polygon
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 156)))

# draw blue lines
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (60, 120))
pygame.draw.line(windowSurface, BLUE, (60, 120), (120, 120), 4)

# draw blue circle
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# draw red ellipse
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# draw text background rectangle
pygame.draw.rect(windowSurface, RED, (textRect.left - 20,
    textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get pixel array of surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# draw text onto surface
windowSurface.blit(text, textRect)

# draw window onto the screen
pygame.display.update()

# run game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
