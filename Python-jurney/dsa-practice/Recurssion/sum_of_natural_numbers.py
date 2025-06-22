"""
Problem Description:
Write a recursive function to calculate the sum of the first N natural numbers.

Constraints:
- 1 <= N <= 10^6 (but recursion limit in Python may restrict very large N)
- Natural numbers start from 1

Input:
- An integer N

Output:
- Sum of first N natural numbers

Example:
Input: 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15
"""

def sum_natural_numbers(n):
    """
    Recursively calculates the sum of the first N natural numbers.

    Args:
    n (int): The number up to which the sum is to be calculated.

    Returns:
    int: Sum of first n natural numbers.
    """
    # Base case
    if n == 1:
        return 1
    # Recursive case
    return n + sum_natural_numbers(n - 1)

if __name__ == "__main__":
    try:
        n = int(input("Enter a natural number: "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            result = sum_natural_numbers(n)
            print(f"Sum of first {n} natural numbers is: {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
