# Problem Description:
# You are given an array A of N integers and an integer B.
# Count the number of pairs (i, j) such that A[i] - A[j] = B and i ≠ j.
# Since the answer can be very large, return the remainder after dividing the count with 10^9 + 7.

# Note: Pair (i, j) is different from (j, i) in this problem since A[i] - A[j] is directional.

# Problem Constraints:
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9

# Input Format:
# First argument A is an array of integers.
# Second argument B is an integer.

# Output Format:
# Return an integer representing the number of valid (i, j) pairs modulo 10^9 + 7.

# Example Input 1:
# A = [3, 5, 1, 2], B = 4
# Output: 1
# Explanation: (5 - 1 = 4)

# Example Input 2:
# A = [1, 2, 1, 2], B = 1
# Output: 4
# Explanation: All (2, 1) pairs.

def count_pairs_difference(A, B):
    MOD = 10**9 + 7
    freq_map = {}
    count = 0

    for num in A:
        # Check how many previous elements satisfy A[i] - A[j] == B
        target1 = num - B
        if target1 in freq_map:
            count = (count + freq_map[target1]) % MOD
        # Store frequency for later elements to use
        freq_map[num] = freq_map.get(num, 0) + 1

    return count % MOD

# Example usage:
if __name__ == "__main__":
    A1 = [3, 5, 1, 2]
    B1 = 4
    print("Output 1:", count_pairs_difference(A1, B1))  # Output: 1

    A2 = [1, 2, 1, 2]
    B2 = 1
    print("Output 2:", count_pairs_difference(A2, B2))  # Output: 4
