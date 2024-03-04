'''
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?

1. Describe the question
Rotate a matrix by 90 degrees
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16]]
[[13,9,5,1],
 [14,10,6,2],
 [15,11,7,3],
 [16,12,8,4]]
4. Any other insights you find
(0,0) => (0,N-1)
(0,1) => (1,N-1)
...
(0,N-1) => (N-1,N-1)

(1,0) => (0, N-2)
(1,1) => (1, N-2)
...
(1,N-1) => (N-1, N-2)

(N-1, 0) => (0,0)
...
(N-1, N-1) => (N-1, 0)

Easiest way would be to create a new board, iterate through each row and assign new position
create new board
for i in board:
    for j,val in enumerate(i):
        newboard[j, N-(i+1)] = val
return new board
'''

def rotate1(board):
    N = len(board)
    newboard = [[None for x in range(N)] for y in range(N)]
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            newboard[j][N-(i+1)] = val
    return newboard

board1 = [[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16]]

board2 = [[]]

print(rotate1(board1))
print(rotate1(board2))

'''runtime is O(N) since we are looping through the grid once.
Space complexity is O(N) since we are creating a new board to return. This can be optimized if I do the rotation in place instead of creating a whole new board. 
How can I rotate in place? Some kind of swapping algorithm. 
Swapping in layers since the layers do not change.

N = len(board)
numlayers = N//2 (if N is odd, the last layer will always be one number and does not change place)
for i in range(numlayers):
    for j in range(N-(i*2 + 1)):
        board[i][j+i], board[j+i][N-(i+1)], board[N-(i+1)][N-(j+i+1)], board[N-(j+i+1)][i] = board[N-(j+i+1)][i], board[i][j+i], board[j][N-(i+1)], board[N-(i+1)][N-(j+i+1)]
return board
'''

def rotate2(board):
    N = len(board)
    numlayers = N//2
    for i in range(numlayers):
        for j in range(N-(i*2 + 1)):
            board[i][j+i], board[j+i][N-(i+1)], board[N-(i+1)][N-(j+i+1)], board[N-(j+i+1)][i] = board[N-(j+i+1)][i], board[i][j+i], board[j+i][N-(i+1)], board[N-(i+1)][N-(j+i+1)]
    return board

print(rotate2(board1))
print(rotate2(board2))

board3 = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
print(rotate1(board3))
print(rotate2(board3))

'''runtime is O(N) since we are looping through the grid once
Space complexity ius now O(1) since we are swapping in place and not creating any new objects.
'''