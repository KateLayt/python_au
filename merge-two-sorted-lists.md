# Linked List

+ [Merge Two Sorted Lists](#merge-two-sorted-lists)

[comment]: <> (Stop)

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

``` python 
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
