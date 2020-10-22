# Linked List

+ [Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

[comment]: <> (Stop)

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

``` python 
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