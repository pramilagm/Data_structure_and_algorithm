def countingSort(arr):
    n = len(arr)
    count = [0]*10
    output = [0]*n
    for i in range(0, n):
        count[arr[i]] += 1
    for i in range(0, 10):
        count[i] = count[i]+count[i-1]
    i = n - 1
    while i >= 0:
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, n):
        arr[i] = output[i]
    return arr


data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
