+ [Reverse Linked List](#)

+ [Middle of the Linked List](#)

+ [Palindrome Linked List](#)

+ [Merge Two Sorted Lists](#)

+ [Remove Nth Node From End of List](#)

+ [Linked List Cycle II](#)

+ [Linked List Cycle](#)

+ [Intersection of Two Linked Lists](#)

[comment]: <> (Stop)

#Intersection of Two Linked Lists

Problem 160. <a href="https://leetcode.com/problems/intersection-of-two-linked-lists/">Link to the page </a>

``` pytnon 
 def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    secondA = headA
    secondB = headB
    ListA = []
    ListB = []
    node = None
    while headA:
        ListA.append(headA.val)
        headA = headA.next
    while headB:
        ListB.append(headB.val)
        headB = headB.next
    if len(ListA) > len(ListB):
        for i in range(len(ListA) - len(ListB)):
            secondA = secondA.next
    if len(ListB) > len(ListA):
        for i in range(len(ListB) - len(ListA)):
            secondB = secondB.next
    while secondA and secondB:
        if secondA.next == secondB.next:
            node = secondA.next
            break
        secondA = secondA.next
        secondB = secondB.next
    return(node)
 ```
#Linked List Cycle

Problem 141. <a href="https://leetcode.com/problems/linked-list-cycle/">Link to the page </a>

``` pytnon 
 def hasCycle(self, head: ListNode) -> bool:
    List = []
    sectime = 0
    n1 = 0 
    n2 = 0
    while head:
        if head.val in List:
            sectime = head.val
            while head:
                if head.val == sectime:
                    while head:
                        if head.val == sectime:
                            if n1 == n2:
                                return(True)
                        n2 += 1
                        head = head.next
                n1 += 1
                head = head.next
        List.append(head.val)
        head = head.next
    return(False)
 ```
#Linked List Cycle II

Problem 142. <a href="https://leetcode.com/problems/linked-list-cycle-ii/">Link to the page </a>

``` pytnon 
 def detectCycle(self, head: ListNode) -> ListNode:
    List = []
    sectime = 0
    n1 = 0 
    n2 = 0
    while head:
        if head.val in List:
            sectime = head.val
            while head:
                if head.val == sectime:
                    while head:
                        if head.val == sectime:
                            if n1 == n2:
                                return(head)
                        n2 += 1
                        head = head.next
                n1 += 1
                head = head.next
        List.append(head.val)
        head = head.next
    return(None)
 ```
#Remove Nth Node From End of List

Problem 19. <a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list/">Link to the page </a>

``` pytnon 
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
#Merge Two Sorted Lists

Problem 21. <a href="https://leetcode.com/problems/merge-two-sorted-lists/">Link to the page </a>

``` pytnon 
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
#Palindrome Linked List

Problem 234. <a href="https://leetcode.com/problems/palindrome-linked-list/">Link to the page </a>

``` pytnon 
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
#Middle of the Linked List

Problem 876. <a href="https://leetcode.com/problems/middle-of-the-linked-list/">Link to the page </a>

``` pytnon 
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
#Reverse Linked List

Problem 206. <a href="https://leetcode.com/problems/reverse-linked-list/">Link to the page </a>

``` pytnon 
 def reverseList(self, head: ListNode) -> ListNode:
    NewList = None
    while head:
        NewList = ListNode(head.val,NewList)
        head = head.next
    return(NewList)
 ```
