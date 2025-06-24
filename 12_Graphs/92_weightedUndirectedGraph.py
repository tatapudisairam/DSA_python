print("\n.........................Weighted Undirected Graph - Adjacency Matrix Representaion.........................\n")

from graphs import Graph

G = Graph(4)

print("Before Inserting edges::::")
print("Adjacency Matrix:")
G.display()
print("Total Vertices:", G.vertex_count())
print("Total Edges:", G.edges_count())

G.insert_edge(0, 1, 26) # third parameter is cost
G.insert_edge(0, 2, 16)
G.insert_edge(1, 0, 26)
G.insert_edge(1, 2, 12)
G.insert_edge(2, 0, 16)
G.insert_edge(2, 1, 12)
G.insert_edge(2, 3, 8)
G.insert_edge(3, 2, 8)

print("\nAfter Inserting edges::::")
print("Adjacency Matrix:")
G.display()

print("\nEdges:")
G.edges()

print("\nVertices:")
G.vertices()

print("\nTotal Vertices:", G.vertex_count())
print("Total Edges:", G.edges_count()) #it will give 8 because it's a undirected graph, so to find exact number divide it by 2

print("\nOutdegree of 2:", G.outdegree(2)) # indegree and outdegree of a vertex is same in undirected graph
print("Indegree of 2:", G.indegree(2))
print("Indegree of 0:", G.indegree(0))

print("\nExist Edge 1--2:", G.exist_edge(1, 2))
G.remove_edge(1, 2) #since it's a undirected graph we need to remove at two places
G.remove_edge(2, 1)
print("\nAfter removing, Exist Edge 1--2:", G.exist_edge(1, 2))
