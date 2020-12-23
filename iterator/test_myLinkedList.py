import unittest
from myLinkedList import MyLinkedList

class TestMyLinkedList(unittest.TestCase):
    def test_get(self):
        a = MyLinkedList()
        a.addAtHead(1)
        a.addAtHead(2)
        a.addAtHead(3)
        expect = 2
        result = a.get(1)
        self.assertEqual(expect, result)

    def test_str(self):
        a = MyLinkedList()
        a.addAtHead(1)
        a.addAtHead(2)
        a.addAtHead(3)
        expect = "3<->2<->1"
        result = str(a)
        self.assertEqual(expect, result)

    def test_addAtTail(self):
        a = MyLinkedList()
        a.addAtHead(1)
        a.addAtHead(2)
        a.addAtHead(3)
        b = MyLinkedList()
        b.addAtTail(3)
        b.addAtTail(2)
        b.addAtTail(1)
        expect = str(a)
        result = str(b)
        self.assertEqual(expect, result)
    
    def test_addAtIndex(self):
        a = MyLinkedList()
        a.addAtHead(1)
        a.addAtHead(2)
        a.addAtHead(3)
        a.addAtIndex(2,3)
        expect = "3<->2<->3<->1"
        result = str(a)
        self.assertEqual(expect, result)

    def test_deleteAtIndex(self):
        a = MyLinkedList()
        a.addAtHead(1)
        a.addAtHead(2)
        a.addAtHead(3)
        a.deleteAtIndex(1)
        expect = "3<->1"
        result = str(a)
        self.assertEqual(expect, result)

if __name__ == "__main__":
    unittest.main()
