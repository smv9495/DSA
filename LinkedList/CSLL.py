"""
In Circular Single Linked List, tail.next reference to head
"""

class Node():
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class CSLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def push(self, value):
        node = Node(value)
        # true while inserting first node
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
            return
        # inserting after first node
        node.next = self.head
        self.tail.next = node
        self.tail = node
    def pop(self, location=-1):
        # c1: LL is empty
        if self.head is None:
            return
        # c2: LL have only 1 node
        if self.head == self.tail:
            self.tail.next = None
            self.head = None
            self.tail = None
            return
        # c3: LL have more than 1 node
            # a: location = 0
        if location == 0:
            self.head = self.head.next
            self.tail = self.head
            # b: loaction = -1
        if location == -1:
            prevNode = self.head
            while True:
                if prevNode.next == self.tail:
                    break
                prevNode = prevNode.next
            prevNode.next = self.head
            self.tail = prevNode
            return
            # c: location = intermediate
        prevNode = self.head
        index = 0
        while index < location - 1:
            if prevNode.next == self.tail:
                prevNode.next = self.head
                self.tail = prevNode
                return
            prevNode = prevNode.next
        prevNode.next = prevNode.next.next
    def insert(self, value, location):
        node = Node(value)
        # case 1: LL is empty
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = self.head
            return
        # case 2: LL have atleast 1 node
        # case 2a: location is 0
        if location == 0:
            self.tail.next = node
            node.next = self.head
            self.head = node
            return
        # case 2a: location is -1 (insert at last)  
        if location == -1:
            self.push(value)
            return
        # case 3a: insert anywhere in the middle
        prevNode = self.head
        index = 0
        while index < location - 1 and prevNode.next != self.head:
            prevNode = prevNode.next
            index += 1
        # case 3aa: prevNode is the last node
        if prevNode.next == self.head:
            self.push(value)
        else: # case 3ab: prevNode is not the last node
            node.next = prevNode.next
            prevNode.next = node

if __name__ == '__main__':
    csll = CSLinkedList()
    print([node.value for node in csll])
    for i in range(2):
        csll.insert(i, 0)
    print([node.value for node in csll])
    csll.pop(2)
    print([node.value for node in csll])