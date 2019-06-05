import pygame
import simulation
import presentation
import sys
from numpy import loadtxt

def InitGame():

    # Initialize pygame
    pygame.init()

    maze = loadtxt('assets\\maze.txt', dtype=str)

    simulation.Init(maze)
    presentation.Init(maze)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        presentation.Update()

InitGame()