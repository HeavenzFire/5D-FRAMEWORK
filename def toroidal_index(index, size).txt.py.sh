def toroidal_index(index, size):
    return index % size

def get_toroidal_element(matrix, indices):
    wrapped_indices = [toroidal_index(idx, dim) for idx, dim in zip(indices, matrix.shape)]
    return matrix[tuple(wrapped_indices)]

# Example usage
indices = [3, 4, 1, 0, 2]  # Indices beyond the matrix dimensions
element = get_toroidal_element(matrix_5d, indices)
print(element)
