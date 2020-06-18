
def heapify(arr, n, i):
    # Find largest among root and children

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n//2-1, -1, -1):

        heapify(arr, n, i)

    for i in range(n-1, -1, -1):
        # swap
        arr[i], arr[0] = arr[0], arr[i]

        # heapify root element
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7]
heapify(arr, len(arr), 0)
for i in range(len(arr)):
    print(arr[i])
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])


# for i in range(10, 0, -1):
#     print(i)
