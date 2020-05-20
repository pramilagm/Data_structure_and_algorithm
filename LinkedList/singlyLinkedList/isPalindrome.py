class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = None(data)
        if self.head is None:
            self.head = newNode
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = newNode

    def isPalindrome(self):
        left = self.head
        right = self.head
        while right.next is not None:
            right = right.next
        while right != left:
            if left.data != right.data:
                return False
            left = left.next
            prevNode = right
