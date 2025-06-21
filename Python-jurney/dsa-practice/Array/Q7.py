"""
Problem Description:

You are given a n x n 2D matrix A representing an image.
Rotate the image by 90 degrees (clockwise) in-place.

Note:
- You must rotate the matrix in-place.
- Using additional array will only get partial score.

Constraints:
- 1 <= n <= 1000

Input Format:
- A: 2D matrix (list of lists) of integers

Output Format:
- Return the same 2D matrix rotated in-place.

Example Input:
Input 1:
 A = [
     [1, 2],
     [3, 4]
 ]

Input 2:
 A = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]

Example Output:
Output 1:
 [
     [3, 1],
     [4, 2]
 ]

Output 2:
 [
     [7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]
 ]
"""

def rotate_matrix(A):
    n = len(A)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            A[i][j], A[j][i] = A[j][i], A[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        A[i].reverse()

    return A


# Example usage:
if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in A:
        print(row)

    rotate_matrix(A)

    print("\nRotated Matrix:")
    for row in A:
        print(row)
