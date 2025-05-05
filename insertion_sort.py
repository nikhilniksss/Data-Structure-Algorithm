# insertion sort algorithm

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        last = i - 1

        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1

        arr[last + 1] = key


arr = [5,4,3,2,1]
insertion_sort(arr)
print(arr)