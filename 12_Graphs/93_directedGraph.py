print("\n.........................Directed Graph - Adjacency Matrix Representaion.........................\n")

from graphs import Graph

G = Graph(4)

print("Before Inserting edges::::")
print("Adjacency Matrix:")
G.display()
print("Total Vertices:", G.vertex_count())
print("Total Edges:", G.edges_count())

G.insert_edge(0, 1) # by default cost is 1
G.insert_edge(0, 2)
G.insert_edge(1, 2)
G.insert_edge(2, 3)

print("\nAfter Inserting edges::::")
print("Adjacency Matrix:")
G.display()

print("\nEdges:")
G.edges()

print("\nVertices:")
G.vertices()

print("\nTotal Vertices:", G.vertex_count())
print("Total Edges:", G.edges_count()) 

print("\nOutdegree of 2:", G.outdegree(2)) 
print("Indegree of 2:", G.indegree(2))
print("Indegree of 0:", G.indegree(0))

print("\nExist Edge 1--2:", G.exist_edge(1, 2))
G.remove_edge(1, 2) 
print("\nAfter removing, Exist Edge 1--2:", G.exist_edge(1, 2))
