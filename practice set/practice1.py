###### Problem 1 #######

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

print("Problem 1 output:")

nums = [1,2,3,1]
print(contains_duplicate(nums))

nums = [1,1,1,1]
print(contains_duplicate(nums))

nums = [1,2,3,4]
print(contains_duplicate(nums))


###### Problem 2 #######

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1

    for val in count:
        if val != 0:
            return False
    return True

print("Problem 2 output:")
s = "anagram"
t = "nagaram"
print(valid_anagram(s,t))

s = "rat"
t = "car"
print(valid_anagram(s,t))