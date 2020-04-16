def heapify(arr, i):
    # parenta node
    if(i == 0):
        return

    p = (i-1)//2

    if (arr[i] > arr[p]):
        arr[i], arr[p] = arr[p], arr[i]
        heapify(arr, p)


def insertHeap(arr, ele):
    arr.append(ele)
    heapify(arr,  len(arr)-1)


arr = [10, 5, 3, 2, 4]
ele = 15
n = len(arr)-1
insertHeap(arr, ele)
n = len(arr)
print("Inserted element in maximum heap ")
for i in range(n):
    print("%d" % arr[i])
