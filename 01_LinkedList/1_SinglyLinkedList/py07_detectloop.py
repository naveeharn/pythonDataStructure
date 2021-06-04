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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist = LinkedList()

print("\nlinkedlist")

for i in range(0,4):
    linkedlist.push(i)

linkedlist.print_list()

print(linkedlist.check_detectloop_set())
linkedlist.head.next.next.next.next = linkedlist.head
print(linkedlist.check_detectloop_set())

print()




class LinkedListHeadTail:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, new_data):
        current = self.tail
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        current.next = new_node
        self.tail = new_node
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head == None:
            self.tail = new_node
        self.head = new_node

    def check_detectloop_headtail(self):
        current = self.head
        tail = self.tail
        while current:
            if(current == tail.next):
                print(current.data)
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist_headtail = LinkedListHeadTail()

print("\nlinkedlist_headtail")

linkedlist_headtail.append(11)

for i in range(0,10):
    linkedlist_headtail.push(i)

linkedlist_headtail.append(10)

linkedlist_headtail.print_list()

print()

print(linkedlist_headtail.check_detectloop_headtail())

print()

linkedlist_headtail.tail.next = linkedlist_headtail.head

print(linkedlist_headtail.check_detectloop_headtail())

    

