"""
Problem: Scalar Multiplication of a Matrix

Given a matrix A (2D list) and an integer B,
return a new matrix where each element of A is multiplied by B.

Example:
Input:
A = [[1, 2],
     [3, 4]]
B = 2

Output:
[[2, 4],
 [6, 8]]
"""

def scalar_multiply_matrix(A, B):
    # Create a new matrix with the same dimensions
    result = []

    for row in A:
        new_row = [element * B for element in row]
        result.append(new_row)

    return result

# Example usage
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = 2
    output = scalar_multiply_matrix(A, B)
    print("Result of scalar multiplication:")
    print(output)
