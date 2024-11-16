import matplotlib.pyplot as plt
import numpy as np

# Define the dimensions of the 5D matrix
dim1, dim2, dim3, dim4, dim5 = 10, 10, 10, 10, 10

# Create the 5D matrix
matrix = np.random.rand(dim1, dim2, dim3, dim4, dim5)

# Define the vantage point
vantage_point = (5, 5, 5)

# Create a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the 5D matrix from the vantage point
for i in range(dim1):
  for j in range(dim2):
    for k in range(dim3):
      ax.scatter(i, j, k, c=matrix[i, j, k, vantage_point[0], vantage_point[1]])

# Set the axis limits
ax.set_xlim(0, dim1)
ax.set_ylim(0, dim2)
ax.set_zlim(0, dim3)

# Show the plot
plt.show()
