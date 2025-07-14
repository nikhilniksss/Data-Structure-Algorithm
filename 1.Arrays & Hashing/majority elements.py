# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majority_elements(nums):
    count = {}
    maxCount = len(nums) // 2

    for n in nums:
        count[n] = count.get(n,0) + 1
        if count[n] > maxCount:
            return n

nums = [3,2,3]
print(majority_elements(nums))

nums = [2,2,1,1,1,2,2]
print(majority_elements(nums))


