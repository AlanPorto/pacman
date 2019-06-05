import random
import os.path
import pygame
from pygame.locals import *

# Constants
main_dir = os.path.split(os.path.abspath(__file__))[0]

def loadImage(imgName):
    print("Loading image")
    imgName = os.path.join(main_dir, 'assets', imgName)
    try:
        surface = pygame.image.load(imgName)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(imgName, pygame.get_error()))
    return surface.convert_alpha()


# Initialize pygame
pygame.init()

size = width, height = 448, 576 #448, 576
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

maze = loadImage("map.png")
mazeRect = maze.get_rect()

ball = loadImage("intro_ball.gif") #pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen.fill(black)
screen.blit(maze, mazeRect)
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #ballrect = ballrect.move(speed)
    #if ballrect.left < 0 or ballrect.right > width:
        #speed[0] = -speed[0]
    #if ballrect.top < 0 or ballrect.bottom > height:
        #speed[1] = -speed[1]

    #screen.fill(black)
    #screen.blit(maze, mazeRect)
    #pygame.display.flip()