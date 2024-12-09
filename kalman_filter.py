import numpy as np

def kalman_filter(A, B, H, Q, R, x_initial, P_initial, measurements, controls):
    """
    Implements the Kalman Filter algorithm.
    
    Parameters:
        A: State transition matrix
        B: Control input matrix
        H: Observation matrix
        Q: Process noise covariance
        R: Measurement noise covariance
        x_initial: Initial state estimate
        P_initial: Initial estimate covariance
        measurements: Array of observed measurements
        controls: Array of control inputs
    
    Returns:
        x_estimates: Array of state estimates
        P_estimates: Array of estimate covariance matrices
    """
    # Initialize state and covariance
    x = x_initial
    P = P_initial
    
    # Store estimates
    x_estimates = []
    P_estimates = []
    
    for n in range(len(measurements)):
        # Predict step
        x = A @ x + B @ controls[n]
        P = A @ P @ A.T + Q
        
        # Measurement update step
        z = measurements[n]
        K = P @ H.T @ np.linalg.inv(H @ P @ H.T + R)  # Kalman Gain
        x = x + K @ (z - H @ x)  # Update state
        P = (np.eye(P.shape[0]) - K @ H) @ P  # Update covariance
        
        # Save estimates
        x_estimates.append(x)
        P_estimates.append(P)
    
    return np.array(x_estimates), np.array(P_estimates)

# Example usage
if __name__ == "__main__":
    # Define matrices and parameters (example values)
    A = np.array([[1]])       # State transition matrix
    B = np.array([[0]])       # Control input matrix
    H = np.array([[1]])       # Observation matrix
    Q = np.array([[0.1]])     # Process noise covariance
    R = np.array([[0.1]])     # Measurement noise covariance
    x_initial = np.array([0]) # Initial state estimate
    P_initial = np.array([[1]])  # Initial estimate covariance

    # Simulated measurements and controls
    measurements = [np.array([i]) for i in [1, 2, 3, 4, 5]]
    controls = [np.array([0]) for _ in range(5)]

    # Run Kalman Filter
    x_estimates, P_estimates = kalman_filter(A, B, H, Q, R, x_initial, P_initial, measurements, controls)

    # Print results
    for i, (x, P) in enumerate(zip(x_estimates, P_estimates)):
        print(f"Step {i+1}:")
        print(f"State Estimate: {x}")
        print(f"Estimate Covariance: {P}")
        print()
