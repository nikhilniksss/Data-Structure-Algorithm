# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome 
# that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 
# Example 1:
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# Example 2:
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.


def longest_palindrome(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    length = 0
    odd_length = False

    for count in freq.values():
        length += (count // 2) * 2
        if count % 2 == 1:
            odd_length = True
    
    if odd_length:
        length += 1

    return length

s = "abccccdd"
print(longest_palindrome(s))