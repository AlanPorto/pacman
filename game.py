import pygame
import simulation
import presentation
import sys
from numpy import loadtxt

def InitGame():

    # Initialize pygame
    pygame.init()

    maze = loadtxt('assets\\maze.txt', dtype=str)
    cellWidth = 16
    cellHeight = 16

    simulation.Init(maze, cellWidth, cellHeight)
    presentation.Init(maze, cellWidth, cellHeight)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        simState = simulation.Update()
        presentation.Update(simState)

InitGame()