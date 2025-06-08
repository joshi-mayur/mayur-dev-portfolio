"""
Problem Description:

Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B.

Problem Constraints:
 1 <= length of the array <= 50000
-1000 <= A[i] <= 1000

Input Format:
The first argument given is the integer array A.
The second argument given is integer B.

Output Format:
Return the total number of subarrays having sum equals to B.

Example Input:
Input 1:
A = [1, 0, 1]
B = 1
Input 2:
A = [0, 0, 0]
B = 0

Example Output:
Output 1:
4
Output 2:
6
"""

def count_subarrays_with_sum_B(A, B):
    """
    Counts number of subarrays with sum equal to B using prefix sums and a dictionary.

    :param A: List[int] - Input array
    :param B: int - Target sum
    :return: int - Number of subarrays with sum equal to B
    """
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}  # To handle subarrays starting at index 0

    for num in A:
        prefix_sum += num
        required_sum = prefix_sum - B

        if required_sum in prefix_map:
            count += prefix_map[required_sum]

        # Beginner-friendly way to update the prefix_map
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] = prefix_map[prefix_sum] + 1  # Increase count by 1
        else:
            prefix_map[prefix_sum] = 1  # First time seeing this prefix sum

    return count


# Example Usage
if __name__ == "__main__":
    A1 = [1, 0, 1]
    B1 = 1
    print("Output 1:", count_subarrays_with_sum_B(A1, B1))  # Expected: 4

    A2 = [0, 0, 0]
    B2 = 0
    print("Output 2:", count_subarrays_with_sum_B(A2, B2))  # Expected: 6
