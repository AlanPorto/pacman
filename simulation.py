import character

mMaze = None

mCharacters = []

mWidth = None
mHeight = None

def Init(mazeArray, cellWidth, cellHeight):

    global mMaze
    mMaze = mazeArray

    global mWidth, mHeight
    mWidth = cellWidth
    mHeight = cellHeight

    cellPosition = [1, 1]
    posX = cellPosition[1] * mWidth
    posY = cellPosition[0] * mHeight

    worldPosition = [posX, posY]

    for i in range(1):
        char = character.Character(i, cellPosition, worldPosition)
        global mCharacters
        mCharacters.append(char)


def Update():

    simState = []

    global mMaze
    global mCharacters
    for i in range(len(mCharacters)):
        char = mCharacters[i]
        char.Update(mMaze)
        simState.append(char)

    return simState