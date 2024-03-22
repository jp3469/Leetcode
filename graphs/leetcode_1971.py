'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

1. Describe the question
determine if a path exists. the input is a 2d array that lists all the edges in a graph. the graph is bi-directional, meaning each edge can go either way
2. What are the constraints
1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
3. What are some examples given, and can you solve it by hand?
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
4. Any other insights you find
make an adjacency list with the given edges, and then do bfs or dfs to find a path
'''

def validPath1(n, edges, source, destination):
    #making the adjacency list
    adj_list = {}
    for i in range(n):
        adj_list[i] = []
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    visited = {}
    def dfs(curr):
        visited[curr] = True
        if curr == destination:
            return True
        for i in adj_list[curr]:
            if i not in visited:
                if dfs(i):
                    return True
        return False
    
    queue = []
    def bfs(curr):
        visited[curr] = True
        queue.append(curr)

        while queue:
            i = queue.pop(0)
            if i == destination:
                return True
            for j in adj_list[i]:
                if j not in visited:
                    visited[j] = True
                    queue.append(j)
        return False
    
    return bfs(source)

n1 = 3
edges1 = [[0,1],[1,2],[2,0]]
source1 = 0
destination1 = 2
output1 = True

n2 = 6
edges2 = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source2 = 0
destination2= 5
output2 = False

print(validPath1(n1, edges1, source1, destination1) == output1)
print(validPath1(n2, edges2, source2, destination2) == output2)