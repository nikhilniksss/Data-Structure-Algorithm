# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.


# check if string is palindrome or not

# Example 1:
# Input: s = "level"
# Output: True

# Example 2:
# Input: s = madamimadam
# Output: True

# Example 3:
# Input: s = race
# Output: False


def palindromic_string(s):
    left = 0
    right = len(s) - 1
    while left <  right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

s = "level"
print(palindromic_string(s))

s = "madamimadam"
print(palindromic_string(s))

s = "race"
print(palindromic_string(s))


