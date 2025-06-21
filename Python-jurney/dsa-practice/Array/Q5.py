"""
Optimized Version:
Pick B elements from either end of array A to maximize their sum.

Approach:
- Precompute prefix sums from the front and back.
- For each i in range [0, B], try taking i elements from front and (B - i) from back.
- Use prefix sums to calculate the total in O(1) time per case.
- Time Complexity: O(B)
"""

def max_sum_from_ends(A, B):
    n = len(A)

    # Compute prefix sums from front
    prefix_front = [0] * (B + 1)
    for i in range(1, B + 1):
        prefix_front[i] = prefix_front[i - 1] + A[i - 1]

    # Compute prefix sums from back
    prefix_back = [0] * (B + 1)
    for i in range(1, B + 1):
        prefix_back[i] = prefix_back[i - 1] + A[-i]

    # Try all combinations
    max_sum = float('-inf')
    for i in range(B + 1):
        current_sum = prefix_front[i] + prefix_back[B - i]
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
if __name__ == "__main__":
    A = [5, -2, 3, 1, 2]
    B = 3
    print("Maximum sum from ends:", max_sum_from_ends(A, B))  # Output: 8
