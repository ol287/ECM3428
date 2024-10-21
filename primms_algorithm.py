import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}  # dictionary of adjacency lists

    def add_edge(self, u, v, weight):
        # Since the graph is undirected, add both (u, v) and (v, u)
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    def prim_mst(self):
        # Array to track vertices included in MST
        in_mst = [False] * self.vertices
        # Min heap to pick the minimum weight edge at every step
        min_heap = []

        # Start with vertex 0
        # Push all edges from vertex 0 to the priority queue
        # (weight, start_vertex, end_vertex)
        for v, weight in self.graph[0]:
            heapq.heappush(min_heap, (weight, 0, v))

        # Include vertex 0 in MST
        in_mst[0] = True
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            # If vertex v is not in MST, it is the next vertex to add
            if not in_mst[v]:
                in_mst[v] = True  # Include vertex in MST
                mst_cost += weight  # Add cost of the edge to the MST total cost
                mst_edges.append((u, v, weight))  # Add edge to MST

                # Add all edges from vertex v to the heap
                for to, w in self.graph[v]:
                    if not in_mst[to]:
                        heapq.heappush(min_heap, (w, v, to))

        return mst_edges, mst_cost

# Example usage:
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    mst_edges, mst_cost = g.prim_mst()
    print("Edges in MST with their weights:")
    for u, v, weight in mst_edges:
        print(f"{u} - {v} with weight {weight}")
    print(f"Total cost of MST: {mst_cost}")
