class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if value < root.value:
        root.left = Node(value)
    elif value > root.value:
        root.right = Node(value)
    else:
        return root

root = Node(9)
insert(root, 20)
insert(root, 2)
insert(root, 7)
insert(root, 9)

print(Node(9))