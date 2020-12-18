# Tree

+ [Binary Tree Inorder Traversal](#binary-tree-inorder-traversal)

[comment]: <> (Stop)

## Binary Tree Inorder Traversal

https://leetcode.com/problems/binary-tree-inorder-traversal/

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
 ```