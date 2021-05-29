class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while(current != None):
            print(current.data,end=" ")
            current = current.next
        print()

def print_after_node(node):
    current = node

    if(current.data == None):
        current = current.next
    
    while(current != None):
        print(current.data,end=" ")
        current = current.next
    print()


# head in linkedlist
linkedlist = LinkedList()

linkedlist.head = Node(1)

secondData = Node(2)
thirdData = Node(3)
fourthData = Node(4)

linkedlist.head.next = secondData
secondData.next = thirdData
thirdData.next = fourthData

linkedlist.print_list()

print()

print_after_node(linkedlist.head)
print_after_node(secondData)
print_after_node(thirdData)
print_after_node(fourthData)

print()

# head in Node without "currentData = newData"
head = Node(None)
currentData = Node(5)
head.next = currentData
newData = Node(6)
currentData.next = newData
newData = Node(7)
currentData.next = newData
for i in range(8,11):
    newData = Node(i)
    currentData.next = newData
print_after_node(head)

print()

# head in Node with "currentData = newData"
head = Node(None)
newData = Node(5)
head.next = newData
current = head.next

newData = Node(6)
current.next = newData
current = current.next

newData = Node(7)
current.next = newData
current = newData

for i in range(8,10):
    newData = Node(i)
    current.next = newData
    current = current.next

print_after_node(head)

print()