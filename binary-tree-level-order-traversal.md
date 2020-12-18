# Tree

+ [Binary Tree Level Order Traversal](#binary-tree-level-order-traversal)

[comment]: <> (Stop)

## Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/

``` python 
 def levelOrder(self, root):
    if root == None:
        return []
    ordered_list = []
    currLevel = [root]    
    while currLevel != []:
        nextLevel, currNodes = [], []
        for node in currLevel:
            currNodes.append(node.val)
            if node.left != None:
                nextLevel.append(node.left)
            if node.right != None:
                nextLevel.append(node.right)
        ordered_list.append(currNodes)
        currLevel = nextLevel       
    return ordered_list
 ```