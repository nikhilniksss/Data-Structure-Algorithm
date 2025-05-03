# binary search algorithm

arr = [2,4,5,7,9,10,17,32,88,99]
target = 10

def binary_search(arr,target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left+right)//2
        mid_element = arr[mid]

        if mid_element == target:
            return mid
        elif mid_element > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# calling function

print(binary_search(arr,target))
