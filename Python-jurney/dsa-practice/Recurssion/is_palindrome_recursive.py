"""
Problem Description:
Check if a given string is a palindrome using recursion.

A palindrome is a string that reads the same forward and backward.
Ignore case sensitivity and non-alphanumeric characters (optional enhancement).

Examples:
Input: "madam" → Output: True
Input: "hello" → Output: False
"""

def is_palindrome(s, left, right):
    """
    Recursively checks whether a string is a palindrome.

    Args:
    s (str): The input string.
    left (int): The starting index.
    right (int): The ending index.

    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Base case: If the indices cross, it's a palindrome
    if left >= right:
        return True

    # If characters don't match, it's not a palindrome
    if s[left] != s[right]:
        return False

    # Recursive case
    return is_palindrome(s, left + 1, right - 1)

if __name__ == "__main__":
    raw_input = input("Enter a string: ")
    # Optional cleanup: remove non-alphanumeric characters and make lowercase
    cleaned = ''.join(char.lower() for char in raw_input if char.isalnum())

    if is_palindrome(cleaned, 0, len(cleaned) - 1):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
