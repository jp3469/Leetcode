graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}    

visited = {}
queue = []

def bfs(visited, queue, graph, node):
    visited[node] = True
    queue.append(node)
    
    while queue:
        m = (queue.pop(0))
        print(m)

        for i in graph[m]:
            if i not in visited:
                visited[i] = True
                queue.append(i)
    
print(bfs(visited, queue, graph, '5'))