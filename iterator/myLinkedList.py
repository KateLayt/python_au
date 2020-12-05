class Node:
    def __init__(self, prev = None,val = 0, next = None):
        self.val = val
        self.next = next
        self.prev = prev
  
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return
        curr_node = self.head
        for i in range(0, index):
            curr_node = curr_node.next
        return curr_node.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        if self.head == None:
            self.head = Node(None, val)
            self.tail = self.head
            return
        self.head = Node(None, val, self.head)
        self.head.next.prev = self.head

    def addAtTail(self, val: int) -> None:
        self.size += 1
        if self.head == None:
            self.head = Node(None, val)
            self.tail = self.head
            return
        self.tail = Node(self.tail, val)
        self.tail.prev.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return 
        if index == self.size:
            self.addAtTail(val)
            return
        self.size += 1
        curr_node = self.head
        for i in range(0, index - 1):
            curr_node = curr_node.next
        curr_node.next = Node(curr_node, val, curr_node.next)

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        self.size -= 1
        if index == 0:
            if self.head == self.tail:
                self.head, self.tail = None, None
                return
            self.head = self.head.next
            self.head.prev = None
            return 
        if index == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
            return
        curr_node = self.head
        for i in range(0, index):
            curr_node = curr_node.next
        tmp_node = curr_node
        curr_node = curr_node.prev
        curr_node.next = tmp_node.next

    def __str__(self):
        string = ""
        curr_node = self.head
        while curr_node != None:
            string += str(curr_node.val) + "<->"
            curr_node = curr_node.next
        string = string[:-3]
        return string
