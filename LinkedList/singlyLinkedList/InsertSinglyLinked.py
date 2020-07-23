class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class


class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None

    def lenList(self):
        len = 0
        current_node = self.head
        while current_node is not None:
            len += 1
            current_node = current_node.next
        return len

    def addFront(self, new_node):
        temp = self.head
        self.head = new_node
        new_node.next = temp
        del temp
        # new_node.next = self.head
        # self.head = new_node

    def addInBetween(self, prev_node, new_data):

        if prev_node is None:
            print('The previous node must be LinkedList')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def addAt(self, new_node, position):
        if position < 0 or position > self.lenList():
            print('invalid position')
            return

        if position is 0:
            self.addFront(new_node)
            return
        current_node = self.head
        current_position = 0
        while True:
            if current_position == position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

    def addInLast(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node

    def deleteFromBeg(self):

        if self.head.next is None:
            self.head = None
        runner = self.head
        self.head = runner.next

    def deleteEnd(self):
        curent_node = self.head
        while curent_node.next is not None:
            previous_node = curent_node
            curent_node = curent_node.next
        previous_node.next = None

    def deleteAt(self, position):
        if position < 0 or position >= self.lenList():
            print('Invalid positon')
            return
        if self.isListEmpty() is False:
            if position is 0:
                self.deleteHead()
                return
            currentNode = self.head
            currentPosition = 0
            while True:
                if currentPosition == position:
                    previousNode.next = currentNode.next
                    currentNode.next = None
                    break
                previousNode = currentNode
                currentNode = currentNode.next
                currentPosition += 1

    def printList(self):
        if self.head is None:
            print('List is empty')
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = LinkedList()
list.head = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Thurs")
# e4 = Node('June')
# e5 = Node('Sun')
# e6 = Node('Saturday')
# list.head.next = e2
# e2.next = e3
# list.addAt(e4, 0)
# list.addFront(e5)
# list.addFront(e6)
# print('----------')
# list.addInBetween(e2, 'wednesdays')

# # j
# list.printList()
list.addInLast('Friday')
list.addInLast('Saturday')
# # list.printList()
# print('////')
# list.deleteFromBeg()
# list.deleteEnd()
# list.deleteEnd()
# list.deleteAt(4)
list.printList()

# result = 0
# arr = [1, 2, 3]
# for i in arr:
#     result = result*i
# print(result)
