import math

class Character:

    ID = None
    name = None
    posX = None
    posY = None
    speed = [0.5, 0]
    row = None
    col = None

    def __init__(self, idNumber, cellPosition, worldPosition):
        self.ID = idNumber

        self.row = cellPosition[0]
        self.col = cellPosition[1]

        self.posX = worldPosition[0]
        self.posY = worldPosition[1]

        if (idNumber == 0):
            self.name = "pacman"
        else:
            self.name = "ghost0" + str(self.ID)

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

    def Update(self, maze):
        
        candidateX = self.posX + self.speed[0]
        candidateY = self.posY + self.speed[1]

        cellPositions = self.GetCellIndexForPosition(maze, candidateX, candidateY)

        rowCandidate = cellPositions[0]
        colCandidate = cellPositions[1]

        botRightX = candidateX + 15
        botRightY = candidateY + 15
        botRightCells = self.GetCellIndexForPosition(maze, botRightX, botRightY)
        botRightRow = botRightCells[0]
        botRightCol = botRightCells[1]

        candidateCollision = (maze[rowCandidate][colCandidate] != '0')
        botRightCollision = (maze[botRightRow][botRightCol] != '0')

        if (candidateCollision == True or botRightCollision == True):
            self.speed[0] *= -1
            self.speed[1] *= -1

        self.posX = candidateX
        self.posY = candidateY

        self.row = rowCandidate
        self.col = colCandidate


