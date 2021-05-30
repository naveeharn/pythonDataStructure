
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def length_loop(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def length_recursive(self,current):
        if not current:
            return 0
        return 1 + self.length_recursive(current.next)

    def length_recursive_short(self):
        return self.length_recursive(self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()


linkedlist = LinkedList()

for i in range(0,10):
    linkedlist.push(i)

print(linkedlist.length_loop())
print(linkedlist.length_recursive(linkedlist.head))
print(linkedlist.length_recursive_short())
linkedlist.print_list()
