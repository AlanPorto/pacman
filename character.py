class Character:

    ID = None
    name = None
    posX = None
    posY = None
    speed = [1, 0]
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
    
    def Update(self, maze):
        
        self.posX += self.speed[0]
        self.posY += self.speed[1]



