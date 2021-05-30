
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

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def search_data(self, target_data):
        current = self.head
        while current:
            if current.data is target_data:
                return True
            current = current.next
        return False

    def search_data_recursive(self, target_data, current):
        if(current is not None) and (current.data == target_data):
            return True
        if(not current):
            return False
        return self.search_data_recursive(target_data, current.next)

    def search_data_recursive_short(self, targrt_data):
        return self.search_data_recursive(targrt_data, self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()
        
linkedlist = LinkedList()

for i in range(0,10):
    linkedlist.push(i)
linkedlist.print_list()

print(linkedlist.search_data(4))
print(linkedlist.search_data(10))

print()

print(linkedlist.search_data_recursive(4, linkedlist.head))
print(linkedlist.search_data_recursive_short(4))

print(linkedlist.search_data_recursive(10, linkedlist.head))
print(linkedlist.search_data_recursive_short(10))
