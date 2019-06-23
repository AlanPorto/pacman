import math
import random
import aStar

class Character:

    ID = None
    name = None
    posX = None
    posY = None
    speed = [0, 0]
    row = None
    col = None

    currentPath = []
    nextMoveCell = None

    targetRow = None
    targetCol = None
    targetX = None
    targetY = None

    def GetCellIndexForPosition(self, maze, posX, posY):

        oneOverCellWidth = 1 / 16
        oneOverCellHeight = 1 / 16

        rowIndex = posY * oneOverCellHeight
        colIndex = posX * oneOverCellWidth

        rowIndex = math.floor(rowIndex)
        colIndex = math.floor(colIndex)

        if (rowIndex == maze.shape[0]):
            rowIndex -= 1

        if (colIndex == maze.shape[1]):
            colIndex -= 1 

        return [rowIndex, colIndex]

    def GetPositionForIndex(self, row, col):

        cellWidth = 16
        cellHeight = 16

        posX = col * cellWidth
        posY = row * cellHeight

        return [posX, posY]

    def SetRndTarget(self, maze):

        maxRow = maze.shape[0] - 1
        maxCol = maze.shape[1] - 1

        self.targetRow = None
        self.targetCol = None

        while (True):
            self.targetRow = random.randint(0, maxRow)
            self.targetCol = random.randint(0, maxCol)

            if (maze[self.targetRow][self.targetCol] == '0'):
                worldPos = self.GetPositionForIndex(self.targetRow, self.targetCol)
                self.targetX = worldPos[0]
                self.targetY = worldPos[1]
                break

    def GenerateNewTarget(self, maze):
        self.SetRndTarget(maze)
        
        startCell = [self.row, self.col]
        endCell = [self.targetRow, self.targetCol]
        self.currentPath = aStar.GetPath(startCell, endCell, maze)
        self.nextMoveCell = None

    def __init__(self, idNumber, cellPosition, worldPosition, maze):
        self.ID = idNumber

        self.row = cellPosition[0]
        self.col = cellPosition[1]

        self.posX = worldPosition[0]
        self.posY = worldPosition[1]

        if (idNumber == 0):
            self.name = "pacman"
        else:
            self.name = "ghost0" + str(self.ID)

        self.GenerateNewTarget(maze)

    def UpdateNextMoveCell(self):

        if self.currentPath == None or len(self.currentPath) == 0:
            return

        currentCell = [self.row, self.col]

        if (self.nextMoveCell == None) or (currentCell == self.nextMoveCell):
            self.nextMoveCell = self.currentPath[0]
            self.currentPath.pop(0)

        self.UpdateMoveDirection(currentCell)

    def UpdateMoveDirection(self, currentCell):

        speedX = 0
        speedY = 0

        if (self.nextMoveCell[0] < currentCell[0]): # Go up
            speedY = -0.2
        elif (self.nextMoveCell[0] > currentCell[0]): # Go down
            speedY = 0.2
        elif (self.nextMoveCell[1] < currentCell[1]): # Go left
            speedX = -0.2
        elif (self.nextMoveCell[0] > currentCell[0]): # Go right
            speedX = 0.2

        self.speed = [speedX, speedY]

    def Update(self, maze):
        
        self.UpdateNextMoveCell()
        
        candidateX = self.posX + self.speed[0]
        candidateY = self.posY + self.speed[1]

        cellPositions = self.GetCellIndexForPosition(maze, candidateX, candidateY)

        rowCandidate = cellPositions[0]
        colCandidate = cellPositions[1]

        # Collision code
        #botRightX = candidateX + 15
        #botRightY = candidateY + 15
        #botRightCells = self.GetCellIndexForPosition(maze, botRightX, botRightY)
        #botRightRow = botRightCells[0]
        #botRightCol = botRightCells[1]

        #candidateCollision = (maze[rowCandidate][colCandidate] != '0')
        #botRightCollision = (maze[botRightRow][botRightCol] != '0')

        #if (candidateCollision == True or botRightCollision == True):
            #self.speed[0] *= -1
            #self.speed[1] *= -1

        self.posX = candidateX
        self.posY = candidateY

        self.row = rowCandidate
        self.col = colCandidate

        if (self.row == self.targetRow and self.col == self.targetCol):
            print("Arrived")
            self.GenerateNewTarget(maze)


