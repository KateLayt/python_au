# Linked List

+ [Palindrome Linked List](#palindrome-linked-list)

[comment]: <> (Stop)

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

``` python 
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