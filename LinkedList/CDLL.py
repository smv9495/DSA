class DNode():
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev

class CDLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next
            if node == self.head:
                break
    
    def reverse(self):
        node = self.tail
        while node:
            yield node.value
            node = node.prev
            if node == self.tail:
                break

    def push(self, value, start=False):
        node = DNode(value)
        
        # case1: LL is empty
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = self.tail
            node.next = self.head
            return
        # case2: LL has only 1 node
        if self.head == self.tail:
            if not start:
                self.head.next = node
                node.prev = self.head
                node.next = self.head
                self.tail = node
                self.head.prev = self.tail
                return
            else:
                node.next = self.tail
                node.prev = self.tail
                self.tail.next = node
                self.tail.prev = node
                self.head = node
                return
        # case3: LL has more than 1 node
        if not start:
            prevNode = self.tail
            prevNode.next = node
            node.prev = prevNode
            node.next = self.head
            self.tail = node
            self.head.prev = self.tail
        else:            
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.prev = self.tail
            self.tail.next = self.head


    def pop(self, start=False):
        # case1: LL is empty
        if self.head is None:
            return
        # case2: LL has only 1 element
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        # case3: LL has more than 1 element
        if not start:
            prevNode = self.tail.prev
            prevNode.next = self.head
            self.tail = prevNode
            self.head.prev = self.tail
        else:
            nextNode = self.head.next
            self.head = nextNode
            self.head.prev = self.tail
            self.tail.next = self.head

if __name__ == '__main__':
    CDLL = CDLinkedList()
    for i in range(5):
        CDLL.push(i, start=True)

    print([node for node in CDLL])
    print([node for node in CDLL.reverse()])

    for i in range(2):
        CDLL.pop(start=True)

    print([node for node in CDLL])
    print([node for node in CDLL.reverse()])
    if CDLL.head is not None:
        print(f"Head: {CDLL.head.value}")
        print(f"Tail: {CDLL.tail.value}")