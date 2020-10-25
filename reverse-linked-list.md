# Linked List

+ [Reverse Linked List](#reverse-linked-list)

[comment]: <> (Stop)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

``` python 
 def reverseList(self, head: ListNode) -> ListNode:
    NewList = None
    while head:
        NewList = ListNode(head.val,NewList)
        head = head.next
    return(NewList)
 ```
