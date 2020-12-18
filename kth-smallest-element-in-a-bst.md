# Tree

+ [Kth Smallest Element in a BST](#kth-smallest-element-in-a-bst)

[comment]: <> (Stop)

## Kth Smallest Element in a BST

https://leetcode.com/problems/kth-smallest-element-in-a-bst/

``` python 
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

def kthSmallest(self, root: TreeNode, k: int) -> int:
    TreeList = self.inorderTraversal(root)
    return TreeList[k - 1]
 ```