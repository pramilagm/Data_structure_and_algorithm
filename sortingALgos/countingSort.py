def countingSort(arr):
    n = len(arr)
    count = [0]*10
    output = [0]*n
    for i in range(0, n):
        # count[arr[0]] +=1  count[4] +=1 count =[0,0,0,0,1,0,0,0,0,0]
        count[arr[i]] += 1
        # count[arr[1]] +=1 count[2] +=1 count = [0,0,1,0,1,0,0,0,0,0]
    for i in range(1, 10):  # [0,1,2,2,1,0,0,0,1,0,0]
        count[i] = count[i]+count[i-1]  # [0,1,2, 4, 6,6,6,7,7,7]
    i = n - 1
    while i >= 0:
        # i =6 arr[6] output[count[arr[6]]-1] = output[count[1]-1] = output[1-1] output[0] = 1
        # i =5 output[count[arr[5]]-1] = output[count[3]-1] = output[5-1] output[4] = 3
        # i=4 output[count[arr[4]]-1] = output[count[3]-1] = output[4-1] output[3] = 3
        # i= 3 # output[count[arr[3]]-1] = output[count[8]-1] = output[7-1]  output[6] = 8
        # i=2 output[count[arr[2]]-1] = output[count[2]-1] = output[3-1]  output[2] = 2
        # i =1 output[count[arr[1]]-1] = output[count[2]-1] = output[2-1]  output[1] = 2
        # i= 0 output[count[arr[0]]-1] = output[count[4]-1] = output[6-1]   output[5] = 4
        #output  =  [1,2,2,3,3,4,8]
        # arr[0] =4

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
