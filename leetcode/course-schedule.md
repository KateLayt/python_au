# LEETCODE

+ [Course Schedule](#course-schedule/submissions)

[comment]: <> (Stop)

## Course Schedule

https://leetcode.com/problems/course-schedule/submissions/

``` python 
 def __init__(self):
    self.examing = []
    self.alreadyTested = []
    

def canBeVisited(self, node, pres, nums):
    if node in self.alreadyTested:
        return True
    for pre in pres:
        if node == pre[0]:
            if not(pre[1] in self.examing):
                self.examing.append(node)
                if not(self.canBeVisited(pre[1], pres, nums)):
                    return False
            else:
                return False
    self.examing = []
    self.alreadyTested.append(node)
    return True


def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    if prerequisites == []:
        return True
    for pre in prerequisites:
        if pre[0] == pre[1]:
            return False
    for num in range(numCourses):
        if not(self.canBeVisited(num, prerequisites, numCourses)):
            return False
    return True
 ```