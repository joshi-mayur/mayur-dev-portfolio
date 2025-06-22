"""
Problem Description:

Given a binary sorted matrix A of size N x N, return the row index with 
the maximum number of 1s.

Rules:
- If two rows have the same number of 1s, return the one with the lower index.
- Each row is sorted (0s followed by 1s).
- Use 0-based indexing.
- Expected time: O(N + N)

Approach:
- Start from top-right corner.
- Move left for 1s, down for 0s.
- Track the row index with maximum 1s seen so far.
"""

def row_with_max_ones(A):
    n = len(A)
    row = 0
    col = n - 1
    max_row_index = -1

    while row < n and col >= 0:
        if A[row][col] == 1:
            max_row_index = row  # found more 1s
            col -= 1             # move left
        else:
            row += 1             # move down

    return max_row_index


# Example usage
if __name__ == "__main__":
    A = [
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 1]
    ]
    print("Row with max 1s:", row_with_max_ones(A))  # Output: 0
