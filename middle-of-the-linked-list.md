# Linked List

+ [Middle of the Linked List](#middle-of-the-linked-list)

[comment]: <> (Stop)

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

``` python 
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
