'''
You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

1. Describe the question
given a grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water, find the perimeter of the 'island' in the grid
2. What are the constraints
row = grid.length
col = grid[i].length
1<= row, col <= 100
grid[i][j] = 0 or 1
there is exactly one island in grid
the grid is surrounded by water
3. What are some examples given, and can you solve it by hand?
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Input: grid = [[1]]
Output: 4
Input: grid = [[1,0]]
Output: 4
4. Any other insights you find
make an adjacency list with all the land squares being vertices, and the amount of perimeter to add is 4-length of adjacent vertices.
no need to make an adjacency list, simply go through all the elements in the grid, and if the square is a land square, check if it has any neighboring squares
that are also land and subtract from 4.

total = 0
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == 1:
            add = 0
            if i == 0:
                add += 1
            elif grid[i - 1][j] == 0:
                add += 1
            if i == len(grid) - 1:
                add += 1
            elif grid[i + 1][j] == 0:
                add += 1
            if j == 0:
                add += 1
            elif grid[i][j-1] == 0:
                add += 1
            if j == len(row) - 1:
                add += 1
            elif grid[i][j+1] == 0:
                add += 1
            total += total
return total
'''
def islandPerimeter(grid):
    total = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                add = 0
                if i == 0:
                    add += 1
                elif grid[i - 1][j] == 0:
                    add += 1
                if i == len(grid) - 1:
                    add += 1
                elif grid[i + 1][j] == 0:
                    add += 1
                if j == 0:
                    add += 1
                elif grid[i][j-1] == 0:
                    add += 1
                if j == len(row) - 1:
                    add += 1
                elif grid[i][j+1] == 0:
                    add += 1
                total += add
    return total

input1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
output1 = 16
input2 = [[1]]
output2 = 4
input3 = [[1,0]]
output3 = 4
print(islandPerimeter(input1) == output1)
print(islandPerimeter(input2) == output2)
print(islandPerimeter(input3) == output3)

