# l=["Harsh","Om","Anand","Shashank","Sambit","Avinash"]
# i=0
# while(i<len(l)):
#     print(l[i])
#     i+=1

# l=["Harsh","Om","Anand","Shashank","Sambit","Avinash"]
# for i in range(4):
    
#     print(l)
#     i+=1
# else:
#     print("Done")

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  

    def bfs(self, start):
        visited = set()
        queue = deque([start]) 

        while queue:
            node = queue.popleft() 
            if node not in visited:
                print(node, end=' ') 
                visited.add(node)  
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("BFS Traversal starting from node 0:")
    g.bfs(0) 

