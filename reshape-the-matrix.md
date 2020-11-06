# Array

+ [Reshape the Matrix](#reshape-the-matrix)

[comment]: <> (Stop)

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

``` python 
 def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    newList = []
    newMatrix = []
    for numList in nums:
        for num in numList:
            newList.append(num)
    if len(newList) != r*c:
        return nums
    c_score = 0
    newLine = []
    for num in newList:
        if c_score == c:
            newMatrix.append(newLine)
            c_score = 0
            newLine = []
        newLine.append(num)
        c_score += 1
    newMatrix.append(newLine)
    return newMatrix
 ```