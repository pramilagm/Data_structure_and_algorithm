def maxHeapify(arr, n, idx):
    largest = idx
    l = 2*idx+1
    r = 2*idx + 2
    if l < n and arr[idx] < arr[l]:
        largest = l
    else:
        largest = idx
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != idx:
        arr[idx], arr[largest] = arr[largest], arr[idx]
        maxHeapify(arr, n, largest)


def buildMaxHeap(arr, n):
    for i in range(n//2-1, -1, -1):
        maxHeapify(arr, n, i)


def mergeHeaps(merged, a, b, n, m):
    for i in range(n):
        merged[i] = a[i]
    for i in range(m):
        merged[n+i] = b[i]
    buildMaxHeap(merged, n+m)


a = [10, 5, 6, 2]
b = [12, 7, 9]
n = len(a)
m = len(b)
merged = [0]*(m+n)
mergeHeaps(merged, a, b, n, m)
for i in range(len(merged)):
    print(merged[i], end=" ")
