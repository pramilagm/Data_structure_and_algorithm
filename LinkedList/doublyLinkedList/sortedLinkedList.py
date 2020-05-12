class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class DDL:
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):
        if self.head is None:
            self.head = new_node
            self.head.prev = None
            return
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node
            return
        else:
            current_node = self.head
            while current_node.next is not None and current_node.next.data < new_node.data:
                current_node = current_node.next
            new_node.next = current_node.next

            if current_node.next is not None:
                new_node.next.prev = new_node
            current_node.next = new_node
            new_node.prev = current_node

    def printList(self):
        prinVal = self.head
        while prinVal is not None:
            print(prinVal.data)
            prinVal = prinVal.next


list = DDL()
node1 = Node(3)
node2 = Node(7)
node3 = Node(2)
node4 = Node(1)
list.sortedInsert(node1)
list.sortedInsert(node2)
list.sortedInsert(node3)
list.sortedInsert(node4)

list.printList()
