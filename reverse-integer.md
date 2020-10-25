# Math

+ [Reverse Integer](#reverse-integer)

[comment]: <> (Stop)

## Reverse Integer

https://leetcode.com/problems/reverse-integer/

``` python 
 def reverse(self, x: int) -> int:
    size = 1
    ifminus = False
    while x > size:
        size *= 10
    if x != size:
        size = size//10
    if x < 0:
        ifminus = True
    reversed_x = 0
    while x != 0:
        reversed_x += (x % 10)*size
        size = size // 10
        x = x // 10
    if ifminus:
        reversed_x *= -1
    return(reversed_x)
 ```
