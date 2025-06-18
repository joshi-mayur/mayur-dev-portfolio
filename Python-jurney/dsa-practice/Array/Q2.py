"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)

Given an array A of length N, find the maximum sum of any non-empty contiguous subarray.

Example:
Input  : A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output : 6
Explanation: [4, -1, 2, 1] has the largest sum = 6

Constraints:
1 <= N <= 10^6
-1000 <= A[i] <= 1000
"""

def max_subarray_sum(A):
    cur_sum = 0
    max_sum = -float('inf')  # Initialize to negative infinity

    for num in A:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)

        # If current sum drops below zero, reset it
        if cur_sum <= 0:
            cur_sum = 0

    return max_sum

# Example usage
if __name__ == "__main__":
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = max_subarray_sum(A)
    print("Maximum Subarray Sum:", result)
