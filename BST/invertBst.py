class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def invertBst(root):
    if root is None:
        return root
    else:
        temp = root
        invertBst(root.left)
        invertBst(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end='. ')
        inOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inOrder(root)
invertBst(root)
print('afer inverse the tree')
inOrder(root)
#     1
#    /\
#   2  5
#   /\
#
