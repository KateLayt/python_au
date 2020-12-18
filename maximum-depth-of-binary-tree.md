# Tree

+ [Maximum Depth of Binary Tree](#maximum-depth-of-binary-tree)

[comment]: <> (Stop)

## Maximum Depth of Binary Tree

https://leetcode.com/problems/maximum-depth-of-binary-tree/

``` python 
 def maxDepth(self, root: TreeNode) -> int:
    if root == None:
        return 0        
    rightd,leftd = 0,0
    if root.right != None:
        rightd = self.maxDepth(root.right)
    if root.left != None:
        leftd = self.maxDepth(root.left)
    return max(rightd, leftd) + 1
 ```