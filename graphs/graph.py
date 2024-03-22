# a graph consists of nodes (or vertices) connected by edges
# n = number of nodes
# m = number of edges

# path: leads from one node to another node through the edges of a graph
#   length of a path: number of edges in the path
#   cycle: path where the first and last node is the same
#   connected: there is a path between any two nodes in a graph
#       components: connected parts of a graph

# tree: connected graph that does not contain cycles

# directed graph: edges can be traversed in one direction only
#   indegree: number of edges that end at the node
#   outdegree: number of edges that start at the node

# weighted graph: each edge is assigned a weight (often interpreted as edge lengths)
#   length of a weighted path: sum of its edge weights

# neighbors/adjacent: there is an edge between them

# degree: number of its neighbors

# sum of degrees is always 2m (2 * number of edges)
#   reason: each edge increases the degree of 2 nodes by 1

# regular graph: degree of every node is a constant d

# complete graph: degree of every node is n - 1 (contains all possible edges between the nodes)

# bipartite graph: possible to color its nodes using 2 colors so that no adjacent nodes have the same color
#   when a graph doesn't have a cycle with an odd number of edges it's always bipartite

# Depth-First Search (DFS)
class Node:
    def __init__(self, data):
        self.children = None:
        self.data = data

    # Insert Node
    def insert(self, data):
        

