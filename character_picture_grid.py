def grid_printing(input_matrix):
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[0])):
            if j == len(input_matrix[0])-1: print(input_matrix[i][j])
            else: print(input_matrix[i][j],end='')


given_grid = [[0,0],[2,1],[4,0],[5,0],[5,1],[5,0],[4,0],[2,1],[0,0]]
grid=[]
for i in range(9):
    inner_grid = ['.']*6
    if given_grid[i][0] != 0:
        for j in range(given_grid[i][1], given_grid[i][1]+given_grid[i][0]):
            inner_grid[j] = 'O'
    grid.append(inner_grid)
#grid_printing(grid)

inversed_grid = []
for i in range(len(grid[0])):
    inversed_inner_grid = []
    for j in range(len(grid)):
        inversed_inner_grid.append( grid[j][i] )
    inversed_grid.append( inversed_inner_grid )
grid_printing(inversed_grid)


