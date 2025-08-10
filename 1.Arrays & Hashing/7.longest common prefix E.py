# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longest_commom_prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    result = ""
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            break
        result += first[i]
    return result

strs = ["dog","racecar","car"]
print(longest_commom_prefix(strs))

strs = ["flower","flow","flight"]
print(longest_commom_prefix(strs))