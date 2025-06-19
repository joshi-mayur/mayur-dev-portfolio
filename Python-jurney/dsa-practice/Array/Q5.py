"""
Problem: Pick B elements from either end of the array to maximize their sum.

Given an array A and an integer B, remove exactly B elements from either front or back
and return the maximum possible sum of those removed elements.

Approach:
Try all combinations of taking i elements from the front and (B - i) from the back.
Calculate the sum for each combination and return the maximum.
"""

def max_sum_from_ends(A, B):
    n = len(A)
    max_sum = float('-inf')

    # Try all combinations of taking i from front and B-i from back
    for i in range(B + 1):
        front = A[:i]             # First i elements
        back = A[n - (B - i):]    # Last B-i elements
        current_sum = sum(front) + sum(back)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
if __name__ == "__main__":
    A = [5, -2, 3, 1, 2]
    B = 3
    print("Maximum sum from ends:", max_sum_from_ends(A, B))  # Output: 8
