import random
import os.path
import pygame

print("Test git")

# Constants
main_dir = os.path.split(os.path.abspath(__file__))[0]

def loadImage(imgName):
    print("Loading images")
    imgName = os.path.join(main_dir, 'assets', imgName)
    try:
        surface = pygame.image.load(imgName)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(imgName, pygame.get_error()))
    return surface.convert()


mazeBG = load_image('maze.png')