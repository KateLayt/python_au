# String

+ [To Lower Case](#to-lower-case)

[comment]: <> (Stop)

## To Lower Case

https://leetcode.com/problems/to-lower-case/

``` python 
 def toLowerCase(self, str: str) -> str:
    newstr = ''
    for symbol in str:
        if symbol == symbol.upper():
            symbol = symbol.lower()
        newstr += symbol
    return newstr
 ```