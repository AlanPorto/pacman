import random
import os.path
import pygame
from pygame.locals import *

# Constants
main_dir = os.path.split(os.path.abspath(__file__))[0]
mWidth = 16
mHeight = 16

# Colors
mBlack = (0, 0, 0)
mWhite = (255, 255, 255)
mBlue = (0, 0, 255)

# Variables
mMaze = None
mScreenSize = None
mRows = None
mCols = None
mBackground = None
mScreen = None

def loadImage(imgName):
    print("Loading image")
    imgName = os.path.join(main_dir, 'assets', imgName)
    try:
        surface = pygame.image.load(imgName)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(imgName, pygame.get_error()))
    return surface.convert_alpha()

def Init(mazeArray):
    print("Init pres")

    global mMaze
    mMaze = mazeArray

    global mRows, mCols
    mRows, mCols = mMaze.shape

    global mScreenSize
    global mWidth, mHeight
    mScreenSize = (mWidth * mCols, mHeight * mRows)

    global mScreen
    mScreen = pygame.display.set_mode(mScreenSize, 0, 16)

    global mBackground
    mBackground = pygame.surface.Surface(mScreenSize).convert()
    mBackground.fill(mBlack)

def Update():

    global mScreen
    mScreen.blit(mBackground, (0,0))

    global mRows, mCols
    global mWidth, mHeight
    for col in range(mCols):
        for row in range(mRows):
            global mMaze
            value = mMaze[row][col]
            if value == '1':
                xPos = col * mWidth
                yPos = row * mHeight
                pygame.draw.rect(mScreen, mBlue, [xPos, yPos, mWidth, mHeight])

    pygame.display.update()

        