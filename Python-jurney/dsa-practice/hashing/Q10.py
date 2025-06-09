def first_repeating_element(A):
    """
    Problem Description:
    Given an integer array A of size N, find the first repeating element in it.
    We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.
    If there is no repeating element, return -1.

    Problem Constraints:
    1 <= N <= 10^5
    1 <= A[i] <= 10^9

    Input Format:
    - A: List of integers of size N

    Output Format:
    - Return the first repeating element. If none, return -1.

    Example Input:
    Input:  A = [10, 5, 3, 4, 3, 5, 6]
    Output: 5

    Input:  A = [6, 10, 5, 4, 9, 120]
    Output: -1
    """
    
    freq_map = {}

    # Count frequency of each element
    for num in A:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Find the first element whose count is more than 1
    for num in A:
        if freq_map[num] > 1:
            return num

    # If no repeating element found
    return -1


# Example usage
A = [10, 5, 3, 4, 3, 5, 6]
print(first_repeating_element(A))  # Output: 5
