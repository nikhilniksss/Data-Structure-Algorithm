# binary search using recursion

def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    result = helper(arr,target,left,right) # will perform all the recursion task
    return result

def helper(arr,target,left,right):
    if left > right:
        return -1
    mid = (left + right)//2
    mid_ele = arr[mid]

    if mid_ele == target:
        return mid
    elif mid_ele > target:
        right = mid - 1
        result = helper(arr,target,left,right)
        return result
    else:
        left = mid + 1
        result = helper(arr,target,left,right)
        return result

arr = [2,4,5,7,9,10,17,32,88,99]
target = 99

# calling function

print(binary_search(arr,target))

