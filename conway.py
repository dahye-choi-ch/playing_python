# Conway's Game of Life
import random, time, copy
width = 10; height = 10;

# create a list of list for the cells:
nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append('#') # add a living cell
        else:
            column.append(' ') # add a dead cell
    nextCells.append(column)

while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)

    # Print currentCells am Bildschirm
    for y in range(height):
        for x in range(width):
            print( currentCells[x][y], end='')
        print()

    #calculate the next step's cells based on current step's cells:
    for x in range(width):
        for y in range(height):
            # get neighboring coordinates:
            # '% width' ensures leftCoor is always between 0 and width-1
            leftCoord = (x-1)%width
            rightCoord = (x+1)%width
            aboveCoord = (y-1)%height
            belowCoord = (y+1)%height

            # count number of living neighbors:
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord]=='#':
                numNeighbors += 1
            if currentCells[leftCoord][y]=='#':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord]=='#':
                numNeighbors += 1
            if currentCells[x][aboveCoord]=='#':
                numNeighbors += 1
            if currentCells[x][belowCoord]=='#':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord]=='#':
                numNeighbors += 1
            if currentCells[rightCoord][y]=='#':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord]=='#':
                numNeighbors += 1

            # set cell based on conway's game of life rules:
            if currentCells[x][y]== '#' and (numNeighbors==2 or numNeighbors==3):
                nextCells[x][y]='#'
            elif currentCells[x][y]==' ' and numNeighbors == 3:
                nextCells[x][y]='#'
            else: nextCells[x][y]=' '
    time.sleep(1)

