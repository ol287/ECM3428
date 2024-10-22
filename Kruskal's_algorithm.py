# Kruskal's algorithm in Python

# Class to represent a graph edge
class Edge:
    def __init__(self, u, v, weight):
        self.u = u  # starting vertex of the edge
        self.v = v  # ending vertex of the edge
        self.weight = weight  # weight of the edge

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # number of vertices in the graph
        self.edges = []  # list to store all edges

    # Function to add an edge to the graph
    def add_edge(self, u, v, weight):
        self.edges.append(Edge(u, v, weight))

    # Utility function to find the set of an element (using path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Utility function to union two sets (using union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of higher rank tree
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Kruskal's algorithm to find MST
    def kruskal(self):
        # This will store the final MST
        result = []

        # Step 1: Sort all edges in non-decreasing order of their weight
        self.edges = sorted(self.edges, key=lambda edge: edge.weight)

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges in MST will be V-1
        e = 0  # Initial number of edges in result
        i = 0  # Initial index of sorted edges

        # Step 2: Pick the smallest edge and check if it forms a cycle
        while e < self.V - 1:
            # Pick the smallest edge
            u, v, w = self.edges[i].u, self.edges[i].v, self.edges[i].weight
            i += 1

            # Find set of both u and v
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If including this edge doesn't cause a cycle, include it in result
            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        # Print the contents of the MST
        print("Edges in the constructed Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal()
