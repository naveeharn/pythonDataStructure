import sys
print(sys.getrecursionlimit())


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

    def delete_node_data(self, target_data):
        current = self.head
        if (current is not None) and (current.data == target_data):
            self.head = current.next
            current = None
            return

        while(current.data != target_data):
            previous = current
            current = current.next

        previous.next = current.next
        current = None
    
    def delete_node_position(self, target_position):
        if self.head is None:
            print("not element in Linked List")
            return

        previous = self.head
        
        if target_position == 0:
            self.head = previous.next
            previous = None
            return
        
        for i in range(target_position - 1):
            previous = previous.next
            if previous is None:
                break

        if (previous is None) or (previous.next is None):
            print("not target position in Linked List")
            return 
        
        next = previous.next.next
        previous.next = None
        previous.next = next
        
    def _delete_node_position(self, target_position):
        if(target_position < 0):
            print("target position in Linked List must not negative number")
            return
        index = 0
        current = self.head
        if(current is not None) and (target_position == 0):
            self.head = current.next
            current = None
            return

        while(target_position != index):
            previous = current
            current = current.next
            index += 1

        if(current is None):
            print("not target position in Linked List")
            return

        previous.next = current.next
        current = None

    def delete_node_data_recursive(self, target_data, current):
        if (current is not None) and (current.data == target_data):
            print("(current is not None) and (current.data == target_data)")
            self.head = current.next
            current = None
            return
        previous = current
        current = current.next
        if(current.data == target_data):
            print("(current.data == target_data)")
            previous.next = current.next
            current = None
            return
        print("recursive")
        return self.delete_node_data_recursive(target_data, current)

    def print_list(self):
        current = self.head
        while(current):
            print(current.data, end=" ")
            current = current.next
        print()


linkedlist = LinkedList()

for i in range(1, 10):
    linkedlist.push(i)

linkedlist.print_list()

linkedlist.delete_node_data(3)

linkedlist.print_list()

linkedlist.delete_node_position(-2)

linkedlist.delete_node_position(8)

linkedlist.delete_node_position(7)

linkedlist.print_list()

linkedlist.delete_node_data_recursive(2, linkedlist.head)

linkedlist.print_list()

linkedlist.delete_node_data_recursive(5, linkedlist.head)

linkedlist.print_list()

linkedlist.delete_node_data_recursive(9, linkedlist.head)

linkedlist.print_list()
