# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

def top_k(nums,k):
    bucket = [[] for _ in range(len(nums) + 1)]
    frequencyMap = {}

    for n in nums:
        if n not in frequencyMap:
            frequencyMap[n] = 1
        else:
            frequencyMap[n] += 1

    for key,frequency in frequencyMap.items():
        bucket[frequency].append(key)

    result = []

    for i in reversed(range(len(bucket))):
        if bucket[i]:
            for value in bucket[i]:
                if len(result) < k:
                    result.append(value)
                else:
                    return result
    return result


nums = [1,1,1,2,2,3]
k = 2
print(top_k(nums,k))


nums = [1]
k = 1
print(top_k(nums,k))