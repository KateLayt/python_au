# Array

+ [Squares of a Sorted Array](#squares-of-a-sorted-array)

[comment]: <> (Stop)

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

``` python 
     NewList = []
    for number in A:
        NewList.append(number**2)
    NewList = sorted(NewList)
    return NewList
 ```