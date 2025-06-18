"""
Problem: Transpose of a Matrix

Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.

Example:
Input  : A = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

Output : [[1, 4, 7],
          [2, 5, 8],
          [3, 6, 9]]
"""

def transpose(A):
    rows = len(A)
    cols = len(A[0])
    
    # Initialize empty result matrix
    result = []

    # Loop through columns and build each transposed row
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(A[r][c])
        result.append(new_row)

    return result

# Example usage
if __name__ == "__main__":
    A1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A2 = [[1, 2], [1, 2], [1, 2]]

    print("Transpose of A1:")
    print(transpose(A1))  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    print("Transpose of A2:")
    print(transpose(A2))  # Output: [[1, 1, 1], [2, 2, 2]]
