"""
Problem Description:
--------------------
SCALER organizes a series of contests aimed at helping learners enhance their coding skills.
Each learner can participate in multiple contests, and their participation is represented by integers in an array.

The goal is to identify how frequently each learner has participated in these contests.
This helps SCALER provide support to less active learners.

Given:
- An array A where each integer represents a learner's participation in a contest.
- An array B containing learners whose participation frequency you want to check.

Task:
Return a list of frequencies corresponding to each learner in B, based on their occurrences in A.

Problem Constraints:
--------------------
1 <= |A| <= 10^5
1 <= |B| <= 10^5
1 <= A[i] <= 10^5
1 <= B[i] <= 10^5

Input Format:
-------------
First argument: array A of integers (contest participants)
Second argument: array B of integers (learners to query)

Output Format:
--------------
Return a list of integers, each representing the frequency of a learner from B in A.

Example Input:
--------------
Input 1:
A = [1, 2, 1, 1]
B = [1, 2]

Input 2:
A = [2, 5, 9, 2, 8]
B = [3, 2]

Example Output:
---------------
Output 1: [3, 1]
Output 2: [0, 2]
"""

# Sample input
A = [1, 2, 1, 1]
B = [1, 2]

# Dictionary to store frequencies of elements in A
frequency_map = {}

# Count frequency of each learner in A
for learner in A:
    if learner in frequency_map:
        frequency_map[learner] += 1
    else:
        frequency_map[learner] = 1

# List to store result frequencies for each learner in B
result = []

# For each learner in B, get their frequency from frequency_map
for learner in B:
    if learner in frequency_map:
        result.append(frequency_map[learner])
    else:
        # If learner not in A, frequency is 0
        result.append(0)

# Output the result
print(result)
