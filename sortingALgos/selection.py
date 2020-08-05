

def selectionSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]


arr = [8, 4, 3, 5, 9, 1, 6]
selectionSort(arr)
for i in range(0, len(arr)):
    print(arr[i])
# Best Case [ O(N2) ]. Also O(N) swaps.
# Worst Case: Reversely sorted, and when inner loop makes maximum comparison. [ O(N2) ] . Also O(N) swaps.
# Average Case: [ O(N2) ] . Also O(N) swaps
