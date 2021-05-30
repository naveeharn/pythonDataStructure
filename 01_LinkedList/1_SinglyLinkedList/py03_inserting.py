
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, previous_node, new_data):
        if previous_node is None:
            print("The given previous node must in LinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return 
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node
        new_node.next = None

    def print_list(self):
        current = self.head
        while(current):
            print(current.data,end=" ")
            current = current.next
        print()


linkedlist = LinkedList()

linkedlist.append(10)

linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
linkedlist.push(4)

linkedlist.print_list()

linkedlist.insert_after_node(linkedlist.head.next,5)

linkedlist.print_list()

linkedlist.insert_after_node(None,7)

linkedlist.print_list()

linkedlist.append(8)
linkedlist.append(9)

linkedlist.print_list()