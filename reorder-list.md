# Linked List

+ [Reorder List](#reorder-list)

[comment]: <> (Stop)

## Reorder List

https://leetcode.com/problems/reorder-list/

``` python 
     ListNode_List = []
    while head:
        ListNode_List.append(head)
        head = head.next
    start = 0 
    end = len(ListNode_List) - 1
    while start < end:
        ListNode_List[start].next = ListNode_List[end]
        ListNode_List[end].next = ListNode_List[start + 1]
        end -= 1
        start += 1
    if len(ListNode_List)%2 == 0:
        ListNode_List[start].next = None
    else:
        ListNode_List[end].next = None
 ```