# bubble sort algorithm

def bubble_sort(arr):
    for iter in range(len(arr)):
        for index in range(0,len(arr)-1-iter):
            if arr[index] > arr[index + 1]:
                arr[index],arr[index + 1] = arr[index + 1],arr[index]

arr = [29,10,14,37,14]
bubble_sort(arr)
print(arr)