class Node:
    ParentNode = None
    Cell = None
    CostF = 0
    CostG = 0
    CostH = 0

    def __init__(self, cell):
        self.Cell = cell

def IsPositionValid(row, col, maze):

    # Check bounds
    if (row < 0) or (row >= maze.shape[0]) or (col < 0) or (col >= maze.shape[1]):
        return False

    # Check if it is pathable
    return (maze[row][col] == '0')

def GetSqrDistance(fromCell, toCell):

    deltaX = fromCell[0] - toCell[0]
    deltaY = fromCell[1] - toCell[1]

    sqrDistance = (deltaX * deltaX) + (deltaY * deltaY)
    return sqrDistance

# Code based on https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
def GetPath(startCell, endCell, maze):
    
    startNode = Node(startCell)
    endNode = Node(endCell)

    openNodes = []
    openNodes.append(startNode)

    closedCells = []

    while len(openNodes) > 0:

        currentNode = openNodes[0]
        currentIndex = 0

        for index, item in enumerate(openNodes):
            if item.CostF < currentNode.CostF:
                currentNode = item
                currentIndex = index

        openNodes.pop(currentIndex)
        closedCells.append(currentNode.Cell)

        if (currentNode.Cell == endNode.Cell):
            path = []
            nextNode = currentNode
            while nextNode is not None:
                path.append(nextNode.Cell)
                nextNode = nextNode.ParentNode
            return path[::-1] # Return reversed path
        
        childrenNodes = []

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # Down, Up, Left, Right
        for newDirection in directions:
            candidateRow = currentNode.Cell[0] + newDirection[0]
            candidateCol = currentNode.Cell[1] + newDirection[1]

            if IsPositionValid(candidateRow, candidateCol, maze) == True:
                newCell = [candidateRow, candidateCol]
                newNode = Node(newCell)
                newNode.ParentNode = currentNode
                childrenNodes.append(newNode)

        for childNode in childrenNodes:
            
            for closedCell in closedCells:
                if (childNode.Cell == closedCell):
                    continue # Go to the next childNode. It is continuing the outter loop

            childNode.CostG = currentNode.CostG + 1
            childNode.CostH = GetSqrDistance(childNode.Cell, endNode.Cell)
            childNode.CostF = childNode.CostG + childNode.CostH

            for openNode in openNodes:
                if (childNode.Cell == openNode.Cell) and (childNode.CostG > openNode.CostG):
                    continue # Skip this child node

            openNodes.append(childNode)


    print("Failed to find a path!")
    return None