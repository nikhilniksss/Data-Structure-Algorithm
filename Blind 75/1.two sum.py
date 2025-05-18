# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def two_sum(nums):
    store = {}
    for i in range(len(nums)):
        if nums[i] in store:
            return [store[nums[i]],i]
        else:
            store[target-nums[i]] = i


nums = [2,7,11,15]
target = 9

print(two_sum(nums))

nums = [3,2,4]
target = 6
print(two_sum(nums))

nums = [3,3]
target = 6
print(two_sum(nums))
