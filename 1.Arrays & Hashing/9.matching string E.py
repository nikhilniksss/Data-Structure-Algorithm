# Given an array of string words, return all strings in words that are a substring of another word.
# You can return the answer in any order.


# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.


# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".


# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


def matching_string(words):
    res = []

    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            if words[i] in words[j]:
                res.append(words[i])
    return list(set(res)) 


words = ["mass","as","hero","superhero"]
print(matching_string(words))


words = ["leetcode","et","code"]
print(matching_string(words))

words = ["blue","green","bu"]
print(matching_string(words))

words = ["leetcoder","leetcode","od","hamlet","am"]
print(matching_string(words))

