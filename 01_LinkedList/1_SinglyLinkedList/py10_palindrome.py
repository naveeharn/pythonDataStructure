class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    
    def check_palindrome(self):
        print("check_palindrome",end=" ")
        head_current = self.head
        tail_current = self.tail
        while head_current:
            if head_current.data != tail_current.data:
                return False
            if head_current == tail_current or head_current.next == tail_current:
                return True
            current = head_current 
            head_current = head_current.next
            while current.next != tail_current:
                current = current.next
            tail_current = current
        return True

    def check_palindrome_stack(self):
        print("check_palindrome_stack",end=" ")
        current = self.head
        stack = []
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        while stack:
            data = stack.pop()
            if current.data != data:
                return False
            current = current.next
        return True


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linkedlist = LinkedList()

linkedlist.append("r")
linkedlist.append("a")
linkedlist.append("d")
linkedlist.append("a")
linkedlist.append("r")

linkedlist.print_list()

print(linkedlist.check_palindrome())
print(linkedlist.check_palindrome_stack())

print(" \n")

linkedlist = LinkedList()

linkedlist.append("n")
linkedlist.append("o")
linkedlist.append("l")
linkedlist.append("e")
linkedlist.append("m")
linkedlist.append("o")
linkedlist.append("n")
linkedlist.append("_")
linkedlist.append("_")
linkedlist.append("n")
linkedlist.append("o")
linkedlist.append("m")
linkedlist.append("e")
linkedlist.append("l")
linkedlist.append("o")
linkedlist.append("n")

linkedlist.print_list()

print(linkedlist.check_palindrome())
print(linkedlist.check_palindrome_stack())
