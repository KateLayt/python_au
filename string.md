# String

+ [Valid Anagram](#valid-anagram)

[comment]: <> (Stop)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

``` python 
 def isAnagram(self, s: str, t: str) -> bool:
    for symbol in s:
        if not(symbol in t):
            return False
        else:
            for index, found_symbol in enumerate(t):
                if symbol == found_symbol:
                    t = t[:index] + t[index + 1:]
                    break
        if t == '':
            return True
    
            
 ```