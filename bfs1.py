                                  

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F','G'],
  'D' : ['H','I'],
  'E' : ['J','K'],
  'F' : ['L','M'],
  'G' : ['N','O'],
  'H' : ['I'],
  'I' : ['J'],
  'J' : ['K'],
  'K' : ['L'],
  'L' : ['M'],
  'M' : ['N'],
  'N' : ['O'],
  'O' : []
}

visited = []
queue = [] 

def bfs(visited, graph, node,dest):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s)

    if(s == dest):
          return

    for neighbour in graph[s]:
      if neighbour not in visited:
        
        visited.append(neighbour)
        queue.append(neighbour)


bfs(visited, graph, 'A','H')
