# Importing threading so we can run multiple parts of the program at the same time (multithreading)
import threading
# Importing time so we can pause the program for a bit (sleep) between operations
import time

# Define a class named Router. Each router will act like a device in a network that talks to other routers.
class Router:
    # The __init__ method initializes the router when it is created.
    # Each router needs an ID (name) and information about its neighbors (other routers it's connected to).
    def __init__(self, node_id, neighbors):
        self.node_id = node_id  # Give this router an ID (like 'A', 'B', etc.)
        self.neighbors = neighbors  # A dictionary of neighbors and the costs to reach them (how far/expensive the connection is)

        # Initialize the distance vector (which stores the shortest known path to each node).
        # At first, all distances are set to infinity (we don't know the actual distances yet).
        self.distance_vector = {node: float('inf') for node in self.neighbors}

        # The distance to itself is always 0, because there's no cost to reach itself.
        self.distance_vector[node_id] = 0

        # Initialize the routing table. This table will tell the router where to send a message 
        # to reach a specific destination.
        self.routing_table = {node: None for node in self.neighbors}
        self.routing_table[node_id] = node_id  # The router knows it can reach itself directly.

    # This method simulates the router sending its current distance vector to all its neighbors.
    def send_distance_vector(self):
        # Go through each neighbor and send them the router's distance information
        for neighbor in self.neighbors:
            # Only send updates to other routers, not to itself
            if neighbor.node_id != self.node_id:
                # Call the 'receive_update' method of the neighbor, simulating them receiving this router's info
                neighbor.receive_update(self.node_id, self.distance_vector)

    # This method receives an update from a neighbor router and updates its distance vector if necessary.
    def receive_update(self, from_node, distance_vector):
        updated = False  # A flag to check if we need to make any changes to our current data

        # Look through the information we received from another router
        for destination, cost in distance_vector.items():
            # Check if the distance to a destination is shorter using the new information
            if destination not in self.distance_vector or \
               self.distance_vector[destination] > self.neighbors[from_node] + cost:
                # If we found a shorter path, update our distance vector
                self.distance_vector[destination] = self.neighbors[from_node] + cost
                # Update the routing table to say we can reach the destination via the 'from_node' neighbor
                self.routing_table[destination] = from_node
                updated = True  # Mark that we updated the table

        # If the table was updated, we print the changes and send our new distance vector to all neighbors
        if updated:
            print(f"Router {self.node_id} updated its table based on information from {from_node}")
            self.send_distance_vector()  # Spread the new information to neighbors

    # This method keeps the router running. It will repeatedly send its distance vector to neighbors.
    def run(self):
        # Infinite loop to keep the router active
        while True:
            # Send the current distance vector to all neighbors
            self.send_distance_vector()
            # Pause for 10 seconds before sending again to avoid overwhelming the network
            time.sleep(10)

    # This method starts the router's activities in a separate thread (allowing it to work in the background)
    def start(self):
        # Create a new thread to run the 'run' method in the background
        thread = threading.Thread(target=self.run)
        # Start the thread so the router begins its work
        thread.start()

# This function sets up a small network of routers and starts them.
def simulate_network():
    # Creating four routers and specifying their neighbors and the costs to reach them
    # For example, router1 (A) can reach router2 (B) with a cost of 1 and router3 (C) with a cost of 4
    router1 = Router('A', {'B': 1, 'C': 4})
    router2 = Router('B', {'A': 1, 'C': 2, 'D': 5})
    router3 = Router('C', {'A': 4, 'B': 2})
    router4 = Router('D', {'B': 5})

    # Starting all the routers so they begin sending messages to each other
    router1.start()
    router2.start()
    router3.start()
    router4.start()

# This ensures that the network simulation starts only when this file is run directly
if __name__ == "__main__":
    simulate_network()  # Set up the network and start the simulation
