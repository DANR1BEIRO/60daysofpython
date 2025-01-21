def transponse_matrix(matrix):
    """
    Function that take a grid (3x3 matrix) and flip it so that rows
    become columns and columns become rows. This is called the transponse of a matrix
    
    Parameters:
    This function will take one input, called matrix. 
    A matrix is like a grid of numbers. 
    
    returns:
    Transponse matrix
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [
    [1, 2, 3], # row 1
    [4, 5, 6], # row 2
    [7, 8, 9]  # row 3
]
transpose = transponse_matrix(matrix)

    
print(("Original matrix:"))
for line in matrix:
    print(line)

print("\nTransponse matrix:")
for line in transpose:
    print(line)