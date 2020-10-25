# String

+ [Reverse Words in a String III](#reverse-words-in-a-string-iii)

[comment]: <> (Stop)

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

``` python 
 def reverseWords(self, s: str) -> str:
    WordList = s.split(' ')
    Reversed_string = ''
    new_word = ''
    for word in WordList:
        new_word = list(word)
        for index in range(len(new_word)//2):
            new_word[index], new_word[len(new_word) - index - 1] = new_word[len(new_word) - index - 1], new_word[index]
            #поменять местами
        for symbol in new_word:
            Reversed_string += symbol
        if word != WordList[len(WordList) - 1]:
            Reversed_string += ' '            
    return Reversed_string
 ```
