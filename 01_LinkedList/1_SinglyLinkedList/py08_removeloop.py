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

    def check_detectloop_set(self):
        current = self.head
        element = set()
        while current:
            if current in element:
                return True
            element.add(current)
            current = current.next
        return False

    def removeloop_set(self):
        previous = self.head
        current = self.head
        element = set()
        if current in element:
            current.next = None
            return
        element.add(current)
        current = current.next
        while current:
            if current in element:
                previous.next = None
                return
            element.add(current)
            previous = previous.next
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
linkedlist = LinkedList()

for i in range(0,4):
    linkedlist.push(i)

linkedlist.print_list()
print(linkedlist.check_detectloop_set())
linkedlist.head.next.next.next.next = linkedlist.head
print(linkedlist.check_detectloop_set())

linkedlist.removeloop_set()
linkedlist.print_list()
print(linkedlist.check_detectloop_set())