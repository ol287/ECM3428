import numpy as np

def pagerank(links, d=0.85, tol=1e-6, max_iter=100):
    """
    Computes the PageRank of each page using the transition matrix approach.

    Args:
        links: Adjacency matrix where links[i][j] is 1 if there's a link from page i to page j, else 0.
        d: Damping factor (default 0.85).
        tol: Convergence tolerance (default 1e-6).
        max_iter: Maximum number of iterations (default 100).

    Returns:
        A numpy array containing the PageRank of each page.
    """
    
    # Number of pages
    N = links.shape[0]
    
    # Create the transition matrix (stochastic matrix)
    transition_matrix = np.zeros_like(links, dtype=float)
    
    for i in range(N):
        # If a row has no outgoing links, it's a sink, distribute rank equally to all pages
        if np.sum(links[i]) == 0:
            transition_matrix[i] = np.ones(N) / N
        else:
            transition_matrix[i] = links[i] / np.sum(links[i])
    
    # Initialize PageRank vector with equal values
    pagerank = np.ones(N) / N
    
    # Matrix to handle the teleportation (damping factor)
    teleportation_matrix = np.ones((N, N)) / N
    
    # Power iteration
    for _ in range(max_iter):
        new_pagerank = d * np.dot(transition_matrix.T, pagerank) + (1 - d) * np.dot(teleportation_matrix.T, pagerank)
        
        # Check for convergence
        if np.linalg.norm(new_pagerank - pagerank, 1) < tol:
            break
        
        pagerank = new_pagerank
    
    return pagerank

# Example usage
if __name__ == "__main__":
    # Example adjacency matrix where a link from page i to page j is represented by a 1 at (i, j)
    links = np.array([[0, 1, 1, 0],
                      [0, 0, 0, 1],
                      [1, 1, 0, 1],
                      [0, 0, 0, 0]])

    # Run PageRank
    ranks = pagerank(links)
    
    # Print PageRank for each page
    print("PageRank values:")
    for i, rank in enumerate(ranks):
        print(f"Page {i+1}: {rank:.6f}")
