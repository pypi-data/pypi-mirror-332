import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg

def generate_random_field(size, length_scale, num_points=100, kernel='gaussian'):
    """
    Generate a 2D pseudorandom field with mean 0 and variance 1.
    
    Parameters:
    - size: tuple of (height, width) for the field dimensions
    - length_scale: float, controls smoothness (larger = smoother)
    - num_points: int, number of grid points per dimension
    - kernel: str, type of covariance kernel ('gaussian' or 'exponential')
    
    Returns:
    - field: 2D numpy array with the random field
    """
    
    # Create grid
    x = np.linspace(0, size[0], num_points)
    y = np.linspace(0, size[1], num_points)
    X, Y = np.meshgrid(x, y)
    
    # Compute distances between all points
    coords = np.stack([X.flatten(), Y.flatten()], axis=1)
    dist = np.sqrt(((coords[:, None, :] - coords[None, :, :]) ** 2).sum(axis=2))
    
    # Define covariance kernel
    if kernel == 'gaussian':
        cov = np.exp(-dist**2 / (2 * length_scale**2))
    elif kernel == 'exponential':
        cov = np.exp(-dist / length_scale)
    else:
        raise ValueError("Kernel must be 'gaussian' or 'exponential'")
    
    # Ensure positive definiteness and symmetry
    cov = (cov + cov.T) / 2  # Make perfectly symmetric
    cov += np.eye(cov.shape[0]) * 1e-6  # Add small jitter for stability
    
    # Generate random field using Cholesky decomposition
    L = linalg.cholesky(cov, lower=True)
    z = np.random.normal(0, 1, size=num_points * num_points)
    field_flat = L @ z
    
    # Reshape and normalize to mean 0, variance 1
    field = field_flat.reshape(num_points, num_points)
    field = (field - np.mean(field)) / np.std(field)
    
    return field

# Example usage and visualization
def plot_field():
    # Parameters
    size = (10, 10)  # Field size
    length_scale = 2.0  # Controls smoothness
    
    # Generate field
    field = generate_random_field(size, length_scale, num_points=100, kernel='gaussian')
    
    # Plot
    plt.figure(figsize=(8, 6))
    plt.imshow(field, cmap='viridis', extent=[0, size[0], 0, size[1]])
    plt.colorbar(label='Field Value')
    plt.title(f'Random Field (length_scale={length_scale})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    
    # Verify mean and variance
    print(f"Mean: {np.mean(field):.4f}")
    print(f"Variance: {np.var(field):.4f}")

if __name__ == "__main__":
    plot_field()