"""
Problem Description:
--------------------
Given an array A of N integers, return the number of unique elements in the array.

Problem Constraints:
--------------------
1 <= N <= 10^5
1 <= A[i] <= 10^9

Input Format:
-------------
First argument A is an array of integers.

Output Format:
--------------
Return an integer.

Example Input:
--------------
Input 1: A = [3, 4, 3, 6, 6]
Input 2: A = [3, 3, 3, 9, 0, 1, 0]

Example Output:
---------------
Output 1: 3
Output 2: 4
"""

# Sample input
A = [3, 4, 3, 6, 6]

# Dictionary to count occurrences of each element
element_count = {}

# Iterate through each number in the array
for num in A:
    # If number already in dictionary, increment its count
    if num in element_count:
        element_count[num] += 1
    else:
        # If it's the first occurrence, initialize count to 1
        element_count[num] = 1

# The number of unique elements is the number of keys in the dictionary
print(len(element_count))
