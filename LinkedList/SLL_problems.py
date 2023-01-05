"""
- In this file we will be solving problems based on Singly Linked List
- In total we will be solving 10 problems
- These 10 problems consist of 5 simple + 3 medium + 2 hard problem type
- We will be referring to geeksforgeeks for problem statement
"""

class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.len = 0
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #insert at the start
                newNode.next = self.head
                self.head = newNode
            elif location < 0: #insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:
                prevNode = self.head
                index = 0
                while index < location-1 and prevNode.next is not None:
                    prevNode = prevNode.next
                    index += 1
                if prevNode.next is None:
                    prevNode.next = newNode
                    self.tail = newNode
                else:
                    newNode.next = prevNode.next
                    prevNode.next = newNode
        self.len += 1

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
    
    def deleteNode(self, location):
        if self.len == 0:
            return None
        elif self.len == 1:
            self.tail = None
            self.head = None
        else:
            if location == 0:
                self.head = self.head.next
            elif location < self.len-1 and location > 0:
                node = self.head
                index = 0
                while index < location - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next
            else:
                node = self.head
                index = 0
                while index < self.len - 2:
                    node = node.next
                    index += 1
                self.tail = node
                node.next = None
        if self.len >= 1:
            self.len -= 1
    
    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0

######## Problem Statement 1: Find the middle of a given linked list (Easy) #########
"""
Given a singly linked list, find the middle of the linked list. 
For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
If there are even nodes, then there would be two middle nodes, 
we need to print the second middle element. 
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4. 
"""
