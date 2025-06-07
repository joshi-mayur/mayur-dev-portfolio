"""
Problem Description:
You are given an array of N integers, A1, A2, ..., AN and an integer B.
Return the count of distinct numbers in all windows of size B.

Return an array of size N-B+1 where the i-th element contains the number of
distinct elements in sequence Ai to Ai+B-1 (inclusive).

Constraints:
1 <= N <= 10^5
1 <= A[i] <= 10^9
1 <= B <= N

Example:
Input:  A = [1, 2, 1, 3, 4, 3], B = 3
Output: [2, 3, 3, 2]
"""

def count_distinct_elements_in_windows(A, B):
    """
    Count distinct elements in every window of size B using
    a sliding window and dictionary (no external imports).
    """
    n = len(A)
    if B > n:
        return []

    freq_map = {}  # Dictionary to store frequency of elements
    result = []    # List to store the number of distinct elements per window

    # Build the frequency map for the first window
    for i in range(B):
        if A[i] in freq_map:
            freq_map[A[i]] += 1
        else:
            freq_map[A[i]] = 1

    # Add count of distinct elements from the first window
    result.append(len(freq_map))

    # Slide the window across the array
    for i in range(B, n):
        # Element that goes out of the window
        outgoing = A[i - B]
        freq_map[outgoing] -= 1
        if freq_map[outgoing] == 0:
            del freq_map[outgoing]

        # Element that comes into the window
        incoming = A[i]
        if incoming in freq_map:
            freq_map[incoming] += 1
        else:
            freq_map[incoming] = 1

        # Append the current count of distinct elements
        result.append(len(freq_map))

    return result

# Example usage
A = [1, 2, 1, 3, 4, 3]
B = 3
output = count_distinct_elements_in_windows(A, B)
print("Distinct counts in each window:", output)
