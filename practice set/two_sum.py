# two sum

# this has complexity of O(n^2)
target = 18
nums = [2,7,11,15]
for i in nums:
    for j in nums:
        if i + j == target:
            print(i,j)


# optimized one with O(n)

def two_sum(nums,target):
    store = {}
    for i in range(len(nums)):
        if nums[i] in store:
            return [store[nums[i]],i]
        else:
            store[target-nums[i]] = i

target = 9
nums = [2,7,11,15]
print(two_sum(nums,target))

target = 18
nums = [2,7,11,15]
print(two_sum(nums,target))
