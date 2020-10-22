# String

+ [Reverse String](#reverse-string)

[comment]: <> (Stop)

## Reverse String

https://leetcode.com/problems/reverse-string/

``` python 
 def reverseString(self, s: List[str]) -> None:
    for index in range(len(s)//2):
        s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]
 ```