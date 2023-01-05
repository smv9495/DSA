"""
- In this file we will be solving problems based on Singly Linked List
- In total we will be solving 10 problems
- These 10 problems consist of 5 simple + 3 medium + 2 hard problem type
- We will be referring to geeksforgeeks for problem statement
"""

######## Problem Statement 1: Find the middle of a given linked list (Easy) #########
"""
Given a singly linked list, find the middle of the linked list. 
For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 
If there are even nodes, then there would be two middle nodes, 
we need to print the second middle element. 
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4. 
"""

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, value):
        """
        add node at the end of the LL
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
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

    def find_middle_node(self, head):
        if head is None:
            return
        
        slow_node = head
        fast_node = head
        while fast_node.next is not None and fast_node.next.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node.value

if __name__ == '__main__':
    sll = SLinkedList()
    for i in range(4):
        sll.push(i)
    
    print([node.value for node in sll])

    print(sll.find_middle_node(sll.head))