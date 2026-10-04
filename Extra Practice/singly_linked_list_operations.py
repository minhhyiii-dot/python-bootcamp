class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def find_position(self, x):
        current = self.head
        position = 1

        while current is not None:
            if current.data == x:
                return position

            current = current.next
            position += 1

        return -1

    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()

my_list = LinkedList()

my_list.insert_beginning(30)
my_list.insert_beginning(20)
my_list.insert_beginning(10)

my_list.insert_end(40)
my_list.insert_end(50)

print("Linked list:")
my_list.print_list()

x = int(input("Enter X: "))

position = my_list.find_position(x)

if position == -1:
    print(x, "is not in the list")
else:
    print(x, "is at position", position)