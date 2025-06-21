"""
Problem Description:

You are given a collection of intervals A in a 2-D array format, where each interval 
is represented by a pair of integers [start, end]. The intervals are sorted based on 
their start values.

Your task is to merge all overlapping intervals and return the resulting set of 
non-overlapping intervals.

Constraints:
- 1 <= len(A) <= 100000
- 1 <= A[i][0] <= A[i][1] <= 100000
- Input is sorted based on the start value (A[i][0])

Input Format:
- A 2D list of intervals A

Output Format:
- A sorted list of non-overlapping intervals after merging

Examples:

Input 1:
    A = [ [1, 3], [2, 6], [8, 10], [15, 18] ]

Output 1:
    [ [1, 6], [8, 10], [15, 18] ]

Input 2:
    A = [ [2, 10], [4, 9], [6, 7] ]

Output 2:
    [ [2, 10] ]
"""

def merge_intervals(A):
    if not A:
        return []

    old = A[0]
    ans = []

    for new in A[1:]:
        s1, e1 = old
        s2, e2 = new

        if e1 >= s2:  # Overlapping intervals
            old = (min(s1, s2), max(e1, e2))
        else:
            ans.append(old)
            old = new

    ans.append(old)
    return ans


# Example usage
if __name__ == "__main__":
    A1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    A2 = [[2, 10], [4, 9], [6, 7]]

    print("Merged Intervals for A1:", merge_intervals(A1))
    print("Merged Intervals for A2:", merge_intervals(A2))
