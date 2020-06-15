class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node

    def printList(self):
        if self.head is None:
            print('SLL is empty')
        printNode = self.head
        while printNode:
            print(printNode.data)
            printNode = printNode.next

    def rotate(self, k):
        if k == 0:
            return

        # Let us understand the below code for example k = 4
        # and list = 10->20->30->40->50->60
        current = self.head

        # current will either point to kth or NULL after
        # this loop
        # current will point to node 40 in the above example
        count = 1
        while(count < k and current is not None):
            current = current.next
            count += 1

        # If current is None, k is greater than or equal
        # to count of nodes in linked list. Don't change
        # the list in this case
        if current is None:
            return

        # current points to kth node. Store it in a variable
        # kth node points to node 40 in the above example
        kthNode = current

        # current will point to lsat node after this loop
        # current will point to node 60 in above example
        while(current.next is not None):
            current = current.next

        # Change next of last node to previous head
        # Next of 60 is now changed to node 10
        current.next = self.head

        # Change head to (k+1)th node
        # head is not changed to node 50
        self.head = kthNode.next

        # change next of kth node to NULL
        # next of 40 is not NULL
        kthNode.next = None


list = SLL()
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node5 = Node(50)
list.push('10')
list.push('20')
list.push('30')
list.push('40')
list.push('50')
list.push('60')
list.printList()
print('------------')
list.rotate(4)
list.printList()
