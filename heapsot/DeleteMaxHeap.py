def heapify(arr, i):
    largest = i
    l = 2*i+1
    r = 2*2 + 2
    if l < len(arr) and arr[l] > arr[largest]:
        largest = l

    if r < len(arr) and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)


def deleteHeapNode(arr):
    deletedNode = arr[0]
    lastnode = len(arr)-1
    lastnode = deletedNode
    n = len(arr)-1
    heapify(arr, n-1)


arr = [10, 5, 3, 2, 4]
deleteHeapNode(arr)
n = len(arr)

for i in range(n):
    print("%d" % arr[i])
