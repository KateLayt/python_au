# -*- coding: utf-8 -*-
print("Введите имя файла решения: ")
filename = input()
print("Введите имя файла .md: ")
output = input()
print("Введите имя группы задач (Intervals, Lists):")
tasktype = input()
file=open(filename, "r")
code=[]
number = ''
title = ''
ifdot = False
firstline = file.readline()
firstline = firstline[1:]
for symb in firstline:
    if symb != '.' and ifdot != True:
        number += symb
    if symb == '.':
        ifdot = True
        number += symb
    if symb != '.' and ifdot == True:
        title += symb
http = file.readline()
http = http[1:]
file.readline()
string=file.readline()
while(string != ""):
    code.append(string)
    string=file.readline()
words = title.split()
newtitle = ''
for word in words:
    newtitle += word.lower() + '-'
newtitle = newtitle[:-1]
file.close()
file_output=open(output, "a")
file_output.write('\n---\n')
file_output.write('## {}\n'.format(title.rstrip()))
file_output.write('<h5> Problem {} <a href="{}">Link to the page </a><br></h5>\n'.format(number,http.rstrip()))
file_output.write('\n```python\n')
for item in code:
    file_output.write(item.rstrip() + '\n')
file_output.write('```\n')
file_output.close()
afterfile = open(output, 'r')
data =[] 
data.append('<a href = "#{}">{}</a><br>\n'.format(newtitle,title.strip()))
line = afterfile.readline()
while line != "":
    data.append(line)
    line = afterfile.readline()
afterfile.close()
file_output_after=open(output, "w")
file_output_after.write('<h1>{}</h1><br>\n'.format(tasktype))
for line in data:
    if not('<h1>' in line):
        file_output_after.write(line)
file_output_after.close()
