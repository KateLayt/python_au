# Math

+ [Largest Perimeter Triangle](#largest-perimeter-triangle)

[comment]: <> (Stop)

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

``` python 
 def largestPerimeter(self, A: List[int]) -> int:
    three_biggest = []
    if len(A) ==  3:
        three_biggest = A
    else:
        three_biggest = sorted(A)[-3:]
    if three_biggest[0] >= three_biggest[1] + three_biggest[2]:
        return 0
    if three_biggest[1] >= three_biggest[0] + three_biggest[2]:
        return 0
    if three_biggest[2] >= three_biggest[1] + three_biggest[0]:
        return 0
    return (three_biggest[0] + three_biggest[1] + three_biggest[2])
 ```
