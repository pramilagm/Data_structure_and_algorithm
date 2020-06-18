# Write a function that takes in a non-empty array of distinct / unique integers representging a targer sum.
# The function should find all triplets in the array tha sum up to the target sum and return a two dimensional array of all these
# triplets. The numbers in each triplet shoul be ordered in ascending order, and the triplets themselves
# should be ordered in ascending order with respect to the numbers that they hold.

# If no three numbers sum up to the target sum, the function should return an empty array.

# o(n2)|time complexity and o(n) space complexity


def three_sum(arr, sum):
    arr.sort()
    target_arr = []
    for i in range(0, len(arr)-1):
        left = i+1
        right = len(arr)-1
        while left < right:
            currentSum = arr[i] + arr[left]+arr[right]
            if currentSum == sum:
                target_arr.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif currentSum < sum:
                left += 1
            elif currentSum > sum:
                right -= 1
    return target_arr


A = [1, 4, 45, 6, 10, 8]
sum = 22
print(three_sum(A, sum))
