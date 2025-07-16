# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

def valid_palindrome_2(s):
    def is_palindrome_range(i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left+1,right) or is_palindrome_range(left,right - 1)
        left += 1
        right -= 1
    return True

s = "aba"
print(valid_palindrome_2(s))

s = "abca"
print(valid_palindrome_2(s))

s = "abc"
print(valid_palindrome_2(s))

s = "acbca"
print(valid_palindrome_2(s))


