"""
Problem Description:

Given an integer A, generate a square matrix filled with elements 
from 1 to A^2 in spiral order and return the generated matrix.

Constraints:
1 <= A <= 1000

Input Format:
- A single integer A

Output Format:
- A 2D matrix (list of lists) filled in spiral order

Example Input:
Input 1:
    1
Input 2:
    2
Input 3:
    5

Example Output:
Output 1:
    [ [1] ]
Output 2:
    [ [1, 2],
      [4, 3] ]
Output 3:
    [ [1,   2,  3,  4, 5],
      [16, 17, 18, 19, 6],
      [15, 24, 25, 20, 7],
      [14, 23, 22, 21, 8],
      [13, 12, 11, 10, 9] ]
"""

def generate_spiral_matrix(A):
    matrix = [[0] * A for _ in range(A)]
    num = 1
    top, bottom, left, right = 0, A - 1, 0, A - 1

    while top <= bottom and left <= right:
        # Fill top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill bottom row
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # Fill left column
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


# Example usage
if __name__ == "__main__":
    A = 5  # You can change this value to test different inputs
    result = generate_spiral_matrix(A)
    for row in result:
        print(row)
