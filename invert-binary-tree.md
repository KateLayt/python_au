# Tree

+ [Invert Binary Tree](#invert-binary-tree)

[comment]: <> (Stop)

## Invert Binary Tree

https://leetcode.com/problems/invert-binary-tree/

``` python 
 def invertTree(self, root: TreeNode) -> TreeNode:
    if root == None:
        return None
    root.right, root.left = root.left, root.right
    self.invertTree(root.right)
    self.invertTree(root.left)
    return root
    
 ```