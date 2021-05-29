# LEETCODE

+ [Course Schedule II](#course-schedule-ii)

[comment]: <> (Stop)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

``` python 
    def __init__(self):
        self.examing = []
        self.alreadyTested = []
        self.canBeFirst = []
        self.orderedArray = []
        

    def canBeVisited(self, node, pres, nums):
        if node in self.alreadyTested:
            return True
        for pre in pres:
            if node == pre[0]:
                if node in self.canBeFirst:
                    self.canBeFirst.remove(node)
                if not(pre[1] in self.examing):
                    self.examing.append(node)
                    if not(self.canBeVisited(pre[1], pres, nums)):
                        return False
                else:
                    return False
        self.examing = []
        self.alreadyTested.append(node)
        return True
 
 
    def depthSearch(self, node, pres):
        self.orderedArray.append(node)
        for pre in pres:
            canAdd = True
            if pre[1] == node:
                for newpre in pres:
                    if (pre[0] == newpre[0]) and not(newpre[1] in self.orderedArray):
                        canAdd = False
                        break
                if canAdd:
                    self.depthSearch(pre[0], pres)
                    
                
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
       
       
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.canBeFirst = [node for node in range(numCourses)]
        if not(self.canFinish(numCourses, prerequisites)):
            return []
        for node in self.canBeFirst:
            if not(node in self.orderedArray):
                self.depthSearch(node, prerequisites)
        return self.orderedArray
 ```
