class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def findHeight(root):
    if root:
        return 1 + max(findHeight(root.left), findHeight(root.right))
    else:
        return -1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(findHeight(root))
