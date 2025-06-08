# Problem: Subarray with Sum 0
# --------------------------------------
# Given an array of integers A, find and return whether the given array 
# contains a non-empty subarray with a sum equal to 0.
#
# Return 1 if such a subarray exists, otherwise return 0.
#
# Constraints:
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9
#
# Examples:
# Input:  A = [1, 2, 3, 4, 5]
# Output: 0   (no subarray has sum 0)
#
# Input:  A = [4, -1, 1]
# Output: 1   (subarray [-1, 1] has sum 0)

def has_zero_sum_subarray(A):
    """
    Function to check if a subarray with sum zero exists using prefix sum and hash map.

    :param A: List[int] - input array
    :return: int - 1 if subarray with sum 0 exists, else 0
    """

    prefix_sum = 0
    prefix_sum_map = {0: 1}  # To handle subarray starting from index 0

    for num in A:
        prefix_sum += num

        # If current prefix sum was already seen, a zero-sum subarray exists
        if prefix_sum in prefix_sum_map:
            return 1
        else:
            prefix_sum_map[prefix_sum] = 1

    return 0

# Example Usage
if __name__ == "__main__":
    A1 = [1, 2, 3, 4, 5]
    print(has_zero_sum_subarray(A1))  # Output: 0

    A2 = [4, -1, 1]
    print(has_zero_sum_subarray(A2))  # Output: 1
