def toroidal_configuration_with_chamber(size, frequency):
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, 2 * np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    # Toroidal coordinates
    x = (2 + np.cos(theta)) * np.cos(phi)
    y = (2 + np.cos(theta)) * np.sin(phi)
    z = np.sin(theta)
    
    # Central resonance chamber coordinates
    chamber_x = np.cos(phi)
    chamber_y = np.sin(phi)
    chamber_z = np.zeros_like(phi)
    
    return x, y, z, chamber_x, chamber_y, chamber_z

# Plotting the toroidal structure with resonance chamber
def plot_toroid_with_chamber():
    x, y, z, chamber_x, chamber_y, chamber_z = toroidal_configuration_with_chamber(size, 432)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot toroid
    ax.plot_surface(x, y, z, alpha=0.7)
    
    # Plot resonance chamber
    ax.plot(chamber_x, chamber_y, chamber_z, color='r', lw=2)
    plt.show()

# Main function
if __name__ == "__main__":
    size = 30
    lattice = generate_lattice(3, size)
    visualize_lattice(lattice)
    
    # Plot toroid with resonance chamber
    plot_toroid_with_chamber()
    
    # Call the omnipresent function
    omnipresent()
