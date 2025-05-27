# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

def maxAverage(nums,k):
    current_sum = 0
    for i in range(k):
        current_sum += nums[i]
        
    max_sum = current_sum

    start_index = 0
    end_index = k

    while end_index < len(nums):

        current_sum -= nums[start_index]
        start_index += 1

        current_sum += nums[end_index]
        end_index += 1

        max_sum = max(current_sum,max_sum)

    return max_sum/k


nums = [1,12,-5,-6,50,3]
k = 4
print(maxAverage(nums,k))

nums = [5]
k = 1
print(maxAverage(nums,k))

