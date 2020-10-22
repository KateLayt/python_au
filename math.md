# Math

+ [Sqrt(x)](#sqrtx)

[comment]: <> (Stop)

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

``` python 
 def mySqrt(self, x: int) -> int:
    n = 0
    while x > n*n:
        n += 1
    if x != n**2:
        return n - 1
    return n
 ```