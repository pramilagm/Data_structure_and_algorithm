class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    # def push(self, data):
    #     newNode = None(data)
    #     if self.head is None:
    #         self.head = newNode
    #     currentNode = self.head
    #     while currentNode.next is not None:
    #         currentNode = currentNode.next
    #     currentNode.next = newNode

    def isPalindrome(self):
        string = ''
        currentNode = self.head
        while currentNode.next is not None:
            string += currentNode.data
            currentNode = currentNode.next
        return palindrome(string)

    def palindrome(self, string):
        i = 0
        j = len(string)-1
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True


list = SLL()
isPal = list.palindrome('racecar')
isPal1 = list.palindrome('hello')
print(isPal)
print(isPal1)
