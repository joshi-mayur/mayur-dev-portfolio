"""
Problem Description:

Given a matrix of integers A of size N x M and an integer B.

Each row and column in the matrix is sorted in non-decreasing order.
Find and return the position of B in the matrix in the following form:

- If A[i][j] == B, return (i + 1) * 1009 + (j + 1)
  (using 1-based indexing as per the problem requirement)
- If B occurs multiple times, return the smallest value of (i + 1) * 1009 + (j + 1)
- If B is not present, return -1

Constraints:
- 1 <= N, M <= 1000
- Time Complexity: O(N + M)

Approach:
- Start from the top-right of the matrix
- Use the sorted nature of rows and columns to reduce search space
- Track the minimum (i * 1009 + j) for all occurrences of B
"""

def search_matrix(A, B):
    i = 0
    j = len(A[0]) - 1
    min_val = float('inf')

    while i < len(A) and j >= 0:
        if A[i][j] == B:
            pos = (i + 1) * 1009 + (j + 1)
            min_val = min(min_val, pos)
            j -= 1  # Move left to find smaller j (smaller pos)
        elif A[i][j] < B:
            i += 1
        else:
            j -= 1

    return min_val if min_val != float('inf') else -1


# Example usage
if __name__ == "__main__":
    A = [
        [2, 8, 8, 8],
        [2, 8, 8, 8],
        [2, 8, 8, 8]
    ]
    B = 8
    result = search_matrix(A, B)
    print("Result:", result)  # Expected Output: 1011
