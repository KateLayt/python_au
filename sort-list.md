# Linked List

+ [Sort List](#sort-list)

[comment]: <> (Stop)

## Sort List

https://leetcode.com/problems/sort-list/

``` python 
     newlist = secondlist
    if type(firstlist) is int:
        if type(secondlist) is int:
            if firstlist < secondlist:
                return [firstlist, secondlist]
            else:
                return [secondlist, firstlist]
        else:
            start = 0
            end = len(firstlist) - 1
            while True:
                if firstlist > secondlist[start]:
                    start += 1
                else:
                    newlist.insert(start, firstlist)
                    break
                if firstlist < secondlist[end]:
                    end -= 1
                else:
                    newlist.insert(end, firstlist)
                    break
    else:
        for element in firstlist:
            start = 0
            end = len(secondlist) - 1
            while True:
                if element > secondlist[start]:
                    start += 1
                else:
                    newlist.insert(start, element)
                    break
                if element < secondlist[end]:
                    end -= 1
                else:
                    if len(newlist) > end + 1:
                        newlist.insert(end + 1, element)
                    else:
                        newlist.append(element)
                    break
    return newlist

sortList(self, head: ListNode) -> ListNode:
    ValList = []
    NewList = []
    while head:
        ValList.append(head.val)
        head = head.next
    while len(ValList) != 1:
        for i in range(len(ValList)//2):
            NewList.append(self.sortsorted(ValList[i], ValList[len(ValList) - i - 1]))
        if len(ValList)%2 != 0:                
            NewList.append(self.sortsorted(NewList[0], ValList[len(ValList)//2 + 1]))
            del NewList[0]
        ValList = NewList
        NewList = []
    NewList = ValList[0]
    NodeList = None
    for j in range(len(NewList)- 1,-1,-1):
        NodeList = ListNode(NewList[j], NodeList)
    return NodeList
 ```