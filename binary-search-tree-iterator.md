# Tree

+ [Binary Search Tree Iterator](#binary-search-tree-iterator)

[comment]: <> (Stop)

## Binary Search Tree Iterator

https://leetcode.com/problems/binary-search-tree-iterator/

``` python 
 def __init__(self, root: TreeNode):
    self.inorderList = self.inorderTraversal(root)
    self.ind = 0
    
def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root == None:
        return []
    TravList = []
    if root.left != None:
        TravList += self.inorderTraversal(root.left)
    TravList.append(root.val)
    if root.right != None:
        TravList += self.inorderTraversal(root.right)
    return TravList

def next(self) -> int:
    if self.hasNext():
        self.ind += 1
        return self.inorderList[self.ind - 1]
    else:
        return 0
        
def hasNext(self) -> bool:
    if self.ind >= len(self.inorderList):
        return False
    return True
 ```