class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node

    # Utility function to print it the linked LinkedList

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def cycleDetect(self):
        slow = self.head
        fast = self.head
        while (slow and fast and fast.next):
            slow = slow.next
            fast = fast.next
            if slow == fast:
                return True
        return False


llist = LinkedList()
llist.head = Node(5)
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
# Create a loop for testing
llist.head.next.next.next.next = llist.head
print(llist.cycleDetect())
# llist.printList()

# Time complexity: O(n).
# Only one traversal of the loop is needed.
# Auxiliary Space: O(1).
# There is no space required.
