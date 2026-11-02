
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 1. Insert node
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

    return root


# 2. Find maximum value
def find_max(root):
    if root is None:
        return None

    while root.right is not None:
        root = root.right

    return root.value


# 3. Search node
def search(root, value):
    while root is not None:
        if value == root.value:
            return True
        elif value < root.value:
            root = root.left
        else:
            root = root.right

    return False


# 4. Delete node
def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        
        successor = root.right
        while successor.left is not None:
            successor = successor.left

        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root


def main():
    root = None

    while True:
        print("\n--- BST MANAGEMENT ---")
        print("1. Insert Node")
        print("2. Find Maximum")
        print("3. Search Node")
        print("4. Delete Node")
        print("5. Exit")

        try:
            menu_choice = int(input("Your Choice: "))
        except ValueError:
            print("Please enter a valid menu number.")
            continue

        if menu_choice == 5:
            print("Exiting program...")
            break

        if menu_choice in (1, 3, 4):
            try:
                value = int(input("Enter value: "))
            except ValueError:
                print("Please enter an integer.")
                continue

        if menu_choice == 1:
            if search(root, value):
                print("Value already exists in BST.")
            else:
                root = insert(root, value)
                print("Insertion completed.")

        elif menu_choice == 2:
            maximum = find_max(root)
            if maximum is None:
                print("BST is empty.")
            else:
                print("Maximum value:", maximum)

        elif menu_choice == 3:
            if search(root, value):
                print("Value exists in BST.")
            else:
                print("Value not found.")

        elif menu_choice == 4:
            if search(root, value):
                root = delete(root, value)
                print("Node deleted successfully.")
            else:
                print("Value not found. Nothing deleted.")

        else:
            print("Invalid choice. Choose 1-5.")


if __name__ == "__main__":
    main()
