"""
Problem Description:

Given an array A of integers and a value B, find the minimum number of swaps 
required to bring all elements ≤ B together in the array.

- You can swap any two elements (not necessarily adjacent).
- Expected time complexity: O(N)

Approach:
1. Count how many elements are ≤ B (call them "good").
2. Use a sliding window of size equal to that count.
3. In each window, count how many "bad" (> B) elements are there.
4. The window with the minimum bads gives the minimum swaps required.

"""

def min_swaps_to_group_elements(A, B):
    n = len(A)

    # Step 1: Count how many elements are ≤ B (good elements)
    count_good = sum(1 for x in A if x <= B)

    # Step 2: Count bad elements in the first window of size count_good
    bad = 0
    for i in range(count_good):
        if A[i] > B:
            bad += 1

    # Step 3: Initialize result with the first window's bad count
    result = bad

    # Step 4: Slide the window across the array
    for start in range(1, n - count_good + 1):
        end = start + count_good - 1

        # If the element going out was bad, reduce bad count
        if A[start - 1] > B:
            bad -= 1

        # If the new element coming in is bad, increase bad count
        if A[end] > B:
            bad += 1

        # Track the minimum number of bads across all windows
        result = min(result, bad)

    return result


# Example usage
if __name__ == "__main__":
    A = [10, 1, 12, 10, 3, 14, 10, 5, 8]
    B = 8
    print("Minimum swaps required:", min_swaps_to_group_elements(A, B))  # Output: 2
