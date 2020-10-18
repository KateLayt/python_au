# Linked List

+ [Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

[comment]: <> (Stop)

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

``` python 
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