import pygame, sys, time
from pygame.locals import *

pygame.init()

wWidth  = 800
wHeight = 600
FPS = 30
fpsClock = pygame.time.Clock()

WHITE = (255, 255, 255)
staffan = pygame.image.load("staffan.jpg")
staffanx = 1
staffany = 1

#set up the window:
DISPLAYSURF = pygame.display.set_mode((wWidth, wHeight), 0, 32)
pygame.display.set_caption("Bermuda")

#main game loop:
while True:
    DISPLAYSURF.fill(WHITE)
    
    #event handling loop:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            staffanx += 5
        if event.type == KEYDOWN and event.key == K_LEFT:
            staffanx -= 5
        if event.type == KEYDOWN and event.key == K_UP:
            staffany -= 5
        if event.type == KEYDOWN and event.key == K_DOWN:
            staffany += 5

    DISPLAYSURF.blit(staffan, (staffanx, staffany))

    pygame.display.update()
    fpsClock.tick(FPS)
