# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative 
# positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


def is_subsequence(str1,str2):
    itr1, itr2 = 0, 0
    while itr1 < len(str1) and itr2 < len(str2):
        if str1[itr1] == str2[itr2]:
            itr1 += 1
            itr2 += 1
        else:
            itr2 += 1
    return itr1 == len(str1)


s = "abc"
t = "ahbgdc"
print(is_subsequence(s,t))


s = "axc"
t = "ahbgdc"
print(is_subsequence(s,t))
