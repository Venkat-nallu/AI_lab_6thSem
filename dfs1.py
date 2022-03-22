                                                       
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

visited = set()

def dfs(visited, graph, node,dest):
    if node not in visited:
        print (node)
        visited.add(node)
        if(node == dest):
            return True
        for neighbour in graph[node]:
            if(dfs(visited, graph, neighbour,dest) == True):
                return True

dfs(visited, graph, 'A','G')
