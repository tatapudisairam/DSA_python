# Graphs ADT - Adjacency Matrix Representaion
import numpy as np
class Graph:
    def __init__(self, vertices):
        self._vertices = vertices
        self._adjMat = np.zeros((vertices, vertices))
    
    def insert_edge(self, u, v, cost = 1): # by default 1 for unweighted graphs
        self._adjMat[u][v] = cost
    
    def remove_edge(self, u, v):
        self._adjMat[u][v] = 0
    
    def exist_edge(self, u, v):
        return self._adjMat[u][v] != 0
    
    def vertex_count(self):
        return self._vertices
    
    def edges_count(self):
        count = 0
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    count = count + 1
        return count

    def vertices(self):
        for i in range(self._vertices):
            print(i, end=" ")
        print()

    def edges(self):
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    print(i, "--", j)

    def get_edges(self):
        edge_list = []
        for i in range(self._vertices):
            for j in range(self._vertices):
                if self._adjMat[i][j] != 0:
                    edge_list.append((i, j, self._adjMat[i][j]))
        return edge_list


    def get_vertices(self):
        return list(range(self._vertices))

    def outdegree(self, vertex):
        count = 0
        for j in range(self._vertices):
            if self._adjMat[vertex][j] != 0:
                count = count + 1
        return count
    
    def indegree(self, vertex):
        count = 0
        for i in range(self._vertices):
            if self._adjMat[i][vertex] != 0:
                count += 1
        return count
    
    def display(self):
        print(self._adjMat)


