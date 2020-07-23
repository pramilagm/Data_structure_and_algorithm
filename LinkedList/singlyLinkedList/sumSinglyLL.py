class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_node(self):
        if self.head is None:
            print("list is empty")
        printVal = self.head
        while printVal is not None:
            print(printVal.value)
            printVal = printVal.next
        # print(self.value)
        # if self.next is not None:
        #     self.next.print_node()

    def length_ll(self):
        node = self
        length = 0
        while node is not None:
            node = node.next
            length += 1
        return length

    def length_recur(self):
        if self.next is None:
            return 1
        return 1 + self.next.length_recur()
# sum

    def sum_iter(self):
        total = 0
        node = self.head
        while node.next:
            total += node.value
            node = node.next
        # needs to add the last node value since it will terminate the while loop once it found node.next so add the last node after out of the while loop
        total += node.value
        return total

    def sum_rec(self):
        if self.next is None:
            return self.value
        return self.value + self.next.sum_rec()

    def append(self, value):
        current = self.head
        if self.head is None:
            self.head = Node(value)
        while current.next is not None:
            current = current.next
        current.next = Node(value)

    def append_rec(self, value):
        if self.next is None:
            self.next = Node(value)
        else:
            self.next.append_rec(value)

    def max_rec(self):
        if self.next is None:
            return self.value

        return max(self.value, self.next.max_rec())

    def insert(self, value):
        if value < self.value:
            node = Node(value)
            node.next = self
            return node

        if self.next is None:
            self.next = Node(value)
        else:
            self.next = self.next.insert(value)
        return self

    def remove_rec(self, target):
        if self.next is not None:
            self.next = self.next.remove(target)
        if target == self.value:
            return self.next
        return self

    def returnkth(self, k):
        slow = self
        fast = self.next
        for i in range(k):
            if fast is not None:
                fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow


# # TEST #
# llist = Node(3)
# llist.append(1)
# llist.append(8)
# llist.append(2)
# print(llist.sum_rec())
# print(llist.sum_iter())
llist = LinkedList()
llist.head = Node(5)
# llist.append(1)
llist.append(2)
llist.append(3)
print(llist.sum_iter())
print(llist.length_recur())
# llist.print_node()
