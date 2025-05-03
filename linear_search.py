# linear search algorithm

arr = [5,3,1,9,2]
target = 9

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search(arr,target))