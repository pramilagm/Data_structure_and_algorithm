class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode = currentNode.next
            currentNode.next = newNode

    def length(self):
        len = 0
        currentNode = self.head
        while currentNode.next is None:
            len += 1
            currentNode = currentNode.next
        return len

    def convertArr(self):
        len = self.length()
        arr = []
        currentNode = self.head
        while currentNode is not None:
            arr.append(currentNode.data)
            currentNode = currentNode.next
        print(arr)

    def printList(self):
        if self.head is None:
            print('List is empty')
            return
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = LinkedList()
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
list.push(node1)
list.push(node2)
list.push(node3)
list.printList()
list.convertArr()
