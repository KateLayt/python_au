# Math

+ [Palindrome Number](#palindrome-number)

[comment]: <> (Stop)

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

``` python 
 def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    size = 1
    while x > size:
        size *= 10
    if x != size:
        size = size//10
    reversed_x = 0
    safe_x = x
    while x != 0:
        reversed_x += (x % 10)*size
        size = size // 10
        x = x // 10
    if safe_x == reversed_x:
        return True
    else:
        return False
 ```
