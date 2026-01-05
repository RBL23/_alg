import numpy as np
import random

def riemann_n_dim(func, bounds, steps):
    """
    n-dimensional Riemann Sum (Midpoint Rule).
    
    :param func: Function to integrate, takes a list/array of length n.
    :param bounds: List of tuples [(min1, max1), (min2, max2), ...]
    :param steps: Number of divisions per dimension.
    """
    n = len(bounds)
    dx = [(b - a) / steps for a, b in bounds]
    total_volume = np.prod(dx)
    
    def recursive_sum(dim, current_point):
        if dim == n:
            return func(current_point)
        
        sum_val = 0.0
        a, b = bounds[dim]
        # Using midpoint rule for better convergence
        for i in range(steps):
            xi = a + (i + 0.5) * dx[dim]
            current_point[dim] = xi
            sum_val += recursive_sum(dim + 1, current_point)
        return sum_val

    # Start recursion
    result = recursive_sum(0, [0.0] * n)
    return result * total_volume

def monte_carlo_n_dim(func, bounds, samples=100000):
    """
    n-dimensional Monte Carlo Integration.
    
    :param func: Function to integrate.
    :param bounds: List of tuples [(min1, max1), ...]
    :param samples: Number of random points to sample.
    """
    n = len(bounds)
    bounds = np.array(bounds)
    mins = bounds[:, 0]
    maxs = bounds[:, 1]
    
    # Generate random points within the hyper-rectangle
    points = np.random.uniform(mins, maxs, (samples, n))
    
    # Evaluate function at all points
    f_values = np.apply_along_axis(func, 1, points)
    
    # Calculate hyper-volume
    volume = np.prod(maxs - mins)
    
    # Average value * hyper-volume
    return volume * np.mean(f_values)

# --- Example Usage: Volume of an N-dimensional Sphere ---

def is_inside_sphere(x):
    # If distance from origin <= 1, return 1 (inside), else 0
    return 1.0 if np.sum(np.square(x)) <= 1.0 else 0.0

if __name__ == "__main__":
    # Dimension of the sphere
    dim = 3
    # Integration bounds (from -1 to 1 for each dimension)
    sphere_bounds = [(-1, 1)] * dim
    
    print(f"Calculating volume of a {dim}D sphere (Exact: {4/3 * np.pi if dim==3 else 'Variable'})...")
    
    # Monte Carlo is usually faster for high dimensions
    mc_res = monte_carlo_n_dim(is_inside_sphere, sphere_bounds, samples=500000)
    print(f"Monte Carlo Result: {mc_res:.5f}")
    
    # Riemann is very slow for dim > 4 because of O(steps^n) complexity
    if dim <= 4:
        r_res = riemann_n_dim(is_inside_sphere, sphere_bounds, steps=20)
        print(f"Riemann Sum Result: {r_res:.5f}")
