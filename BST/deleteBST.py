class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val <= node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def deleteNode(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = deleteNode(root.left, val)
    elif val > root.val:
        root.right = deleteNode(root.right, val)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = findMin(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    return root


def findMin(root):
    current = root
    if current.left is not None:
        current = current.left
    return current


r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

deleteNode(r, 50)

inOrder(r)
