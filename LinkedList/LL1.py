"""
# Linked List Vs Array

- Elements of linked list(LL) are independent objects
- Size of LL is not predefined
- Insertion and removals in LL are very efficient
- Random access of an element is very efficient in an array

# Types of LL

- Singly LL
    - In Singly LL, each node stores value and reference to the next node
- Circular Singly LL
    - In Circular LL, last node stores reference to the first node
    - Remaining structure is same as singly LL
- Doubly LL
    - In Doubly LL, each node stores value along with reference to previous node and reference to next node
- Circular Doubly LL
    - In circular doubly LL, first and last node have access to last and first node respectively
    - Remaining structure is same as doubly LL

# How LL are stored in memory?

- Elements of array are stored continously in memory
- Elements of LL are not stored continously in memory
- We have don't have access to intermediate elements in LL, we have to traverse through LL                                                                                                       
"""

# Creation of Singly LL

#1. Create Head and Tail, initialize with null
#2. Create a blank Node and assign a value to it and reference to null
#3. Reference Head and Tail to this node

# class Node():
#     def __inti__(self, value=None):
#         self.value = value
#         self.next = None

# class SLinkedList():
#     def __init__(self):
#         self.head = None
#         self.tail = None

# #intitialize LL
# singlyLinkedList = SLinkedList()
# #create nodes
# node1 = Node(1)
# node2 = Node(2)
# #create link between nodes
# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

"""
# Insertion of Node in Singly LL

1. Insert Node at the begining of LL
   - Initialize a node with a value and reference it to the first Node of LL
   - Change reference of the Head of LL to this newly created Node
2. Insert Node in the middle of LL
    - Initialize a Node with a value and reference it to the next node of previous Node
    - Change reference of previous Node to this newly initialized Node
3. Insert Node to the end of LL
    - Initialize a Node with a value and reference it to null
    - Change reference of Last Node to this newly created Node
    - Change reference of Tail to this newly created Node

Steps for insertion:

1. Create a Node and assign a Value
2. Check if Head is Null ?
    - Yes (it means we are adding first Node in LL)
    - No (we already have nodes present)
3. If Head is not Null, we check for location (first/last/intermediate ?)
    - First: 
        node.next = Head
        Head = node
    - Last:
        node.next = Null
        last.next = node
        tail = node
    - Intermediate:
        Find location (Loop)
        node.next = current.next
        current.next = node
4. If Head is Null
    - node.next = Null
    - Head = node
    - Tail = node
"""

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            elif location < 0:
                self.push(value)
            else:
                prevNode = self.head
                index = 0
                while prevNode.next is not None and index < location-1:
                    prevNode = prevNode.next
                    index += 1
                if prevNode.next is None:
                    self.tail.next = node
                    self.tail = node
                else:
                    node.next = prevNode.next
                    prevNode.next = node
                

# sll = SLinkedList()

# #insert first element
# print("Inserting first element")
# sll.insert(1,10)
# print([node.value for node in sll])

# print("Inserting element 5 at location greater than length of linked list")
# sll.insert(5,10)
# print([node.value for node in sll])

# print("Inserting element 9 at location greater than length of linked list")
# sll.insert(9,10)
# print([node.value for node in sll])

# print("Inserting element 50 at negative location value")
# sll.insert(50,-110)
# print([node.value for node in sll])

# print("Inserting element 99 at start")
# sll.insert(99,0)
# print([node.value for node in sll])

# print("Inserting element 65 at somewhere middle say position 2")
# sll.insert(65,2)
# print([node.value for node in sll])


"""
# Traversal of Single LL

if head:
    node = head
    while node:
        yeild node
        node = node.next
else:
    print("No element found in LL")

# Deleting node from SLL

1. Deleting the first node
    - There is only 1 node in LL
    - There are more than 1 node in LL
2. Deleting any given node
    - 
3. Deleting the last node
    - There is only 1 node in LL
    - There are more than 1 node in LL
"""

class SLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self, value, location):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                self.head = node
            elif location < 0:
                self.push(value)
            else:
                prevNode = self.head
                index = 0
                while prevNode.next is not None and index < location-1:
                    prevNode = prevNode.next
                    index += 1
                if prevNode.next is None:
                    self.tail.next = node
                    self.tail = node
                else:
                    node.next = prevNode.next
                    prevNode.next = node

    def traversalSLL(self):
        if self.head is None:
            print("There are no nodes in Single LL")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def searchSLL(self, value):
        if self.head is None:
            return None
        else:
            node = self.head
            index = 0
            while node:
                if node.value == value:
                    return index
                node = node.next
                index += 1
            return None
    
    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0


sll = SLinkedList()

for i in range(5):
    sll.insert(i,0)

print([node.value for node in sll])
# sll.traversalSLL()

# print(sll.searchSLL(3))
# print(sll.searchSLL(4))
# print(sll.searchSLL(10))

# sll.deleteNode(0)
sll.clear()
print([node.value for node in sll])
print(sll.len)