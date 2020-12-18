# Array

+ [Flipping an Image](#flipping-an-image)

[comment]: <> (Stop)

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

``` python 
 def ReverseLine(self,line):
    l = len(line)
    for num_ind in range(l//2):
        line[num_ind], line[l - num_ind - 1] = line[l - num_ind - 1], line[num_ind]
    return line
def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    line_len = 0
    collumn_len = 0
    for line in A:
        line_len = len(line)
        collumn_len += 1
    for line_ind in range(collumn_len):
        for num_ind in range(line_len):
            if A[line_ind][num_ind] == 0:
                A[line_ind][num_ind] = 1
                continue
            else:
                A[line_ind][num_ind] = 0
    for line in A:
        line = self.ReverseLine(line)
    return A
 ```