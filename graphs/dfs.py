visited = {}

def dfs(node, graph, visited):
    if node not in visited:
        print(node)
        visited[node] = True
        for i in graph[node]:
            dfs(i, graph, visited)

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}    

print(dfs('5', graph, visited))