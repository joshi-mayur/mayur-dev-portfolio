"""
Problem: Count Elements with Frequency 1

You are given an array A of N integers. Return the count of elements that appear exactly once in the array.

Constraints:
- 1 <= N <= 10^5
- 1 <= A[i] <= 10^9

Approach:
- Use a hash map (dictionary) to count the frequency of each element.
- Traverse the frequency map and count how many elements have a frequency of 1.

Time Complexity: O(N)
Space Complexity: O(N)
"""

def count_unique_frequency(A):
    # Dictionary to store frequency of elements
    freq_map = {}
    
    # Step 1: Count frequency of each element
    for num in A:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Step 2: Count elements with frequency exactly 1
    count = 0
    for val in freq_map.values():
        if val == 1:
            count += 1

    return count

# Example Usage
if __name__ == "__main__":
    # Test case 1
    A = [3, 4, 3, 6, 6]
    print(count_unique_frequency(A))  # Output: 1 (only 4 appears once)

    # Test case 2
    A = [3, 3, 3, 9, 0, 1, 0]
    print(count_unique_frequency(A))  # Output: 2 (9 and 1 appear once)
