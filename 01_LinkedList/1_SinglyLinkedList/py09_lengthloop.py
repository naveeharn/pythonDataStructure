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
