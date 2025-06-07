#Problem Description : 
#Determine the "GOOD"ness of a given string A, where the "GOOD"ness is defined by the length of the longest substring that contains no repeating characters. The greater the length of this unique-character substring, the higher the "GOOD"ness of the string.
#Your task is to return an integer representing the "GOOD"ness of string A.
#Note: The solution should be achieved in O(N) time complexity, where N is the length of the string.

#Problem Constraints#

#1# <= size(A) <= 106

#String consists of lowerCase,upperCase characters and digits are also present in the string A.
#
#Input Format
#Single Argument representing string A.
#Output Format
#Return an integer denoting the maximum possible length of substring without repeating characters.

#Exnample Input
#Sput 1:
#    A = "abcabcbb"
#Input 2:
#    A = "AaaA"
#Example Output
# Output 1:
#  3
#Output 2:
#6

# Input string
input_str = "abcabcbb"

# Initialize an empty set to store unique characters in the current window
my_set = set()

# Start of the sliding window
start = 0

# To store the maximum length found
max_len = 0

# Loop through the string using the 'end' pointer (right side of the window)
for end in range(len(input_str)):
    
    # If the current character already exists in the set,
    # it means we have a duplicate and need to shrink the window from the left
    while input_str[end] in my_set:
        # Remove the character at 'start' from the set and move 'start' forward
        my_set.remove(input_str[start])
        start += 1

    # Add the current character to the set (it’s now guaranteed to be unique in the window)
    my_set.add(input_str[end])

    # Update max length of substring found so far
    max_len = max(max_len, end - start + 1)

# Print the result
print(max_len)
