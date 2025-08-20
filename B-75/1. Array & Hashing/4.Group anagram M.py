# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

def group_anagram(strs):
    anagrams = {}
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1

        key = tuple(count)
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(strs))

strs = [""]
print(group_anagram(strs))
