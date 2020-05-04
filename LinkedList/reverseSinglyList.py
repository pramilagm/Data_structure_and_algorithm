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

    def insertElement(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            curent_node = self.head
            while True:
                if curent_node.next is None:
                    break
                curent_node = curent_node.next
            curent_node.next = new_node

    def printList(self):

        if self.head is None:
            print('List is Empty')
        printValue = self.head
        while printValue is not None:
            print(printValue.data)
            printValue = printValue.next

# reversing a list

    def reverseList(self):
        previousNode = None
        currentNode = self.head
        nextNode = self.head
        while nextNode is not None:
            nextNode = nextNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode
        self.head = previousNode


list = LinkedList()
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node('5')
list.insertElement(node1)
list.insertElement(node2)
list.insertElement(node3)
list.insertElement(node4)
list.insertElement(node5)
list.reverseList()
list.printList()
