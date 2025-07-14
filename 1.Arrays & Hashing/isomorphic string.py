# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. 
# No two characters may map to the same character, but a character may map to itself.


# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:

# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false
# Explanation:
# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

def isomorphic(s,t):
    pattern_s = []
    pattern_t = []

    for c in s:
        pattern_s.append(s.index(c))

    for c in t:
        pattern_t.append(t.index(c))

    return pattern_s == pattern_t

s = "egg"
t = "add"
print(isomorphic(s,t))

s = "foo"
t = "bar"
print(isomorphic(s,t))

s = "paper"
t = "title"
print(isomorphic(s,t))