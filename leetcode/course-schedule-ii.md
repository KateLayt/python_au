# LEETCODE

+ [Course Schedule II](#course-schedule-ii)

[comment]: <> (Stop)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

``` python 
 def __init__(self):
    self.visited = []
    self.nodelist = []

def depthsearchfrom(self, node, prerequisites):
    self.visited.append(node)
    for list in prerequisites:
        if list[1] == node and not (list[0] in self.visited):
            self.depthsearchfrom(list[0], prerequisites)

def extendedsearchfrom(self, node, prerequisites):
    for list in prerequisites:
        if list[1] == node:
            if not (list[0] in self.nodelist):
                self.nodelist.append(list[0])
            self.extendedsearchfrom(list[0], prerequisites)

def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    for course in range(numCourses):
        self.visited = []
        self.depthsearchfrom(course, prerequisites)
        if len(self.visited) == numCourses:
            start = course
            self.nodelist.append(start)
            self.extendedsearchfrom(start, prerequisites)
            break
    return self.nodelist
 ```