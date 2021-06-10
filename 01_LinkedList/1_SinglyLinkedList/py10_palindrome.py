class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist = LinkedList()

linkedlist.push("r")
linkedlist.push("a")
linkedlist.push("d")
linkedlist.push("a")
linkedlist.push("r")

linkedlist.print_list()