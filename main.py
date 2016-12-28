import pygame, sys, time
from pygame.locals import *
import GameObject

def main():
    pygame.init()

    wWidth  = 800
    wHeight = 600

    WHITE = (255, 255, 255)
    anne = pygame.image.load("sprites/Anne_01.png")
    annex4 = pygame.image.load("sprites/Anne_01_x4.png")
    staffan = pygame.image.load("staffan.jpg")
    staffanX = 1
    staffanY = 1
    xSpeed = 100 #px/s
    ySpeed = 100 #px/s

    #set up the window
    DISPLAYSURF = pygame.display.set_mode((wWidth, wHeight), 0, 32)
    pygame.display.set_caption("Bermuda")

    #init previus time for delta calculation
    prevTime = pygame.time.get_ticks()
    global dT

    #main game loop
    while True:
        DISPLAYSURF.fill(WHITE)

        #calculate delta time
        currentTime = pygame.time.get_ticks()
        dT = currentTime - prevTime
        dT /= 1000 #convert from ms to s
        prevTime = currentTime
        
        #event handling loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        #movement
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            staffanX +=  xSpeed * dT
        if keys[K_LEFT]:
            staffanX -=  xSpeed * dT
        if keys[K_UP]:
            staffanY -=  ySpeed * dT
        if keys[K_DOWN]:
            staffanY +=  ySpeed * dT


        DISPLAYSURF.blit(annex4, (staffanX, staffanY))

        pygame.display.flip()

if __name__ == "__main__": main()
