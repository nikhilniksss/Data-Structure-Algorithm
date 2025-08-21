# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums 
# except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

 
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

## brute force

def product_self(nums):
    n = len(nums)
    ans = [1] * n
    for i in range(n):
        product = 1
        for j in range(n):
            if j != i:
                product *= nums[j]
        ans[i] = product
    return ans

nums = [1,2,3,4]
print(product_self(nums))