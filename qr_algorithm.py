import numpy as np

#QR algorithm to compute the eigenvalues of a given square matrix

def qr_algorithm(matrix, max_iterations=1000, tolerance=1e-10):
    """
    Perform the QR algorithm to compute the eigenvalues of a square matrix.

    Parameters:
    - matrix (numpy.ndarray): The input square matrix for which eigenvalues are computed.
    - max_iterations (int): The maximum number of iterations allowed.
    - tolerance (float): The convergence tolerance for determining eigenvalues.

    Returns:
    - numpy.ndarray: An array containing the eigenvalues of the matrix.
    """

    # Step 1: Make a copy of the matrix to avoid modifying the original
    A = np.copy(matrix)
    n = A.shape[0]  # Size of the matrix

    # Step 2: Perform iterations of the QR algorithm
    for i in range(max_iterations):
        # Step 3: Decompose A into Q and R where A = Q * R
        Q, R = np.linalg.qr(A)

        # Step 4: Form the new matrix A by multiplying R and Q (A_next = R * Q)
        A_next = R @ Q

        # Step 5: Check for convergence by seeing if off-diagonal elements are close to zero
        if np.allclose(A, A_next, atol=tolerance):
            break  # Stop if converged

        # Update A for the next iteration
        A = A_next

    # Step 6: Extract the diagonal elements as the eigenvalues
    eigenvalues = np.diag(A)
    
    return eigenvalues

# Example usage
A = np.array([[4, 1], [2, 3]])  # Define a 2x2 matrix
eigenvalues = qr_algorithm(A)   # Compute the eigenvalues
print("Computed Eigenvalues:", eigenvalues)
