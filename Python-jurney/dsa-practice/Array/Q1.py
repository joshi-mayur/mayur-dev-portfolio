"""
Problem: Trapping Rain Water

Given an array of non-negative integers representing the height of bars in a histogram,
compute how much water can be trapped after raining.

Example:
Input  : A = [5, 4, 1, 4, 3, 2, 7]
Output : 11

Approach:
Use two auxiliary arrays to store the maximum height to the left and right of every bar.
Then for each bar, water trapped = min(max_left, max_right) - height (if positive).
"""

def trap_rain_water(Arr):
    n = len(Arr)
    if n == 0:
        return 0

    # Step 1: Precompute max on the left for each bar
    max_on_left = [0] * n
    max_on_left[0] = Arr[0]
    for i in range(1, n):
        max_on_left[i] = max(max_on_left[i - 1], Arr[i])

    # Step 2: Precompute max on the right for each bar
    max_on_right = [0] * n
    max_on_right[-1] = Arr[-1]
    for i in range(n - 2, -1, -1):
        max_on_right[i] = max(max_on_right[i + 1], Arr[i])

    # Step 3: Calculate water trapped at each position
    total_water = 0
    for i in range(n):
        cur_water = min(max_on_left[i], max_on_right[i]) - Arr[i]
        if cur_water > 0:
            total_water += cur_water

    return total_water

# Example usage:
if __name__ == "__main__":
    Arr = [5, 4, 1, 4, 3, 2, 7]
    result = trap_rain_water(Arr)
    print("Total water trapped:", result)
