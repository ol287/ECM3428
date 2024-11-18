import heapq
import math

# Node Class: Represents a tree node with character, frequency, and pointers to left and right children.
class Node:
    def __init__(self, char=None, freq=0):
        """
        Initializes a Node object.

        Parameters:
        char (str): The character represented by the node (None for internal nodes).
        freq (float): The frequency or weight associated with the node.
        """
        self.char = char  # The character (for leaf nodes, None for internal nodes)
        self.freq = freq  # The frequency of the character
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

    def __lt__(self, other):
        """
        Comparator function for Node objects, required for priority queue (heap).
        Compares nodes based on their frequency.
        """
        return self.freq < other.freq


# Priority Queue (Heap): Used to always extract the two nodes with the smallest frequencies efficiently.
def huffman_tree(characters):
    """
    Constructs the Huffman Tree for a given set of characters and their frequencies.

    Parameters:
    characters (list of tuples): A list where each tuple is (char, freq).

    Returns:
    Node: The root of the Huffman Tree.
    """
    # Step 1: Create a priority queue (min-heap) of nodes from the character-frequency pairs
    heap = [Node(char, freq) for char, freq in characters]
    heapq.heapify(heap)  # Converts the list into a heap (min-priority queue)

    # Step 2: While there is more than one node in the heap
    while len(heap) > 1:
        # Step 3: Extract the two nodes with the smallest frequencies
        x = heapq.heappop(heap)  # Node with smallest frequency
        y = heapq.heappop(heap)  # Node with second smallest frequency

        # Step 4: Create a new node z with the combined frequency
        z = Node(freq=x.freq + y.freq)  # New internal node with combined frequency
        z.left = x  # Left child points to the smaller frequency node
        z.right = y  # Right child points to the larger frequency node

        # Step 5: Insert the new node back into the heap
        heapq.heappush(heap, z)

    # Step 6: Return the root of the Huffman Tree
    return heap[0]  # The last remaining node is the root of the tree


# Tree Traversal: Optional function to display the Huffman codes for each character.
def print_tree(node, prefix=""):
    """
    Recursively traverses the Huffman Tree and prints the Huffman codes for each character.

    Parameters:
    node (Node): The current node in the Huffman Tree.
    prefix (str): The binary code prefix generated so far.
    """
    if node:
        # If the node is a leaf (contains a character), print its code
        if node.char:
            print(f"{node.char}: {prefix}")
        # Recursively traverse the left and right subtrees with updated prefixes
        print_tree(node.left, prefix + "0")
        print_tree(node.right, prefix + "1")


# Entropy Calculation: Function to compute the entropy of the symbols
def calculate_entropy(characters):
    """
    Calculates the entropy of the given set of characters and their frequencies.

    Parameters:
    characters (list of tuples): A list where each tuple is (char, freq).

    Returns:
    float: The entropy of the symbols in bits/symbol.
    """
    entropy = 0
    for _, freq in characters:
        if freq > 0:  # Avoid log(0) issues
            entropy += freq * math.log2(1 / freq)  # or equivalently -freq * log2(freq)
    return entropy


# Example usage
if __name__ == "__main__":
    # Input characters and their frequencies
    characters = [('A', 0.16), ('B', 0.51), ('C', 0.09), ('D', 0.13), ('E', 0.11)]

    # Huffman Tree Construction: Follows the algorithm described above
    root = huffman_tree(characters)

    # Print the Huffman codes for each character
    print("Huffman Codes:")
    print_tree(root)

    # Calculate and print the entropy of the symbols
    entropy = calculate_entropy(characters)
    print(f"\nEntropy of the symbols: {entropy:.4f} bits/symbol")
