# Problem Description:
# You are given an array A of N integers and an integer B.
# Count the number of pairs (i,j) such that A[i] + A[j] = B and i ≠ j.
# Since the answer can be very large, return the remainder after dividing the count with 10^9 + 7.
# Note - The pair (i,j) is same as the pair (j,i) and we need to count it only once.

# Problem Constraints:
# 1 <= N <= 10^5
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9

# Input Format:
# First argument A is an array of integers.
# Second argument B is an integer.

# Output Format:
# Return an integer representing the number of valid pairs modulo 10^9 + 7.

# Example Input 1:
# A = [3, 5, 1, 2]
# B = 8
# Example Output 1: 1

# Example Input 2:
# A = [1, 2, 1, 2]
# B = 3
# Example Output 2: 4

def count_pairs_with_sum(A, B):
    MOD = 10**9 + 7
    freq_map = {}
    count = 0

    for num in A:
        complement = B - num
        # If complement exists, add the frequency (number of times it appeared before)
        if complement in freq_map:
            count = (count + freq_map[complement]) % MOD
        # Update the frequency of the current number
        freq_map[num] = freq_map.get(num, 0) + 1

    return count % MOD

# Example usage:
if __name__ == "__main__":
    A1 = [3, 5, 1, 2]
    B1 = 8
    print("Output 1:", count_pairs_with_sum(A1, B1))  # Output: 1

    A2 = [1, 2, 1, 2]
    B2 = 3
    print("Output 2:", count_pairs_with_sum(A2, B2))  # Output: 4
