# Linked List

+ [Linked List Cycle](#linked-list-cycle)

[comment]: <> (Stop)

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

``` python 
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
