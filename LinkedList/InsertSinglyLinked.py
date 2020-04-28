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

    def addFront(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def addInBetween(self, prev_node, new_data):
        if prev_node is None:
            print('The previous node must be LinkedList')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def addInLast(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node

    def printList(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thurs")

list.head.next = e2
e2.next = e3
list.addFront("Sun")
list.addFront('Saturday')
print('----------')
list.addInBetween(e2, 'wednesdays')
list.printList()
list.addInLast('Friday')
list.printList()
