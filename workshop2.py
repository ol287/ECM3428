from matplotlib import *
from matplotlib.pyplot import *
from numpy import *
from scipy.optimize import rosen

# Task 1: Drawing the Rosenbrock function contours
def rosen_contours(Nx=100, Ny=100):
    """
    Draw contours of the Rosenbrock test function
    """
    x = linspace(-2.0, 2.0, Nx)  # Generate x values
    y = linspace(-2.0, 2.0, Ny)  # Generate y values

    R = zeros((Nx, Ny))  # Initialize the matrix to store Rosenbrock values
    for i in range(Nx):
        for j in range(Ny):
            X = asarray([x[i], y[j]])  # Create 2D point
            R[i, j] = rosen(X)  # Evaluate Rosenbrock function at the point

    v = concatenate((arange(20), arange(25, 500, 10)))  # Levels for contours
    clf()
    contour(x, y, R.T, v, alpha=0.3)  # Plot the contours
    colorbar()
    plot(1.0, 1.0, marker='o', color='yellow')  # Mark the minimum (1, 1)

# Function to cycle through the color set
def cycle(s):
    """
    Yield elements of s cyclically
    """
    n = 0
    while True:
        yield s[n % len(s)]
        n += 1

# Task 2: Helper function to decide interaction with user
def maybe_wait(interact):
    if interact:
        return input('-----> ')  # Wait for user input

# Task 3: Drawing the simplex
def draw_simplex(S, colours):
    """
    Draw the simplex S in the colour given by the colour generator colours.
    """
    D = len(S[0][1])  # Dimension of the problem
    v = zeros((D + 2, 2))  # Initialize array for plotting simplex vertices
    for i in range(D + 1):
        v[i, :] = S[i][1]  # Get simplex points
    v[-1, :] = S[0][1]  # Repeat the first point to close the loop
    plot(v[:, 0], v[:, 1], color=next(colours))  # Plot the simplex

# Task 4: Implementing the Nelder-Mead algorithm
def neldermead(x0, func, tolx=1e-3, tolf=1e-3, Niter=1000, draw=True, interact=True):
    """
    Nelder Mead optimization of func(x) using the Nelder-Mead simplex algorithm.

    Arguments:
    x0: Initial guess (vector/list)
    func: The function to be minimized
    tolx: Stop when the vertices of the simplex are closer than this
    tolf: Stop if the function values at the simplex vertices are closer than this
    Niter: Maximum number of iterations
    draw: Draw the simplices if True
    interact: Wait for the user to press return after each iteration if True

    Returns:
    fmin: The function value at the minimum
    x: The point at which the minimum is found
    """

    D = len(x0)  # Dimension of the problem
    simplex = []  # List to store simplex vertices
    simplex.append((func(x0), x0))  # Add initial point to the simplex

    # Create initial simplex by moving one coordinate of x0 in each direction
    for i in range(D):
        x = x0.copy()
        x[i] *= 1.1  # Move the i-th coordinate
        simplex.append((func(x), x))  # Add new point to the simplex

    # Draw the initial simplex if requested
    if draw:
        colours = cycle("rgbmky")
        draw_simplex(simplex, colours)
        maybe_wait(interact)

    # Task 1: Replace centroid code with a function
    def centroid(simplex):
        """
        Calculate the centroid of all points except the worst point.
        """
        c = zeros(D)  # Initialize the centroid
        for v in simplex[1:]:
            c += v[1]  # Sum up points
        c /= D  # Average to get the centroid
        return c

    # Main optimization loop
    for iter in range(Niter):
        c = centroid(simplex)  # Calculate centroid of the simplex
        x = c + (c - simplex[0][1])  # Reflection through the centroid
        simplex[0] = (func(x), x)  # Replace the worst point with the new point

        # Draw updated simplex
        if draw:
            draw_simplex(simplex, colours)
            maybe_wait(interact)

        # Task 3: Termination condition
        if max([linalg.norm(simplex[i][1] - simplex[j][1]) for i in range(D+1) for j in range(D+1)]) < tolx:
            # Stop if the simplex points are close enough
            break
        if max([abs(simplex[i][0] - simplex[j][0]) for i in range(D+1) for j in range(D+1)]) < tolf:
            # Stop if function values are close enough
            break

    return simplex[0]  # Return the result (minimum function value and point)

# Main part of the code
if __name__ == "__main__":
    rosen_contours()  # Draw Rosenbrock contours
    x0 = asarray([-1.0, 1.0])  # Initial guess
    neldermead(x0, rosen, draw=True, interact=True)  # Call the Nelder-Mead algorithm
    maybe_wait(True)  # Wait for user interaction to end
