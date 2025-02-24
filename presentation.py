import random
import os.path
import pygame
from pygame.locals import *

# Constants
main_dir = os.path.split(os.path.abspath(__file__))[0]

# Characters
mPacmanID = 0
mcGhostID = 1

# Colors
mBlack = [0, 0, 0]
mWhite = [255, 255, 255]
mBlue = [0, 0, 255]
mYellow = [255, 255, 0]
mRed = [255, 0, 0]

# Variables
mWidth = None
mHeight = None
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

def Init(mazeArray, cellWidth, cellHeight):

    global mMaze
    mMaze = mazeArray

    global mRows, mCols
    mRows, mCols = mMaze.shape

    global mWidth, mHeight
    mWidth = cellWidth
    mHeight = cellHeight

    global mScreenSize
    mScreenSize = (mWidth * mCols, mHeight * mRows)

    global mScreen
    mScreen = pygame.display.set_mode(mScreenSize, 0, 16)

    global mBackground
    mBackground = pygame.surface.Surface(mScreenSize).convert()
    mBackground.fill(mBlack)

def GetColorForID(idNumber):
    if (idNumber == 0):
        return mYellow
    else:
        return mRed

def DrawnLevel():

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
    
def DrawnCharacters(simState):

    for i in range(len(simState)):
        char = simState[i]
        color = GetColorForID(char.ID)
        xPos = char.posX
        yPos = char.posY

        targetColor = mYellow
        targetX = char.targetX
        targetY = char.targetY

        global mScreen, mWidth, mHeight
        pygame.draw.rect(mScreen, color, [xPos, yPos, mWidth, mHeight])
        pygame.draw.rect(mScreen, targetColor, [targetX, targetY, mWidth, mHeight])


def Update(simState):
    DrawnLevel()
    DrawnCharacters(simState)
    pygame.display.update()

    

        