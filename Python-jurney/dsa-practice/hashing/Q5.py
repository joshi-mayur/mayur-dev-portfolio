"""
Problem: Find Common Elements in Two Arrays (Including Duplicates)

Given two integer arrays A and B, return an array of their common elements,
including duplicates. The output should reflect the number of times an element
appears in both arrays.

Constraints:
- 1 <= N, M <= 10^5
- 1 <= A[i], B[i] <= 10^9

Approach:
- Use a hash map (dictionary) to count the frequency of each element in A.
- Then iterate through B and for each element, check if it exists in the
  frequency map with a count > 0.
- If yes, add it to the result and reduce the count in the map.

Time Complexity: O(N + M)
Space Complexity: O(N)
"""

def common_elements(A, B):
    # Dictionary to store frequency of elements in array A
    freq_map = {}
    
    # List to store the common elements
    result = []

    # Step 1: Count frequency of elements in A
    for num in A:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Step 2: Iterate through B to find common elements
    for num in B:
        if num in freq_map and freq_map[num] > 0:
            result.append(num)       # Add to result
            freq_map[num] -= 1       # Decrease frequency to avoid extra matches

    return result

# Example Usage:
if __name__ == "__main__":
    # Test case 1
    A = [1, 2, 2, 1]
    B = [2, 3, 1, 2]
    print(common_elements(A, B))  # Output: [2, 1, 2]

    # Test case 2
    A = [2, 1, 4, 10]
    B = [3, 6, 2, 10, 10]
    print(common_elements(A, B))  # Output: [2, 10]
