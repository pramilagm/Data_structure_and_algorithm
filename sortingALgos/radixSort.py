def countingSort(arr, p):
    count = [0]*10
    n = len(arr)
    output = [0]*n
    for i in range(0, n):
        count[arr[i]//p % 10] += 1
 # Calculate cummulative count
    for i in range(0, 10):
        count[i] = count[i] + count[i-1]
 # Place the elements in sorted order
    i = n-1
    while i >= 0:
        output[count[arr[i]//p % 10]-1] = arr[i]
        count[arr[i]//p % 10] -= 1
        i -= 1

    # copying the value to original array
    for i in range(0, n):
        arr[i] = output[i]


def radixSort(arr):

    # Find the maximum number to know number of digits
    max1 = max(arr)
    print(max1)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10


data = [121, 432, 564, 23, 1, 45, 788]
radixSort(data)
print(data)
