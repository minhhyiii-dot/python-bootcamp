class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        if root.left is None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    elif value > root.value:
        if root.right is None:
            root.right = Node(value)
        else:
            insert(root.right, value)
    else:
        return root
    return root

def find_max(root):
    if root is None:
        return None
    while root.right is not None:
        if root.right is not None:
            root = root.right
        else:
            return root.value

def search(root, value):
    if 
def main():
    root = None

    while True:
        print("\n--- BST Management")
        print("1. Insert Node")
        print("2. Find Maximum")
        print("3. Search Node")
        print("4. Delete Node")
        print("5. Exit")

        menu_choice = int(input("Your Choice: "))

        if menu_choice == 5:
            print("Existing program...")
            break

        if menu_choice == 1:
            value = int(input("Enter value: "))
            root = insert(root, value)
            print("Insertion completed")

        if menu_choice == 2:
            print(find_max(root))
if __name__ == "__main__" :
    main()