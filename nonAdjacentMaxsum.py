
# O(n) space complexity and O(n) time compexity


def nonAjdacentSum(arr):
    if len(arr) is None:
        return

    if len(arr) == 1:
        return arr[0]
    maxSums = arr[:]
    maxSums[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2]+arr[i])
    return maxSums[-1]


arr = [10, 12, 9, 45, 7, 5]
print(nonAjdacentSum(arr))

# O(1) space complexity and O(n) time complexity more optimal way


def nonAjdacentMaxSUm(arr):
    if len(arr) is None:
        return

    if len(arr) == 1:
        return arr[0]
    second = arr[0]
    first = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        current = max(first, second + arr[i])
        second = first
        first = current
    return first
