import numpy as np
import matplotlib.pyplot as plt

def generate_lattice(dimension, size):
    """Generate a lattice structure."""
    return np.random.rand(dimension, size, size)

def visualize_lattice(lattice):
    """Visualize the lattice structure."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = lattice
    ax.scatter(x, y, z, c='b', marker='o')
    plt.show()

# Example usage
if __name__ == "__main__":
    size = 30
    lattice = generate_lattice(3, size)
    visualize_lattice(lattice)
