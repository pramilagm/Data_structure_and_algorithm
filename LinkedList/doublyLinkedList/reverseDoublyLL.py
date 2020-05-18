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
        new_node.prev = current_node

    def reverseDDL(self):
        current_node = self.head
        temp = None
        while current_node is not None:
            temp = current_node.prev

            current_node.prev = current_node.next
            current_node.next = temp
            current_node = current_node.prev
        if temp is not None:
            self.head = temp.prev

    def printList(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal = printVal.next


list = DDL()
node1 = Node(5)
node2 = Node(3)
node3 = Node(2)
node4 = Node(1)
list.push(node1)
list.push(node2)
list.push(node3)
list.push(node4)
list.reverseDDL()
list.printList()
