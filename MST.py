class Edge:
    """
    Class representing an edge in the graph. Each edge connects two vertices with a weight.
    """
    def __init__(self, u, v, weight):
        self.u = u  # First vertex of the edge
        self.v = v  # Second vertex of the edge
        self.weight = weight  # Weight of the edge


class Graph:
    """
    Graph class to represent an undirected weighted graph.
    """

    def __init__(self, vertices):
        """
        Initialize the graph with the given number of vertices and an empty edge list.
        """
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        """
        Add an edge to the graph. Each edge is represented by its two vertices and weight.
        """
        self.edges.append(Edge(u, v, weight))

    def print_graph(self):
        """
        Print a visual representation of the graph with vertices and edges.
        """
        print("Graph Representation:")
        for edge in self.edges:
            print(f"Vertex {edge.u} --({edge.weight})-- Vertex {edge.v}")

    def kruskal_mst(self):
        """
        Kruskal's algorithm to compute the Minimum Spanning Tree (MST).
        Returns the list of edges in the MST and the total weight of the MST.
        """
        # Sort all edges by increasing weight
        self.edges.sort(key=lambda edge: edge.weight)

        # Initialize disjoint set for the vertices
        disjoint_set = DisjointSet(self.vertices)

        mst_edges = []  # List to store the edges of the MST
        mst_weight = 0  # Total weight of the MST

        # Iterate over all sorted edges
        for edge in self.edges:
            # Find the roots of the sets of the two vertices of the edge
            u_root = disjoint_set.find(edge.u)
            v_root = disjoint_set.find(edge.v)

            # If u and v are in different sets, include this edge in the MST
            if u_root != v_root:
                mst_edges.append(edge)
                mst_weight += edge.weight
                # Union the two sets
                disjoint_set.union(u_root, v_root)

        return mst_edges, mst_weight


class DisjointSet:
    """
    Disjoint Set (Union-Find) class to manage subsets of vertices for Kruskal's Algorithm.
    This allows efficient union and find operations.
    """

    def __init__(self, n):
        # Initialize the parent list where each node is its own parent (self loop).
        # Initialize the rank to 0 for all vertices (used for union by rank).
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        """
        Find the representative of the set that u belongs to.
        Implements path compression to flatten the structure, improving efficiency.
        """
        if u != self.parent[u]:
            # Path compression: recursively find the root and update the parent of u to the root.
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        """
        Union two sets by rank. Attach the tree with lower rank under the tree with higher rank.
        """
        root_u = self.find(u)
        root_v = self.find(v)

        # Union by rank
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                # If ranks are equal, promote one and merge
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


if __name__ == "__main__":
    # Create a graph with 4 vertices
    g = Graph(4)
    
    # Add edges (u, v, weight)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    # Print the graph structure
    g.print_graph()

    # Compute the MST
    mst_edges, mst_weight = g.kruskal_mst()

    # Output the result
    print("\nEdges in the Minimum Spanning Tree:")
    for edge in mst_edges:
        print(f"Edge ({edge.u}, {edge.v}) with weight {edge.weight}")
    print(f"Total weight of MST: {mst_weight}")
