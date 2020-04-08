def bubbleSOrt(arr):
    n = len(arr)
    for j in range(n):
        swapped = False
        for i in range(0, n-j-1):

            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True

        if(swapped == False):
            break

    return arr


arr = [13, 8, 3, 2, 1]
print(bubbleSOrt(arr))
