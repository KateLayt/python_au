# Array

+ [Move Zeroes](#move-zeroes)

[comment]: <> (Stop)

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

``` python 
 def moveZeroes(self, nums: List[int]) -> None:
    num_of_zeroes = 0
    for num in nums:
        if num == 0:
            nums.remove(0)
            num_of_zeroes += 1
    for i in range(num_of_zeroes):
        nums.append(0)
 ```