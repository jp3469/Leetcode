'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

1. Describe the question
find the biggest island on the grid
2. What are the constraints
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
3. What are some examples given, and can you solve it by hand?
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
4. Any other insights you find
'''

def maxAreaOfIsland1(grid):
    biggest_island = 0
    visited = {}

    def dfs(i,j, island):
        if i>0 and grid[i-1][j] == 1 and (i-1,j) not in visited:
            visited[(i-1,j)] = True
            island += 1
            island = dfs(i-1, j, island)
        if i+1 < len(grid) and grid[i+1][j] == 1 and (i+1,j) not in visited:
            visited[(i+1,j)] = True
            island += 1
            island = dfs(i+1, j, island)
        if j>0 and grid[i][j-1] == 1 and (i,j-1) not in visited:
            visited[(i,j-1)] = True
            island += 1
            island = dfs(i, j-1, island)
        if j+1 < len(grid[i]) and grid[i][j+1] == 1 and (i,j+1) not in visited:
            visited[(i,j+1)] = True
            island += 1
            island = dfs(i, j+1, island)
        return island

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if (i,j) not in visited and val == 1:
                island = 1
                visited[(i,j)] = True
                island = dfs(i,j, island)

                biggest_island = max(biggest_island, island)
    

    return biggest_island

input1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
output1 = 6
input2 = [[0,0,0,0,0,0,0,0]]
output2 = 0

print(maxAreaOfIsland1(input1))
print(maxAreaOfIsland1(input1) == output1)
print(maxAreaOfIsland1(input2) == output2)

def maxAreaOfIsland2(grid):
    biggest_island = 0
    visited = {}
    queue = []

    def bfs(i,j, island):
        while queue:
            i,j = queue.pop(0)
            if i>0 and grid[i-1][j] == 1 and (i-1,j) not in visited:
                visited[(i-1,j)] = True
                island += 1
                queue.append((i-1, j))
            if i+1 < len(grid) and grid[i+1][j] == 1 and (i+1,j) not in visited:
                visited[(i+1,j)] = True
                island += 1
                queue.append((i+1, j))
            if j>0 and grid[i][j-1] == 1 and (i,j-1) not in visited:
                visited[(i,j-1)] = True
                island += 1
                queue.append((i, j-1))
            if j+1 < len(grid[i]) and grid[i][j+1] == 1 and (i,j+1) not in visited:
                visited[(i,j+1)] = True
                island += 1
                queue.append((i, j+1))
            
        return island

    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if (i,j) not in visited and val == 1:
                island = 1
                visited[(i,j)] = True
                queue.append((i,j))
                island = bfs(i,j, island)

                biggest_island = max(biggest_island, island)
    
    return biggest_island

print(maxAreaOfIsland2(input1))
print(maxAreaOfIsland2(input1) == output1)
print(maxAreaOfIsland2(input2) == output2)