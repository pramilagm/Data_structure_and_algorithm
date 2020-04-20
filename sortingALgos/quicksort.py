def partition(arr, low, high):
    pivot = arr[high]
    pIndex = low-1
    for i in range(low, high):
        if arr[i] <= pivot:
            pIndex += 1
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
    arr[pIndex+1], arr[high] = arr[high], arr[pIndex+1]
    return pIndex+1


def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size-1)
print('Sorted Array in Ascending Order:')
print(data)
