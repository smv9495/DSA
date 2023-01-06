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

class solution1():
    def find_middle_node(self, head):
        if head is None:
            return
        
        slow_node = head
        fast_node = head
        while fast_node.next is not None and fast_node.next.next is not None:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
        return slow_node.value

######## Problem Statement 2: Count of number of Linked List (Easy) #########
"""
Given a singly linked list and a key, 
count the number of occurrences of the given key in the linked list. 
For example, if the given linked list is 1->2->1->2->1->3->1 
and the given key is 1, then the output should be 4.
"""
class solution2():
    def count(self, sll, key):
        count = 0
        node = sll.head
        while node:
            if node.value == key:
                count += 1
            node = node.next
        return count
        
######## Problem Statement 3: Check if given LL is Circular (Easy) #########
"""
A linked list is called circular 
if it is not NULL-terminated and all nodes are connected in the form of a cycle. 
Below is an example of a circular linked list.
"""
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
        tempNode = self.head
        while True:
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next
        tempNode.next = node
        node.next = self.head
        self.tail = node

class solution3():
    def isCircular(self, ll):
        node = ll.head
        while node:
            if node.next == ll.head:
                return 1
            node = node.next
        return 0

######## Problem Statement 4: Count nodes in Circular linked list (Easy) #########
"""
Given a circular linked list, count the number of nodes in it. 
For example, the output is 5 for the below list. 
"""
class solution4():
    def count_nodes(self, cll):
        node = cll.head
        count = 0
        while node:
            count += 1
            if node.next == cll.head:
                break
            node = node.next
        return count

######## Problem Statement 5: Convert Singly LL into Circular LL (Easy) #########
"""
Given a singly linked list, 
we have to convert it into circular linked list. 
For example, 
we have been given a singly linked list with four nodes 
and we want to convert this singly linked list into circular linked list.
"""
class solution5():
    def isCircular(self, ll):
        node = ll.head
        while node:
            if node.next == ll.head:
                return 1
            node = node.next
        return 0

    def sll_to_cll(self, ll):
        if ll.head is None:
            return ll
        if not self.isCircular(ll):
            node = ll.head
            while node.next:
                node = node.next
            node.next = ll.head
        return ll

if __name__ == '__main__':
    sll = SLinkedList()
    cll = CSLinkedList()
    for i in range(10):
        sll.push(i%3)
        cll.push(i)
    
    print([node.value for node in sll])
    print([node.value for node in cll])

    print(solution1().find_middle_node(sll.head))
    print(solution2().count(sll, 4))
    print(solution3().isCircular(sll))
    print(solution3().isCircular(cll))
    print(solution4().count_nodes(cll))
    print("Before")
    print(f"Is circular: {solution3().isCircular(sll)}")
    print("After converting")
    sll = solution5().sll_to_cll(sll)
    print(f"Is circular: {solution3().isCircular(sll)}")