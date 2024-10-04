#Question 1
# Dijkstra's Algorithm Example Implementation
# We are using a simple graph with four nodes (A, B, C, D) and positive edge costs
# The graph is represented as G = (N, E), where:
# N is the set of nodes {A, B, C, D}
# E is the set of edges with costs: {(A, B, 2), (A, C, 6), (B, C, 3), (B, D, 1), (C, D, 1)}

# Dijkstra's algorithm is used to find the shortest paths from a starting node (node A in this example) 
# to all other nodes in a graph with positive edge weights.

# Step 1: Initialization
# We initialize the distances from the start node (A) to all other nodes as infinity, except for the start node itself which is 0.
# Predecessors for each node are initially set to None, except the start node which has no predecessor.

# Nodes and their initial distances and predecessors
distances = {'A': 0, 'B': float('inf'), 'C': float('inf'), 'D': float('inf')}
predecessors = {'A': None, 'B': None, 'C': None, 'D': None}

# The neighbors of each node with the associated edge costs
graph = {
    'A': {'B': 2, 'C': 6},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 6, 'B': 3, 'D': 1},
    'D': {'B': 1, 'C': 1}
}

# Set of unvisited nodes
unvisited = set(['A', 'B', 'C', 'D'])

# Step 2: Algorithm Execution
# We process each node, starting from the initial node (A)
current_node = 'A'

while unvisited:
    # Find the node with the smallest distance
    current_node = min((node for node in unvisited if distances[node] != float('inf')), key=lambda node: distances[node])
    
    # Update the distances for the neighbors of the current node
    for neighbor, cost in graph[current_node].items():
        if neighbor in unvisited:  # Only consider unvisited neighbors
            new_distance = distances[current_node] + cost
            if new_distance < distances[neighbor]:  # Check if a shorter path is found
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_node  # Update the path to reflect the shorter path

    # Remove the current node from the set of unvisited nodes
    unvisited.remove(current_node)

# Step 3: Output the results
# After processing all nodes, print the shortest distances and the paths to each node
for node in distances:
    print(f"Shortest distance to {node} is {distances[node]} with path involving {predecessors[node]}")


#Question 2 - bidirectional search
def bidirectional_dijkstra(graph, source, target):
    # Initialization for forward search
    fwd_distances = {node: float('inf') for node in graph}
    fwd_distances[source] = 0
    fwd_predecessors = {node: None for node in graph}
    fwd_visited = set()

    # Initialization for backward search
    bwd_distances = {node: float('inf') for node in graph}
    bwd_distances[target] = 0
    bwd_predecessors = {node: None for node in graph}
    bwd_visited = set()

    # Priority queues for nodes to be processed next
    fwd_queue = {source: 0}
    bwd_queue = {target: 0}

    # Helper function to relax edges
    def relax(node, neighbor, queue, distances, predecessors, other_distances):
        if neighbor in graph[node]:
            new_distance = distances[node] + graph[node][neighbor]
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = node
                queue[neighbor] = new_distance
                # Termination condition: check if the node is processed in both directions
                if neighbor in other_distances:
                    return True
        return False

    # Search loop
    while fwd_queue and bwd_queue:
        # Forward step
        fwd_current = min(fwd_queue, key=fwd_queue.get)
        fwd_queue.pop(fwd_current)
        fwd_visited.add(fwd_current)

        # Check all neighbors for a relaxation and termination possibility
        for neighbor in graph[fwd_current]:
            if relax(fwd_current, neighbor, fwd_queue, fwd_distances, fwd_predecessors, bwd_distances):
                return trace_path(fwd_predecessors, bwd_predecessors, neighbor)

        # Backward step
        bwd_current = min(bwd_queue, key=bwd_queue.get)
        bwd_queue.pop(bwd_current)
        bwd_visited.add(bwd_current)

        # Check all neighbors for a relaxation and termination possibility
        for neighbor in graph[bwd_current]:
            if relax(bwd_current, neighbor, bwd_queue, bwd_distances, bwd_predecessors, fwd_distances):
                return trace_path(fwd_predecessors, bwd_predecessors, neighbor)

    return None  # if no path found

# Function to trace back the path from the meeting point
def trace_path(fwd_predecessors, bwd_predecessors, meet):
    # Trace forward path
    path = []
    step = meet
    while step is not None:
        path.append(step)
        step = fwd_predecessors[step]
    path.reverse()

    # Trace backward path
    step = bwd_predecessors[meet]
    while step is not None:
        path.append(step)
        step = bwd_predecessors[step]

    return path

# Example usage
graph = {
    'A': {'B': 2, 'C': 6},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 6, 'B': 3, 'D': 1},
    'D': {'B': 1, 'C': 1}
}
source = 'A'
target = 'D'
print("Shortest path from A to D using bi-directional Dijkstra:")
print(bidirectional_dijkstra(graph, source, target))

