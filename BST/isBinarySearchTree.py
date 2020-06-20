class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_binary_search_tree(root):
    return isBinaryUtl(root, None, None)


def isBinaryUtl(root, left, right):
    if root is None:
        return True
    if left != None and root.data <= left.data:
        return False
    if right != None and root.data >= right.data:
        return False
    return isBinaryUtl(root.left, left, root) and isBinaryUtl(root.right, root, right)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)

#      4
#     2   6
#   1   3 5  7
print(check_binary_search_tree(root))
