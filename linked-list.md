<h1>Lists</h1><br>
<a href = "#remove-nth-node-from-end-of-list">Remove Nth Node From End of List</a><br>
<a href = "#merge-two-sorted-lists">Merge Two Sorted Lists</a><br>
<a href = "#palindrome-linked-list">Palindrome Linked List</a><br>
<a href = "#middle-of-the-linked-list">Middle of the Linked List</a><br>
<a href = "#reverse-linked-list">Reverse Linked List</a><br>

---
##  Reverse Linked List
<h5> Problem 206. <a href="https://leetcode.com/problems/reverse-linked-list/">Link to the page </a><br></h5>

```python
    def reverseList(self, head: ListNode) -> ListNode:
        NewList = None
        while head:
            NewList = ListNode(head.val,NewList)
            head = head.next
        return(NewList)
```

---
##  Middle of the Linked List
<h5> Problem 876. <a href="https://leetcode.com/problems/middle-of-the-linked-list/">Link to the page </a><br></h5>

```python
    def middleNode(self, head: ListNode) -> ListNode:
        List = []
        secondhead = head
        HeadNode = None
        NewHeadNode = None
        n = 0
        while head:
            List.append(head.val)
            head = head.next
        Remains = int(len(List)/2 + len(List)%2*0.5) - 1
        while secondhead:
            if n >= Remains:
                HeadNode = ListNode(secondhead.val, HeadNode)
            n += 1
            secondhead = secondhead.next
        while HeadNode:
            NewHeadNode = ListNode(HeadNode.val, NewHeadNode)
            HeadNode = HeadNode.next
        return(NewHeadNode)
```

---
##  Palindrome Linked List
<h5> Problem 234. <a href="https://leetcode.com/problems/palindrome-linked-list/">Link to the page </a><br></h5>

```python
    def isPalindrome(self, head: ListNode) -> bool:
        string = []
        while head:
            string.append(head.val)
            head = head.next
        Is = True
        for i in range(len(string)):
            if string[i] != string[len(string) - i - 1]:
                Is = False
        return(Is))
```

---
##  Merge Two Sorted Lists
<h5> Problem 21. <a href="https://leetcode.com/problems/merge-two-sorted-lists/">Link to the page </a><br></h5>

```python
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        List1 = []
        List2 = []
        ReversedMergedListNode = None
        MergedListNode = None
        while l1:
            List1.append(l1.val)
            l1 = l1.next
        while l2:
            List2.append(l2.val)
            l2 = l2.next
        MergedList = []
        n1 = 0
        n2 = 0
        while n1 < len(List1) and n2 < len(List2):
            if List1[n1] < List2[n2]:
                MergedList.append(List1[n1])
                n1 += 1
            elif List1[n1] > List2[n2]:
                MergedList.append(List2[n2])
                n2 += 1
            elif List1[n1] == List2[n2]:
                MergedList.append(List1[n1])
                n1 += 1
                MergedList.append(List2[n2])
                n2 += 1
        while n1 < len(List1):
            MergedList.append(List1[n1])
            n1 += 1
        while n2 < len(List2):
            MergedList.append(List2[n2])
            n2 += 1
        for element in MergedList:
            ReversedMergedListNode = ListNode(element, ReversedMergedListNode)
        while ReversedMergedListNode:
            MergedListNode = ListNode(ReversedMergedListNode.val, MergedListNode)
            ReversedMergedListNode = ReversedMergedListNode.next
        return(MergedListNode)
```

---
##  Remove Nth Node From End of List
<h5> Problem 19. <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">Link to the page </a><br></h5>

```python
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        List = []
        ReversedNewHead = None
        NewHead = None
        while head:
            List.append(head.val)
            head = head.next
        del List[-n]
        for element in List:
            ReversedNewHead = ListNode(element, ReversedNewHead)
        while ReversedNewHead:
            NewHead = ListNode(ReversedNewHead.val, NewHead)
            ReversedNewHead = ReversedNewHead.next
        return(NewHead)
```
