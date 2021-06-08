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
        print("\ncheck_detectloop_set")
        current = self.head
        element = set()
        while current:
            if current in element:
                return True
            element.add(current)
            current = current.next
        return False
        
    def check_detectloop_floydcycle(self):
        print("\ncheck_detectloop_floydcycle")
        slow_current = fast_current = self.head
        while slow_current and fast_current and fast_current.next:
            slow_current = slow_current.next
            fast_current = fast_current.next.next
            if slow_current == fast_current:
               return True
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

    def removeloop_floydcycle(self):
        print("\nremoveloop_floydcycle")
        if self.check_detectloop_floydcycle():
            previous = current = self.head
            # count the number of nodes in loop
            k = 1
            while previous.next != current:
                previous = previous.next
                k+=1

            previous = current = self.head
            for i in range(k):
                current = current.next
            
            while previous != current:
                previous = previous.next
                current = current.next

            while previous != current.next:
                current = current.next

            current.next = None
            return
        print("\n<!> removeloop_floydcycle is not working")

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

print("\n= = = = = = = = = = = = = = = = = = = = = = = = = = = = =\n")

linkedlist.print_list()
print(linkedlist.check_detectloop_floydcycle())
linkedlist.removeloop_floydcycle()
linkedlist.head.next.next.next.next = linkedlist.head
print(linkedlist.check_detectloop_floydcycle())
linkedlist.removeloop_floydcycle()
print(linkedlist.check_detectloop_floydcycle())