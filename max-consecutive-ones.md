# Array

+ [Max Consecutive Ones](#max-consecutive-ones)

[comment]: <> (Stop)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

``` python 
 def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    max_cons = 0
    curr_cons = 0
    for num in nums:
        if num == 1:
            curr_cons += 1
        else:
            if curr_cons > max_cons:
                max_cons = curr_cons
            curr_cons = 0
    if curr_cons > max_cons:
        max_cons = curr_cons
    return max_cons
 ```