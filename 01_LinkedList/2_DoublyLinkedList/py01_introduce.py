
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linkedlist = LinkedList()

linkedlist.head = Node(1)

secondData = Node(2)
thirdData = Node(3)
fourthData = Node(4)

'''
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
  
    linkedlist.head          second             third
            |                  |                  |
            |                  |                  |
        +----+------+     +----+------+     +----+------+
        | 1  | None |     | 2  | None |     |  3 | None |
        +----+------+     +----+------+     +----+------+
'''

linkedlist.head.next = secondData

'''
    Now next of first Node refers to second.  So they
    both are linked.
  
    linkedlist.head          second            third
            |                  |                 |
            |                  |                 |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  | null |     |  3 | null |
        +----+------+     +----+------+     +----+------+ 
'''

secondData.next = thirdData

'''
    Now next of second Node refers to third.  So all three
    nodes are linked.
  
    linkedlist.head          second            third
            |                  |                 |
            |                  |                 |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  |  o-------->|  3 | null |
        +----+------+     +----+------+     +----+------+ 
'''