"""
Problem Description:
Calculate x raised to the power n (x^n) using recursion.

Examples:
Input: x = 2, n = 3 → Output: 8
Input: x = 5, n = 0 → Output: 1

Constraints:
- x is a number (int or float)
- n is a non-negative integer
"""

def power(x, n):
    """
    Recursively calculates x raised to the power n.

    Args:
    x (int or float): The base number.
    n (int): The exponent (should be non-negative).

    Returns:
    int or float: The result of x^n
    """
    # Base case: anything to power 0 is 1
    if n == 0:
        return 1
    # Recursive case
    return x * power(x, n - 1)

if __name__ == "__main__":
    try:
        base = float(input("Enter the base (x): "))
        exponent = int(input("Enter the exponent (n): "))
        if exponent < 0:
            print("Please enter a non-negative exponent.")
        else:
            result = power(base, exponent)
            print(f"{base} ^ {exponent} = {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
