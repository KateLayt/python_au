# Math

+ [Base 7](#base-7)

[comment]: <> (Stop)

## Base 7

https://leetcode.com/problems/base-7/

``` python 
 def convertToBase7(self, num: int) -> str:
    ifminus = False
    if num < 0:
        ifminus = True
    size = 1
    new_num = 0
    while num != 0:
        new_num += (num % 7)*size
        size *= 10
        num //= 7
    if ifminus:
        new_num *= -1
    return str(new_num)
 ```
