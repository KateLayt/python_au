# Tree

+ [Symmetric Tree](#symmetric-tree)

[comment]: <> (Stop)

## Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

``` python 
 def isSymNodes(self,first, second):
    if first != None or second != None:
        if first == None or second == None:
            return False
        if first.val != second.val or not(self.isSymNodes(first.right, second.left)) or not(self.isSymNodes(first.left, second.right)):
            return False
    return True

def isSymmetric(self, root):
    return self.isSymNodes(root, root)
 ```