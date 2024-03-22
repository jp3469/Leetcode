'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

1. Describe the question
you are given a grid, an integer that signifies the row of the starting pixel, an integer that signifies the column of the starting pixel,
and an integer that the grid should be "filled" with. 
the starting square should be changed to the new pixel, then all squares adjacent to that square that have the same pixel as the starting square's original
pixel should also be changed to the new pixel, and it should continue for all pixels adjacent to the new pixel that was changed and so on.
2. What are the constraints
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
3. What are some examples given, and can you solve it by hand?
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
4. Any other insights you find
you can solve this question through DFS or BFS
if the starting pixel is equal to the new pixel, no changes are made to the image. 
DFS:
starting = image[sr][sc]
if starting == color:
    return image

def dfs(sr, sc):
    if image[sr][sc] == starting:
        image[sr][sc] = color 
        if sr >= 1:
            dfs(sr-1, sc)
        if sr + 1 < len(image):
            dfs(sr + 1, sc)
        if sc >= 1:
            dfs(sr, sc -1)
        if sc + 1 < len(image[sr]):
            dfs(sr, sc + 1)
dfs(sr, sc)
return image

BFS:
visited = {}
starting = image[sr][sc]

def bfs(sr, sc):
    q = []
    q.append((sr,sc))
    visited.add((sr,sc))
    image[sr][sc] = color

    while q:
        sr, sc = q.pop(0)
        if sr >= 1 and image[sr - 1][sc] == starting and (sr-1, sc) not in visited:
            q.append((sr-1, sc))
            visited.add((sr-1, sc))
            image[sr-1][sc] = color

        if sr + 1 < len(image) and image[sr+1][sc] == starting and (sr+1, sc) not in visited:
            q.append((sr+1, sc))
            visited.add((sr+1, sc))
            image[sr+1][sc] = color
        
        if sc >= 1 and image[sr][sc-1] == starting and (sr, sc-1) not in visited:
            q.append((sr, sc-1))
            visited.add((sr, sc-1))
            image[sr][sc-1] = color
        
        if sc + 1 <len(image[sr]) and image[sr][sc+1] == starting and (sr, sc+1) not in visited:
            q.append((sr, sc+1))
            visited.add((sr, sc+1))
            image[sr][sc+1] = color
        
bfs(sr, sc)
return(image)

'''

def floodFill1(image, sr, sc, color):
    starting = image[sr][sc]
    if image[sr][sc] == color:
        return image
    def dfs(r, c):
        if image[r][c] == starting:
            image[r][c] = color
            if r > 0:
                dfs(r-1, c)
            if r+1 < len(image):
                dfs(r+1, c)
            if c > 0:
                dfs(r, c-1)
            if c+1 < len(image[r]):
                dfs(r, c+1)
    dfs(sr, sc)
    return image

image1 = [[1,1,1],[1,1,0],[1,0,1]] 
sr1 = 1 
sc1 = 1 
color1 = 2
output1 = [[2,2,2],[2,2,0],[2,0,1]]

image2 = [[0,0,0],[0,0,0]]
sr2 = 0 
sc2 = 0 
color2 = 0
output2 = [[0,0,0],[0,0,0]]

print(floodFill1(image1, sr1, sc1, color1) == output1)
print(floodFill1(image2, sr2, sc2, color2) == output2)

def floodFill2(image, sr, sc, color):
    if image[sr][sc] == color:
        return image
            
    visited = {}
    starting = image[sr][sc]
    queue = []

    def bfs(r,c):
        queue.append((r,c))
        visited[(r,c)] = True
        while queue:
            r,c = queue.pop(0)
            image[r][c] = color
            if r>0 and image[r-1][c] == starting and (r-1,c) not in visited:
                visited[(r-1, c)] = True
                queue.append((r-1, c))
            if r+1 < len(image) and image[r+1][c] == starting and (r+1, c) not in visited:
                visited[(r+1, c)] = True
                queue.append((r+1, c))
            if c>0 and image[r][c-1] == starting and (r,c-1) not in visited:
                visited[(r, c-1)] = True
                queue.append((r, c-1))
            if c+1 < len(image) and image[r][c+1] == starting and (r, c+1) not in visited:
                visited[(r, c+1)] = True
                queue.append((r, c+1))
        
    bfs(sr,sc)
    return image

image1 = [[1,1,1],[1,1,0],[1,0,1]] 
print(floodFill2(image1, sr1, sc1, color1) == output1)
print(floodFill2(image2, sr2, sc2, color2) == output2)
