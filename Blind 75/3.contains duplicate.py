# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.


def contains_duplicate(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False

nums = [1,2,3,1]
print(contains_duplicate(nums))


nums = [1,2,3,4]
print(contains_duplicate(nums))


nums = [1,1,1,3,3,4,3,2,4,2]
print(contains_duplicate(nums))

