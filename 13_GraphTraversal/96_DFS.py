print("\n.........................Depth First Search.........................\n")

import numpy as np
class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
        self._visited = [0] * self._vertices

    def insert_edge(self, u, v, cost = 1):
        self._adjMat[u][v] = cost
    
    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0
    
    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0
    
    def vertex_count(self):
        return self._vertices
    
    def edge_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count += 1
        return count
    
    def vertices(self):
        for i in range(self._vertices):
            print(i, end=" ")
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i,"--",j)
    

    def outdegree(self, vertex):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[vertex][i] != 0:
                count += 1
        return count
    

    def indegree(self, vertex):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][vertex] != 0:
                count += 1
        return count
    
    def display(self):
        print(self._adjMat)

    def DFS(self, startVertex):
        self._visited = [0] * self._vertices
        self.DFS_util(startVertex)
        print()

    def DFS_util(self, startVertex):
        print(startVertex, end=" ")
        self._visited[startVertex] = 1
        for i in range(self._vertices):
            if self._adjMat[startVertex][i] != 0 and self._visited[i] == 0:
                self.DFS_util(i)

    




G = Graph(7)
G.insert_edge(0, 1)
G.insert_edge(0, 5)
G.insert_edge(0, 6)
G.insert_edge(1, 0)
G.insert_edge(1, 2)
G.insert_edge(1, 5)
G.insert_edge(1, 6)
G.insert_edge(2, 3)
G.insert_edge(2, 4)
G.insert_edge(2, 6)
G.insert_edge(3, 4)
G.insert_edge(4, 2)
G.insert_edge(4, 5)
G.insert_edge(5, 2)
G.insert_edge(5, 3)
G.insert_edge(6, 3)
print("Grpah is:")
G.display()
print("\nDFS - traversal starting from vertex-0")
G.DFS(0)
print("\nDFS - traversal starting from vertex-1")
G.DFS(1)