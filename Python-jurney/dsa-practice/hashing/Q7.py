"""
Problem:
Given an array A of N integers, find the count of subarrays that sum to zero.
Since the answer can be very large, return the result modulo 10^9 + 7.

Constraints:
1 <= N <= 10^5
-10^9 <= A[i] <= 10^9

Example:
Input: A = [1, -1, -2, 2]
Output: 3
Explanation:
The subarrays with sum = 0 are: [1, -1], [-2, 2], and [1, -1, -2, 2]
"""

def prefix_sum(A):
    """
    Computes the prefix sum array for a given list A.
    
    Parameters:
    A (list): List of integers.

    Returns:
    list: Prefix sum array.
    """
    pf = [A[0]]  # Initialize with first element

    for i in range(1, len(A)):
        pf.append(pf[i - 1] + A[i])

    return pf


def count_zero_sum_subarrays(A):
    """
    Counts the number of subarrays with sum = 0 using prefix sums.

    Parameters:
    A (list): List of integers.

    Returns:
    int: Count of zero-sum subarrays modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    pf = prefix_sum(A)  # Get prefix sums
    freq_map = {0: 1}   # Include 0 for subarrays starting from index 0
    count = 0

    for val in pf:
        if val in freq_map:
            freq_map[val] += 1
        else:
            freq_map[val] = 1

    # Count the number of valid subarray pairs
    for freq in freq_map.values():
        if freq > 1:
            count = (count + (freq * (freq - 1)) // 2) % MOD

    return count


# Example usage
if __name__ == "__main__":
    A = [1, -1, -2, 2]
    result = count_zero_sum_subarrays(A)
    print("Count of zero-sum subarrays:", result)
