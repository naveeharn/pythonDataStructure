class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedListSst:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def check_detectloop_set(self):
        print("check_detectloop_set")
        current = self.head
        element = set()
        while current:
            if current in element:
                print(current.data)
                return True
            element.add(current)
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current and not self.check_detectloop_set():  #warning condition
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist_set = LinkedListSst()

print("\nlinkedlist_set")

for i in range(0,4):
    linkedlist_set.push(i)

linkedlist_set.print_list()

print(linkedlist_set.check_detectloop_set())
linkedlist_set.head.next.next.next.next = linkedlist_set.head
linkedlist_set.print_list()                                 #warning condition
print(linkedlist_set.check_detectloop_set())

print()

print(" = = = = = = = = = = = = = = = = = = = = = = = = ")

class NodeWithFlag:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.flag = 0

class LinkedListFlag:
    def __init__(self) -> None:
        self.head = None
        self.isloop = False         #think myself

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.flag = 0
        new_node.next = self.head
        self.head = new_node

    def check_detectloop_flag(self):
        print("\ncheck_detectloop_flag")
        current = self.head
        while current:
            if current.flag:
                print(current.data)
                self.isloop = True  #think myself
                return True
            current.flag = 1
            current = current.next
        self.isloop = False         #think myself
        return False

    def print_list(self):
        current = self.head
        while current and not self.isloop:  #think myself
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist_flag = LinkedListFlag()

for i in range(0,4):
    linkedlist_flag.push(i)

print("\nlinkedlist_flag")

linkedlist_flag.print_list()

print(linkedlist_flag.check_detectloop_flag())

linkedlist_flag.head.next.next.next.next = linkedlist_flag.head

print(linkedlist_flag.check_detectloop_flag())

linkedlist_flag.print_list()


print(" = = = = = = = = = = = = = = = = = = = = = = = = ")

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedListFloydCycle:
    def __init__(self) -> None:
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def check_detectloop_floydcycle(self):
        print("\ncheck_detectloop_floydcycle")
        slow_current = self.head
        fast_current = self.head
        while slow_current and fast_current:
            slow_current = slow_current.next
            fast_current = fast_current.next.next
            if slow_current == fast_current:
                print(slow_current.data)
                return True
        return False

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist_floydcycle = LinkedListFloydCycle()

for i in range(0,4):
    linkedlist_floydcycle.push(i)

print("\nlinkedlist_floydcycle")
linkedlist_floydcycle.print_list()

print(linkedlist_floydcycle.check_detectloop_floydcycle())
linkedlist_floydcycle.head.next.next.next.next = linkedlist_floydcycle.head
print(linkedlist_floydcycle.check_detectloop_floydcycle())

linkedlist_floydcycle = LinkedListFloydCycle()

for i in range(0,4):
    linkedlist_floydcycle.push(i)

linkedlist_floydcycle.head.next.next.next = linkedlist_floydcycle.head
print(linkedlist_floydcycle.check_detectloop_floydcycle())



print(" = = = = = = = = = = = = = = = = = = = = = = = = ")

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

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
        print("\ncheck_detectloop_headtail")
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

print(linkedlist_headtail.check_detectloop_headtail())

linkedlist_headtail.tail.next = linkedlist_headtail.head

print(linkedlist_headtail.check_detectloop_headtail())



