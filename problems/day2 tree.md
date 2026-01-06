## 102. Binary Tree Level Order Traversal
use a queue to iterate by level. 
1. push the nodes of current level to the queue
2. keep the size of the current level
3. iterate the current level's nodes, visit one node, pop, and add the node's left and right child to the queue
```python
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if root == None:
        return []
    q = collections.deque()
    q.append(root)
    res = []

    while q:
        s = len(q)
        level = [] # the array that strone current level of nodes
        for i in range(s):
            node = q.popleft()
            if node:
                level.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res

```

## 107. Binary Tree Level Order Traversal II
很容易混淆level 这个数组应该在哪里开始，要这样想里面的for 循环代表的是每次iterate 一层，同时加入这次层node 的孩子，所以iterate 完这一层，level 就要清空，然后开始存下一层的node.
```python
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            s = len(q)
            #iterate the current level
            for i in range(s):
                #pop up each node
                node = q.popleft()
                # store it in the level 
                level.append(node.val)
                # add the node's left, right child
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res[::-1]
```
