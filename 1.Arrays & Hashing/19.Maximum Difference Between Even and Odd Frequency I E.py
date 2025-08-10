# You are given a string s consisting of lowercase English letters.
# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.

 
# Example 1:
# Input: s = "aaaaabbc"
# Output: 3
# Explanation:
# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.


# Example 2:
# Input: s = "abcabcab"
# Output: 1
# Explanation:
# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.
 

# Constraints:
# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with an odd frequency and one with an even frequency.

def maximum_difference(s):
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord("a")] += 1

    max_odd = float("-inf")
    min_even = float("inf")

    for count in freq:
        if count > 0:
            if count % 2 == 1:
                if count > max_odd:
                    max_odd = count
            else:
                if count < min_even:
                    min_even = count
    return max_odd - min_even


s = "abcabcab"
print(maximum_difference(s))

s = "aaaaabbc"
print(maximum_difference(s))
