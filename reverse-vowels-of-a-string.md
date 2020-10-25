# String

+ [Reverse Vowels of a String](#reverse-vowels-of-a-string)

[comment]: <> (Stop)

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

``` python 
 def reverseVowels(self, s: str) -> str:
    Vowels = ['a','e','i','o','u']
    word_vowels = []
    for symbol in s:
        if symbol in Vowels:
            word_vowels.append(symbol)
    for index in range(len(word_vowels)//2):
        word_vowels[index], word_vowels[len(word_vowels) - index - 1] = word_vowels[len(word_vowels) - index - 1], word_vowels[index]
    num_of_vowel = 0
    new_s = ''
    for symbol in s:
        if symbol in Vowels:
            new_s += word_vowels[num_of_vowel]
            num_of_vowel += 1
        else:
            new_s += symbol
    return new_s
 ```
