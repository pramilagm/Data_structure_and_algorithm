def addString(list):
    result = ''
    for num in range(0, len(list)):
        newNum = list[num].split('  ,')
        print(newNum)
    return result


list = ['12', '163', '44', '558']
print(addString(list))
