from typing import List


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
        
    def createloop(self, target_position):
        print("createloop")
        if not self.check_detectloop_set():
            tail = self.head
            while tail and tail.next:
                tail = tail.next
            target = self.head
            for _ in range(target_position):
                if not target:
                    print("<!> over target position")
                    return
                target = target.next
            tail.next = target
            
    # def removeloop_set(self):

            

    def lengthloop_set(self):
        length_linkedlist = 1
        current = self.head
        element = set()
        while current:
            if current in element:
                target = current
                current = self.head
                count = 1
                while current:
                    if current == target:
                        print(length_linkedlist - count)
                        return
                    current = current.next
                    count += 1
            element.add(current)
            current = current.next
            length_linkedlist += 1

    def lengthloop_floydcycle(self):
        if not self.head:
            print("no loop\n")
            return 0
        slow_c = fast_c = self.head
        flag = 0    # to show that both slow and fast are at start of the Linked List
        while slow_c and slow_c.next and fast_c and fast_c.next and fast_c.next.next:
            if slow_c == fast_c and flag != 0:
                count = 1
                slow_c = slow_c.next
                while slow_c != fast_c:
                    slow_c = slow_c.next
                    count += 1
                print(count,end="\n")
                return count
            slow_c = slow_c.next
            fast_c = fast_c.next.next
            flag = 1
        print("no loop\n")
        return 0

    def print_list(self):
        if not self.check_detectloop_set():
            current = self.head
            while current:
                print(current.data, end=" ")
                current = current.next
        print()


linkedlist = LinkedList()

for i in range(4):
    linkedlist.push(i)

linkedlist.print_list()
print(linkedlist.check_detectloop_set())

linkedlist.head.next.next.next.next = linkedlist.head.next

linkedlist.print_list()
print(linkedlist.check_detectloop_set())
linkedlist.lengthloop_set()

linkedlist.head.next.next.next.next = linkedlist.head.next.next
print(linkedlist.check_detectloop_set())
linkedlist.lengthloop_set()

linkedlist.head.next.next.next.next = linkedlist.head.next.next.next
print(linkedlist.check_detectloop_set())
linkedlist.lengthloop_set()


for i in range(5):
    linkedlist.head.next.next.next.next = None
    linkedlist.createloop(i)
    print(linkedlist.check_detectloop_set())
    linkedlist.lengthloop_set()

print("\n= = = = = = = = = = = = = = = = = = = =\n")

for i in range(5):
    linkedlist.head.next.next.next.next = None
    linkedlist.createloop(i)
    print(linkedlist.check_detectloop_set())
    linkedlist.lengthloop_floydcycle()
