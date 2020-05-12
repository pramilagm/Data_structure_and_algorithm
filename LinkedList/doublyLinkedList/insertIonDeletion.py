class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DDL:
    def __init__(self):
        self.head = None

    def lenList(self):
        len = 0
        current_node = self.head
        while current_node is not None:
            len += 1
            current_node = current_node.next
        return len

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

    def pushFront(self, new_node):
        new_node.next = self.head
        new_node.prev = None
        if self.head is None:
            self.head = new_node
            self.head.prev = None
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def addAt(self, pre_node, new_node):
        if pre_node is None:
            print('the given previous node is None ')
        new_node.next = pre_node.next
        pre_node.next = new_node
        new_node.prev = pre_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def addAtposition(self, position, new_node):
        if position <= 0 or position > self.lenList():
            print('invalid position')
            return
        if position is 1:
            self.pushFront(new_node)

            return

        index = 0
        current_node = self.head
        while index < position-2:
            current_node = current_node.next
            index += 1
        new_node.next = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def deleteFromBeg(self):
        if self.head.next is None:
            self.head = None
            return
        deleted_node = self.head
        self.head = deleted_node.next
        self.head.prev = None

    def deleteAtLast(self):
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next
        current_node.next = None

    def deleteAt(self, position):
        if position <= 0 or position > self.lenList():
            print('the position does not Exist')
        if position is 1:
            self.deleteFromBeg()
            return
        current_node = self.head
        index = 0
        while index < position:
            current_node = current_node.next
            index += 1
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

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
val5 = Node('z')
val6 = Node('F')
val7 = Node('M')

list.push(val1)
list.push(val2)
list.push(val3)
list.push(val4)
list.pushFront(val5)
list.addAt(val2, val6)
list.addAtposition(3, val7)
list.deleteFromBeg()
list.deleteFromBeg()
list.addAtposition(2, val1)

list.deleteAt(2)
list.deleteAtLast()
list.deleteAtLast()
list.printList()
