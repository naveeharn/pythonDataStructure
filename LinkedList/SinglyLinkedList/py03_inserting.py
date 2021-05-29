
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

    def print_list(self):
        current = self.head
        while(current != None):
            print(current.data,end=" ")
            current = current.next
        print()


linkedlist = LinkedList()

linkedlist.push(1)
linkedlist.push(2)
linkedlist.push(3)
linkedlist.push(4)

linkedlist.print_list()