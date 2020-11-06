# Array

+ [Transpose Matrix](#transpose-matrix)

[comment]: <> (Stop)

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

``` python 
 def transpose(self, A: List[List[int]]) -> List[List[int]]:
    collumn_num = 0
    line_num = 0
    for line in A:
        collumn_num = len(line)
        line_num += 1
    NewMatrix = []
    for collumn_ind in range(collumn_num):
        NewLine = []
        for line_ind in range(line_num):
            NewLine.append(A[line_ind][collumn_ind])
        NewMatrix.append(NewLine)
    return NewMatrix
 ```