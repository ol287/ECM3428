import matplotlib.pyplot as plt
import math

# Function to find the orientation of the triplet (p, q, r)
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

# Function to find the convex hull using the Gift Wrapping (Jarvis March) algorithm
def gift_wrapping(points):
    hull = []
    start = min(points, key=lambda p: p[0])
    point_on_hull = start

    while True:
        hull.append(point_on_hull)
        endpoint = points[0]
        
        for p in points:
            if p == point_on_hull:
                continue
            if endpoint == point_on_hull or orientation(point_on_hull, endpoint, p) == 2:
                endpoint = p

        point_on_hull = endpoint
        if point_on_hull == start:
            break

    return hull

# Example usage
points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
convex_hull = gift_wrapping(points)

# Plotting the points and the convex hull
def plot_convex_hull(points, hull):
    # Unzip points for easier plotting
    x, y = zip(*points)
    
    # Plot all points
    plt.scatter(x, y, label="Points", color="blue")
    
    # Plot the convex hull path
    hull_x, hull_y = zip(*hull)
    plt.plot(hull_x + (hull_x[0],), hull_y + (hull_y[0],), 'r-', label="Convex Hull")

    # Highlight points on the hull
    plt.scatter(hull_x, hull_y, color="red")

    # Add labels and legend
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Convex Hull using Gift Wrapping (Jarvis March)")
    plt.legend()
    plt.show()

# Visualize the convex hull
plot_convex_hull(points, convex_hull)
