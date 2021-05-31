
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

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def cheak_data(self, target_data):
        current = self.head
        while current:
            if current.data is target_data:
                return True
            current = current.next
        return False

    def cheak_data_recursive(self, target_data, current):
        if(current is not None) and (current.data == target_data):
            return True
        if(not current):
            return False
        return self.cheak_data_recursive(target_data, current.next)

    def cheak_data_recursive_short(self, targrt_data):
        return self.cheak_data_recursive(targrt_data, self.head)

    def search_position(self, target_position):
        current = self.head
        index = 0
        while current:
            if index == target_position:
                return current.data
            current = current.next
            index += 1
        # assert(False)
        return None

    def search_position_recursive(self, start_index, target_position, current):
        if (current is not None) and (start_index == target_position):
            return current.data
        if not current:
            return None
        return self.search_position_recursive(start_index + 1, target_position, current.next)

    def search_position_recursive_short(self, target_position):
        return self.search_position_recursive(0, target_position, self.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linkedlist = LinkedList()

for i in range(0, 10):
    linkedlist.push(i)
linkedlist.print_list()

print(linkedlist.cheak_data(4))
print(linkedlist.cheak_data(10))

print()

print(linkedlist.cheak_data_recursive(4, linkedlist.head))
print(linkedlist.cheak_data_recursive_short(4))

print(linkedlist.cheak_data_recursive(10, linkedlist.head))
print(linkedlist.cheak_data_recursive_short(10))

print()

print(linkedlist.search_position(3))
print(linkedlist.search_position(10))

print()

print(linkedlist.search_position_recursive(0, 4, linkedlist.head))
print(linkedlist.search_position_recursive_short(4))

print(linkedlist.search_position_recursive(0, 10, linkedlist.head))
print(linkedlist.search_position_recursive_short(10))
