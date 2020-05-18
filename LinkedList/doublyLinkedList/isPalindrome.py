class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DDL:
    def __init__(self):
        self.head = None

    def isPalindrome(self):
        pass

    def push(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.head.prev = None
            return
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode
        newNode.prev = currentNode

    def isPalindrome(self):
        left = self.head
        right = self.head
        while right.next is not None:
            right = right.next
        while left != right:
            if left.data != right.data:
                return False

            left = left.next
            right = right.prev
        return True


list = DDL()
list.push('L')
list.push('E')
list.push('V')
list.push('E')
list.push('L')
list1 = DDL()
list1.push('r')
list1.push('a')
list1.push('m')
print(list.isPalindrome())
print(list1.isPalindrome())
