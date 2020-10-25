# Linked List

+ [Linked List Cycle II](#linked-list-cycle-ii)

[comment]: <> (Stop)

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

``` python 
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
