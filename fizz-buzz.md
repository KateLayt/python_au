# Math

+ [Fizz Buzz](#fizz-buzz)

[comment]: <> (Stop)

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

``` python 
 def fizzBuzz(self, n: int) -> List[str]:
    fizzbuzz_list = []
    for number in range (1, n+1):
        if number % 15 == 0:
            fizzbuzz_list.append("FizzBuzz")
            continue
        elif number % 3 == 0:
            fizzbuzz_list.append("Fizz")
            continue
        elif number % 5 == 0:
            fizzbuzz_list.append("Buzz")
            continue
        else:
            fizzbuzz_list.append(str(number))
    return fizzbuzz_list
 ```
