# Math

+ [Fibonacci Number](#fibonacci-number)

[comment]: <> (Stop)

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

``` python 
 def fib(self, N: int) -> int:
    if N < 2:
        return N
    else:
        return self.fib(N - 1) + self.fib(N - 2)
 ```