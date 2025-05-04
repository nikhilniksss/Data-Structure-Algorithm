# selection sort algorithm

def selection_sort(arr):
    for i in range(0,len(arr)):
        min_x = i

        for item in range(i+1,len(arr)):
            if arr[item] < arr[min_x]:
                min_x = item

        arr[i], arr[min_x] = arr[min_x],arr[i]


arr = [20,12,10,15,2]
selection_sort(arr)
print(arr)