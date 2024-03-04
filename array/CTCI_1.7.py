'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0. 

1. Describe the question
If an element in a matrix is 0, its entire row and column are set to 0
2. What are the constraints
3. What are some examples given, and can you solve it by hand?
[[1,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,3,3]]
[[0,0,0,0,0],
 [1,0,1,1,1],
 [3,0,3,3,3]]
4. Any other insights you find
My initial approach was to just go through and find any elements where the value is 0, and set the entire row and column to 0, but I realized that this would make
the rows/columns for values that weren't originally 0 but got turned into 0 to also turn into 0. We would need to somehow find all the places where the value is 0
and then go about turning the rows and columns into 0 so there isn't any error in the algorithm

create array for rows that cotain a 0
create array for columns that contain a 0
for i, row in board:
    for j, val in row:
        if val == 0:
            m.append(i)
            n.append(j)

for i, row in board:
    for j, val in board:
        if i in m or j in n:
            board[i][j] = 0

return board

'''

def turnzero1(board):
    m = []
    n = []
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                m.append(i)
                n.append(j)

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if i in m or j in n:
                board[i][j]= 0

    return board    

board1 = [[1,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,3,3]]

board2 = [[0,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,3,3]]

board3 = [[0,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,0,3],
 [4,4,4,4,4]]


print(turnzero1(board1))
print(turnzero1(board2))
print(turnzero1(board3))

'''runtime of this code is O(N^2) since you are looping through the matrix 2x and creating two arrays and looking through them for every element.
    the space complexity is O(N) since you have to create two arrays that potentially could have as many elements as the number of elements in the matrix. 
    We could optimize runtime by making the arrays boolean arrays, that way we don't have to look through the array to see if an element exists, and since
    if any element in a row or column is 0, the entire row or column will be 0, we don't actually need to mark down exactly where the 0 is.
    '''

def turnzero2(board):
    m = [False for i in range(len(board))]
    n = [False for i in range(len(board[1]))]
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                m[i] = True
                n[j] = True

    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if m[i] or n[j]:
                board[i][j]= 0

    return board    

board4 = [[1,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,3,3]]

board5 = [[0,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,3,3]]

board6 = [[0,0,2,3,4],
 [1,1,1,1,1],
 [3,3,3,0,3],
 [4,4,4,4,4]]
print(turnzero2(board4))
print(turnzero2(board5))
print(turnzero2(board6))

'''runtime is now O(n) since all we have to do is go through the matrix 2x.
space complexity is the same at O(n) since we have to create 2 new arrays of length m and n. 
'''