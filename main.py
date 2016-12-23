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

rKeyPressed = False
lKeyPressed = False
uKeyPressed = False
dKeyPressed = False

#set up the window
DISPLAYSURF = pygame.display.set_mode((wWidth, wHeight), 0, 32)
pygame.display.set_caption("Bermuda")

#main game loop
while True:
    DISPLAYSURF.fill(WHITE)

    if rKeyPressed:
        staffanx +=5
    if lKeyPressed:
        staffanx -=5
    if uKeyPressed:
        staffany -=5
    if dKeyPressed:
        staffany +=5
    
    #event handling loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            if not rKeyPressed:
                rKeyPressed = True
                staffanx += 5
        if event.type == KEYDOWN and event.key == K_LEFT:
            if not lKeyPressed:
                lKeyPressed = True
                staffanx -= 5
        if event.type == KEYDOWN and event.key == K_UP:
            if not uKeyPressed:
                uKeyPressed = True
                staffany -= 5
        if event.type == KEYDOWN and event.key == K_DOWN:
            if not dKeyPressed:
                dKeyPressed = True
                staffany += 5

        if event.type == KEYUP and event.key == K_RIGHT:
            rKeyPressed = False
        if event.type == KEYUP and event.key == K_LEFT:
            lKeyPressed = False
        if event.type == KEYUP and event.key == K_UP:
            uKeyPressed = False
        if event.type == KEYUP and event.key == K_DOWN:
            dKeyPressed = False

    DISPLAYSURF.blit(staffan, (staffanx, staffany))

    pygame.display.update()
    fpsClock.tick(FPS)
