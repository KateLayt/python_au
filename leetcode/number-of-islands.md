# LEETCODE

+ [Number of Islands](#number-of-islands)

[comment]: <> (Stop)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

``` python 
class Solution:
    def __init__(self):
        self.alreadyExplored = []
        
    def exploreIsland(self, node, grid):
        if node in self.alreadyExplored:
            return
        self.alreadyExplored.append(node)
        if node[0] > 0:
            if grid[node[0] - 1][node[1]] == '1':
                self.exploreIsland([node[0] - 1, node[1]], grid)
        if node[1] > 0:
            if grid[node[0]][node[1] - 1] == '1':
                self.exploreIsland([node[0], node[1] - 1], grid)
        if node[0] < len(grid) - 1:
            if grid[node[0] + 1][node[1]] == '1':
                self.exploreIsland([node[0] + 1, node[1]], grid)
        if node[1] < len(grid[0]) - 1:
            if grid[node[0]][node[1] + 1] == '1':
                self.exploreIsland([node[0], node[1] + 1], grid)
                                
        
    def numIslands(self, grid: List[List[str]]) -> int:
        islnum = 0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == '1' and not([j, i] in self.alreadyExplored):
                    self.exploreIsland([j, i], grid)
                    islnum += 1
        return islnum
```