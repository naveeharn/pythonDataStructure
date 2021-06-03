
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

    def search_data(self, target_position):
        current = self.head
        index = 0
        while current:
            if index == target_position:
                return current.data
            current = current.next
            index += 1
        # assert(False) // syntax error
        return None

    def search_data_recursive(self, start_index, target_position, current):
        if (current is not None) and (start_index == target_position):
            return current.data
        if not current:
            return None
        return self.search_data_recursive(start_index + 1, target_position, current.next)

    def search_data_recursive_short(self, target_position):
        return self.search_data_recursive(0, target_position, self.head)

    def search_data_from_last(self, target_position):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if count < target_position:
            print("Location is greater than length of LinkedList")
            return None
        current = self.head
        for i in range(0,count-target_position):
            current = current.next
        return current.data

    def search_data_middle(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        current = self.head
        for i in range(0,int(count/2)):
            current = current.next
        return current.data

    def search_data_middle_double_pointer(self):
        current = self.head
        middle = self.head
        count = 0
        while current:
            count += 1
            if count%2 == 0:
                middle = middle.next
            current = current.next
        if middle:
            return middle.data
        else:
            return None

    def search_data_frequency(self, target_data):
        current = self.head
        count = 0
        while current:
            if current.data == target_data:
                count += 1
            current = current.next
        return count

    def search_data_frequency_recursive(self, target_data, current):
        if current and current.data == target_data:
            return 1 + self.search_data_frequency_recursive(target_data, current.next)
        if not current:
            return 0
        return self.search_data_frequency_recursive(target_data, current.next)

    def search_data_frequency_recursive_short(self,target_data):
        return self.search_data_frequency_recursive(target_data, self.head)

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

# check data
print(linkedlist.cheak_data(4))
print(linkedlist.cheak_data(10))

print()

# check data with recursive
print(linkedlist.cheak_data_recursive(4, linkedlist.head))
print(linkedlist.cheak_data_recursive_short(4))

print(linkedlist.cheak_data_recursive(10, linkedlist.head))
print(linkedlist.cheak_data_recursive_short(10))

print()

# search data
print(linkedlist.search_data(3))
print(linkedlist.search_data(10))

print()

# search data with recursive
print(linkedlist.search_data_recursive(0, 4, linkedlist.head))
print(linkedlist.search_data_recursive_short(4))

print(linkedlist.search_data_recursive(0, 10, linkedlist.head))
print(linkedlist.search_data_recursive_short(10))

print()

# search data from last node
print(linkedlist.search_data_from_last(4))
print(linkedlist.search_data_from_last(9))
print(linkedlist.search_data_from_last(10))
print(linkedlist.search_data_from_last(11))

print()

# search data middle
linkedlist.print_list()
print(linkedlist.search_data_middle())
print(linkedlist.search_data_middle_double_pointer())
linkedlist.push(10)
print()
linkedlist.print_list()
print(linkedlist.search_data_middle())
print(linkedlist.search_data_middle_double_pointer())

print()

# search frequency of data
linkedlist.push(8)
linkedlist.push(8)
linkedlist.push(4)
print(linkedlist.search_data_frequency(0))
print(linkedlist.search_data_frequency(1))
print(linkedlist.search_data_frequency(4))
print(linkedlist.search_data_frequency(8))

print()

# search frequency of data
print(linkedlist.search_data_frequency_recursive_short(0))
print(linkedlist.search_data_frequency_recursive_short(1))
print(linkedlist.search_data_frequency_recursive_short(4))
print(linkedlist.search_data_frequency_recursive_short(8))