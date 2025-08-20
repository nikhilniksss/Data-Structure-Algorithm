# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

def top_k(nums,k):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x,0) + 1

    buckets = [[] for _ in range(len(nums) + 1)]
    for x, c in freq.items():
        buckets[c].append(x)

    res = []
    for c in range(len(nums),0,-1):
        for x in buckets[c]:
            res.append(x)
            if len(res) == k:
                return res
    return res

nums = [1,1,1,2,2,3]
k = 2
print(top_k(nums,k))

nums = [1]
k = 1
print(top_k(nums,k))
    