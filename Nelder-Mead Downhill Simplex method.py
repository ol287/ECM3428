import numpy as np
import matplotlib.pyplot as plt

def nelder_mead(f, initial_simplex, alpha=1, gamma=2, rho=0.5, sigma=0.5, max_iter=1000, tol=1e-6):
    """
    Nelder-Mead Downhill Simplex method for minimizing a function and plotting the simplex at each iteration.

    Parameters:
    f : function
        The objective function to minimize.
    initial_simplex : np.array
        A (D+1) x D array where D is the dimensionality of the problem.
    alpha : float, optional
        Reflection coefficient, typically 1.
    gamma : float, optional
        Expansion coefficient, typically 2.
    rho : float, optional
        Contraction coefficient, typically 0.5.
    sigma : float, optional
        Shrink coefficient, typically 0.5.
    max_iter : int, optional
        Maximum number of iterations.
    tol : float, optional
        Convergence tolerance.
    
    Returns:
    np.array
        The optimized point (minimum of the function).
    """

    # Copy the initial simplex so we don't modify the original
    simplex = np.copy(initial_simplex)
    num_vertices = simplex.shape[0]
    
    # Set up plotting
    fig, ax = plt.subplots()
    plot_simplex(ax, simplex, f, 0)  # Initial simplex plot
    
    for i in range(max_iter):
        # Step 1: Sort the simplex points based on their function values
        simplex = sorted(simplex, key=lambda x: f(x))
        f_values = np.array([f(vertex) for vertex in simplex])

        # Step 2: Plot the current simplex
        plot_simplex(ax, simplex, f, i+1)

        # Step 3: Check for convergence (difference between max and min function values)
        if np.max(f_values) - np.min(f_values) < tol:
            plt.show()
            return simplex[0]
        
        # Step 4: Calculate the centroid of the best points (all but the worst point)
        centroid = np.mean(simplex[:-1], axis=0)
        
        # Step 5: Reflection
        worst_point = simplex[-1]
        reflected_point = centroid + alpha * (centroid - worst_point)
        f_reflected = f(reflected_point)
        
        if f_reflected < f_values[0]:
            # Step 6: Expansion if reflected point is better than the best point
            expanded_point = centroid + gamma * (reflected_point - centroid)
            f_expanded = f(expanded_point)
            
            if f_expanded < f_reflected:
                simplex[-1] = expanded_point
            else:
                simplex[-1] = reflected_point
        elif f_values[0] <= f_reflected < f_values[-2]:
            # Accept the reflected point if it's better than the second worst but not better than the best
            simplex[-1] = reflected_point
        else:
            # Step 7: Contraction
            if f_reflected < f_values[-1]:
                worst_point = reflected_point
            contracted_point = centroid + rho * (worst_point - centroid)
            f_contracted = f(contracted_point)
            
            if f_contracted < f_values[-1]:
                simplex[-1] = contracted_point
            else:
                # Step 8: Shrink the simplex if contraction fails
                best_point = simplex[0]
                for j in range(1, num_vertices):
                    simplex[j] = best_point + sigma * (simplex[j] - best_point)
    
    # Final plot after iterations
    plt.show()

    # If algorithm didn't converge, return the best point found
    return simplex[0]

def plot_simplex(ax, simplex, f, iteration):
    """
    Plot the simplex and label the vertices.

    Parameters:
    ax : Matplotlib axis object
        The axis on which to plot.
    simplex : np.array
        The vertices of the simplex.
    f : function
        The function being minimized (used for labeling points with function values).
    iteration : int
        Current iteration number (used for the title).
    """
    
    simplex = np.array(simplex)
    ax.clear()
    
    # Plot simplex lines connecting the vertices
    for i in range(len(simplex)):
        next_point = simplex[(i + 1) % len(simplex)]  # Connect to the next vertex
        ax.plot([simplex[i][0], next_point[0]], [simplex[i][1], next_point[1]], 'b-', lw=1)

    # Plot the vertices
    for vertex in simplex:
        ax.plot(vertex[0], vertex[1], 'ro')
        ax.text(vertex[0], vertex[1], f'{f(vertex):.2f}', fontsize=12)

    # Set plot limits and title
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_title(f'Simplex at Iteration {iteration}')
    plt.pause(0.5)  # Pause to visually show changes

# Example usage:
def rosenbrock(x):
    # Rosenbrock function: Standard test function for optimization algorithms.
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

# Initial simplex for 2D Rosenbrock function
initial_simplex = np.array([[1.3, 1.3], [1.0, 1.0], [0.7, 0.9]])

# Run the Nelder-Mead algorithm with plotting
minimum = nelder_mead(rosenbrock, initial_simplex)

print("Found minimum:", minimum)
