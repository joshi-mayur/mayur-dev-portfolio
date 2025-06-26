# Python program to find the length of the longest subarray with sum = 0

def longest_subarray_sum_zero(arr):
    # Initialize prefix sum and max length
    prefix_sum = 0
    max_len = 0

    # Dictionary to store first occurrence of each prefix sum
    sum_index = {}

    # Iterate through the array
    for i in range(len(arr)):
        prefix_sum += arr[i]

        # If prefix sum becomes 0, entire subarray from 0 to i has sum = 0
        if prefix_sum == 0:
            max_len = i + 1

        # If prefix_sum is already seen before,
        # the subarray from that index+1 to i has sum = 0
        if prefix_sum in sum_index:
            subarray_len = i - sum_index[prefix_sum]
            max_len = max(max_len, subarray_len)
        else:
            # Store the first occurrence of the prefix_sum
            sum_index[prefix_sum] = i

    return max_len


if __name__ == "__main__":
    # Sample test case
    arr = [1, -1, 3, 2, -5]
    
    # Output the result
    print("Longest subarray with sum 0 has length:", longest_subarray_sum_zero(arr))
