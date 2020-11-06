# Array

+ [Image Smoother](#image-smoother)

[comment]: <> (Stop)

## Image Smoother

https://leetcode.com/problems/image-smoother/

``` python 
 def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    collumn_len = 0
    line_len = 0
    num_of_elements = 0
    summ_of_elements = 0
    for line in M:
        line_len = len(line)
        collumn_len += 1
    NewMatrix = M
    for line_ind in range(collumn_len):
        for num_ind in range(line_len):
            num_of_elements = 1
            summ_of_elements = M[line_ind][num_ind]
            if line_ind + 1 != collumn_len:
                num_of_elements += 1
                summ_of_elements += M[line_ind+1][num_ind]
            if line_ind + 1 != collumn_len and num_ind + 1 != line_len:
                num_of_elements += 1
                summ_of_elements += M[line_ind+1][num_ind+1]
            if num_ind + 1 != line_len:
                num_of_elements += 1
                summ_of_elements += M[line_ind][num_ind+1]
            if num_ind + 1 != line_len and line_ind - 1 >= 0:
                num_of_elements += 1
                summ_of_elements += M[line_ind - 1][num_ind+1]   
            if line_ind - 1 >= 0:
                num_of_elements += 1
                summ_of_elements += M[line_ind - 1][num_ind]   
            if num_ind - 1 >= 0 and line_ind - 1 >= 0:
                num_of_elements += 1
                summ_of_elements += M[line_ind - 1][num_ind - 1]   
            if num_ind -1 >= 0:
                num_of_elements += 1
                summ_of_elements += M[line_ind][num_ind - 1]   
            if num_ind - 1 >= 0 and line_ind + 1 != collumn_len:
                num_of_elements += 1
                summ_of_elements += M[line_ind + 1][num_ind - 1]   
            NewMatrix[line_ind][num_ind] = summ_of_elements // num_of_elements    
    return NewMatrix
 ```