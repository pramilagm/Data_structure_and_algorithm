class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DDL:
    def __init__(self):
        self.head = None

    def push(self, new_node):
        current_node = self.head
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        current_node.prev = current_node

    def printList(self):
        printVal = self.head
        if self.head is None:
            print('List is empty')
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = DDL()
val1 = Node('A')
val2 = Node('B')
val3 = Node('C')
val4 = Node('D')
list.push(val1)
list.push(val2)
list.push(val3)
list.push(val4)
list.printList()
