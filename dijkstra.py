class Graph:
    def __init__(self, vertices):
        # Number of vertices
        self.V = vertices
        # Create a 2D array for the adjacency matrix
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def add_edge(self, u, v, w):
        # Function to add an edge from vertex u to vertex v with weight w
        self.graph[u][v] = w
        self.graph[v][u] = w  # Assuming undirected graph

    def print_solution(self, dist):
        # Utility function to print the constructed distance array
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(f"Vertex {node}: {dist[node]}")

    def min_distance(self, dist, visited):
        # Utility function to find the vertex with minimum distance
        # from the set of vertices not yet processed
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_val and not visited[v]:
                min_val = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        # The main function that calculates the minimum distance from the source to all other vertices
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not yet processed
            u = self.min_distance(dist, visited)

            # Put the minimum distance vertex in the processed set
            visited[u] = True

            # Update dist value of the adjacent vertices of the picked vertex only if the current
            # distance is greater than the new distance and the vertex is not in visited
            for v in range(self.V):
                if self.graph[u][v] > 0 and not visited[v] and \
                   dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

# Example usage
g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, 1)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 9)
g.add_edge(1, 3, 2)

g.dijkstra(0)
