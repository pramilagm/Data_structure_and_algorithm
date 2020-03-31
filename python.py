def compareTriplets(a, b):

    return map(
        lambda t: sum([x > y for x, y in zip(*t)]),
        ((a, b), (b, a))
    )


x = (4, 5, 6)
y = (3, 7, 8)
print(list(compareTriplets(x, y)))

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)
print(list(mapped))


def test(*t):
    for x, y in zip(*t):
        print(x, y)


def aVeryBigSum(ar):
    sum = 0
    carry = 0
    for num in ar:
        sum += num
    return sum


arr = [9999, 9999, 10000]
print(aVeryBigSum(arr))
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]
i, j = 0, len(arr)-1
while(i < len(arr)):
    print(arr[i][j])
    i += 1
    j -= 1


def plusMinus(arr):
    p, n, z = 0, 0, 0
    for num in arr:
        if num > 0:
            p += 1
        if num < 0:
            n += 1
        if num == 0:
            z += 1
    positiveFraction = float(p/len(arr))
    print('{0:.6f}'.format(p/len(arr)))
    print('{0:.6f}'.format(n/len(arr)))
    print('{0:.6f}'.format(z/len(arr)))


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)


def staircase(n):
    printstaircase = ''
    for i in range(1, n+1):
        if (i < n):
            printstaircase += ' '*(n-i) + '#'*(i) + '\n'
        else:
            printstaircase += '#'*i
    print(printstaircase)


staircase(4)


def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    arr.sort()
    for i in range(0, len(arr)-1):
        minSum += arr[i]
    for i in range(0, len(arr)):
        maxSum += arr[i]
    return minSum, maxSum


arr = [1, 2, 3, 4, 5]
print(miniMaxSum(arr))


def birthdayCakeCandles(ar):
    return ar.count(max(ar))


    # tallest_candle = new_ar[len(new_ar)]
    # countTallestCandle =1
    # for candle in new_ar:
    #     if(tallest_candle==candle):
    #        countTallestCandle += 1
    # return countTallestCandle
arr = [3, 2, 1, 3]
print(birthdayCakeCandles(arr))


def timeConversion(s):
    hour = int(s[0:2])
    if "AM" in s:
        if hour == 12:
            hour = "0"
            s = str(hour) + s[2:-2]
            return s
        else:
            return s.replace("AM", "")
    else:
        if(hour == 12):
            return s.replace("PM", "")
        else:
            hour += 12
            s = str(hour) + s[2:-2]
            return s


time = '07: 05: 45PM'
print(timeConversion(time))


def balancedSums(arr):
    mid = int(len(arr)/2)
    sumLeft = 0
    sumRight = 0

    for i in range(0, mid):
        sumLeft += arr[i]
    for i in range(mid+1, len(arr)):
        sumRight += arr[i]
    if(sumLeft == sumRight):
        return True
    else:
        return False


ar = [1, 1, 4, 1, 1]
print(balancedSums(ar))