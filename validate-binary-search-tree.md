# Tree

+ [Validate Binary Search Tree](#validate-binary-search-tree)

[comment]: <> (Stop)

## Validate Binary Search Tree

https://leetcode.com/problems/validate-binary-search-tree/

``` python 
 def isValid(self, node, interval):
    if node != None:
        if node.val < interval[1] and node.val >  interval[0] and self.isValid(node.right, [node.val, interval[1]]) and self.isValid(node.left, [interval[0], node.val]):
            return True
        else:
            return False
    return True
    
def isValidBST(self, root: TreeNode) -> bool:
    return self.isValid(root, [-2**100, 2**100])
 ```