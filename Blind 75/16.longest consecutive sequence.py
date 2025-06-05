#Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
#You must write an algorithm that runs in O(n) time.


# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# Example 3:
# Input: nums = [1,0,1,2]
# Output: 3

def longest_sequence(nums):
    numSet = set(nums)
    longest = 0

    for n in numSet:
        if n - 1 not in numSet:
            current_num = n
            current_streak = 1

            while current_num + 1 in numSet:
                current_num += 1
                current_streak += 1
            longest = max(longest,current_streak)
    return longest


nums = [100,4,200,1,3,2]
print(longest_sequence(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_sequence(nums))

nums = [1,0,1,2]
print(longest_sequence(nums))