"""
Problem Description:
Reverse a string using recursion.

Examples:
Input: "hello"
Output: "olleh"

Constraints:
- Input is a non-empty string
"""

def reverse_string(s):
    """
    Recursively reverses a string.

    Args:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    # Base case: single character or empty string
    if len(s) <= 1:
        return s
    # Recursive case
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    input_str = input("Enter a string to reverse: ")
    result = reverse_string(input_str)
    print("Reversed string:", result)
