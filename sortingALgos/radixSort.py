def countingSort(arr, p):
    count = [0]*10
    n = len(arr)
    output = [0]*n
    for i in range(0, n):
        count[arr[i]//p % 10] += 1  # arr = [1,121,23,432,45,564,788]

        # count[arr[0]//1%10] count[121%10]=  count[1] += 1     [0, 2,1,1,1,1,0,0,1,0,0]
        # count[arr[0]//10%10] count[121//10%10] =  count[12%10] = count[2]+=1   [1,0,2,1,1,0,1,0,1,0,0]

        # count[arr[0]//100%10] count[1//100%10] count[0] +=1      count = [3,1,0,0,1,1,0,1,0,0]

        # count[arr[1]//1%10] count[432%10]= count[2] +=1
        # count[arr[1]//10%10] count[1//10%10] =  count[0%10] = count[0]+=1
        # count[arr[1]//100%10] count[121//100%10] = count[1%10] = count[1] +=

        # count[arr[2]//1%10]  count[564%10] = count[4]+=1
        # count[arr[2]//10%10] count[432//10%10] =  count[43%10] = count[3]+=1
        # count[arr[2]//100%10] count[23//100%10] = count[0] = count[0] +=1

        # count[arr[3]//1%10]  count[23%10] = count[3]+=1
        # count[arr[3]//10%10] count[23//10%10] =  count[2%10] = count[2]+=1
        # count[arr[3]//100%10] count[432//100%10] = count[4%10] = count[4] +=1

        # # count[arr[4]//1%10]  count[1%10] = count[1]+=1
        # count[arr[4]//10%10] count[564//10%10] =  count[56%10] = count[6]+=1
        # count[arr[4]//100%10] count[45//100%10] count[0%10] = count[0]+=1

        # count[arr[5]//1%10]  count[45%10] = count[5]+=1
        # count[arr[5]//10%10] count[45//10%10] =  count[4%10] = count[4]+=1
        # count[arr[5]//100%10] count[564//100%10] = count[5%10] = count[5]+=1
        # count[arr[6]//1%10]  count[788%10] = count[8]+=1
        # count[arr[6]//10%10] count[788//10%10] =  count[78%10] = count[8]+=1
        # count[arr[6]//100%10] count[788//100%10] = count[7%10] = count[7]+=1
 # Calculate cummulative count
    for i in range(1, 10):
        # count = [0,2,3,4,5,6,6,6,7,7,7] [0,1,3,4,5,6,6,6,7,7,7]
        # count = [1,0,2,1,1,0,1,0,1,0,0] [1,1,3,4,5,5,6,6,7,7,7]
        #count = [3,1,0,0,1,1,0,1,0,0] [1,4,4,4,4,6,6,7,7,7]
                                        #   arr = [1,121,23,432,45,564,788]
        count[i] = count[i] + count[i-1]
        # Place the elements in sorted order
    i = n-1
    while i >= 0:

        output[count[arr[i]//p % 10]-1] = arr[i]

# ouput = [1,23,45,121,432,564,788]
        # output[count[arr[6]//100%10]] output[count[788//100%10]-1] output[count[7]-1] output[7-1] =output[6] = arr[6]=788
        #  output[count[arr[5]//100%10]-1] =  output[count[564//100%10]-1]  output[count[5]-1] output[6-1] output[5]= 564
        # output[count[arr[4]//100%10]-1] =  output[count[45//100%10]-1]  output[count[0]-1] output[3-1] output[2]= 45
        #  output[count[arr[3]//100%10]-1] =  output[count[432//100%10]-1]  output[count[4]-1] output[5-1] output[4]= 432
        # output[count[arr[2]//100%10]-1] =  output[count[23//100%10]-1]  output[count[0]-1] output[2-1] output[1]= 23
        # output[count[arr[1]//100%10]-1] =  output[count[121//100%10]-1]  output[count[1]-1] output[4-1] output[3]= 121
        # output[count[arr[0]//100%10]-1] =  output[count[1//100%10]-1]  output[count[0]-1] output[1-1] output[0]= 1

        count[arr[i]//p % 10] -= 1
        i -= 1
    # copying the value to original array
    for i in range(0, n):
        arr[i] = output[i]
        #arr = [121,1,432,23,564,45,788]
        #arr = [1,121,23,432,45,564,788]

        #arr = [1,23,45,121,432,564,788]


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
ar = [1, 3, 3, 3, 4, 4, 5, 5]
count = 0
for i in range(0, len(ar)-1):
    if ar[i] == ar[i+1]:
        count += 1
print(count)
