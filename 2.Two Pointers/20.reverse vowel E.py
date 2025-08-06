# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"


def reverse_vowel(s):
    vowel = {'a','e','i','o','u','A','E','I','O','U'}
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] not in vowel:
            left += 1
        elif s[right] not in vowel:
            right -= 1
        else:
            s[left], s[right] = s[right],s[left]
            left += 1
            right -= 1
    return "".join(s)


s = "IceCreAm"
print(reverse_vowel(s))

s = "leetcode"
print(reverse_vowel(s))