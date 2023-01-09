class DNode():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
    
    def reverse(self):
        node = self.tail
        while node:
            yield node.value
            node = node.prev
            
    def push(self, value):
        node = DNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def pop(self):
        # check if LL is empty
        if self.tail is not None:
            node = self.tail.prev
            # check if LL have only 1 node
            if node is not None:
                node.next = None
                self.tail = node
            else:
                self.head = None
                self.tail = None

    def insert(self, value, location):
        node = DNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if location == 0:
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        if location == -1:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            return
        prevNode = self.head
        index = 0
        while index < location-1:
            prevNode = prevNode.next
            index += 1
            if prevNode is None:
                node.prev = prevNode
                prevNode.next = node
                self.tail = prevNode
                return
        node.prev = prevNode
        node.next = prevNode.next
        prevNode.next.prev = node
        prevNode.next = node
    def search(self, value):
        if self.head is None:
            return None
        node = self.head
        index = 0
        while node:
            if node.value == value:
                return index
            node = node.next
            index += 1

    def delete(self, location):
        if self.head is None:
            return
        if self.head == self.tail and (location==0 or location==-1):
            self.head = None
            self.tail = None
            return
        if location == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        if location == -1:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        prevNode = self.head
        index = 0
        while index < location - 1:
            if prevNode == self.tail:
                return  
            prevNode = prevNode.next
            index += 1
        if prevNode == self.tail:
            pass
        else:
            prevNode.next = prevNode.next.next
            prevNode.next.prev = prevNode
    def clear(self):
        self.head = None
        self.tail = None


if __name__ == '__main__':
    DLL = DLinkedList()
    for i in range(5):
        DLL.push(i)
    print([node for node in DLL])
    # DLL.pop()
    # print([node for node in DLL])
    # DLL.insert(99,3)
    # DLL.insert(101,0)
    # DLL.insert(102,1)
    # DLL.insert(116,-1)
    # print([node for node in DLL])
    # print([node for node in DLL.reverse()])
    # print(DLL.search(0))
    DLL.delete(1)
    print([node for node in DLL])
    DLL.clear()
    print([node for node in DLL])