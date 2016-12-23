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
xSpeed = 100 #px/s
ySpeed = 100 #px/s

rKeyPressed = False
lKeyPressed = False
uKeyPressed = False
dKeyPressed = False

#set up the window
DISPLAYSURF = pygame.display.set_mode((wWidth, wHeight), 0, 32)
pygame.display.set_caption("Bermuda")

#init previus time for delta calculation
prevTime = pygame.time.get_ticks()

#main game loop
while True:
    DISPLAYSURF.fill(WHITE)

    #calculate delta time
    currentTime = pygame.time.get_ticks()
    deltaTime = currentTime - prevTime
    deltaTime /= 1000 #convert from ms to s
    prevTime = currentTime

    if rKeyPressed:
        staffanx += xSpeed * deltaTime
    if lKeyPressed:
        staffanx -= xSpeed * deltaTime
    if uKeyPressed:
        staffany -= ySpeed * deltaTime
    if dKeyPressed:
        staffany += ySpeed * deltaTime
    
    #event handling loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_RIGHT:
            if not rKeyPressed:
                rKeyPressed = True
                staffanx +=  xSpeed * deltaTime
        if event.type == KEYDOWN and event.key == K_LEFT:
            if not lKeyPressed:
                lKeyPressed = True
                staffanx -=  xSpeed * deltaTime
        if event.type == KEYDOWN and event.key == K_UP:
            if not uKeyPressed:
                uKeyPressed = True
                staffany -=  ySpeed * deltaTime
        if event.type == KEYDOWN and event.key == K_DOWN:
            if not dKeyPressed:
                dKeyPressed = True
                staffany +=  ySpeed * deltaTime

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