
# 222. Count Complete Tree Nodes
use level order traversal

```python

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        node_num = 0
        q = collections.deque()
        q.append(root)
        while q:
            j = len(q)
             
            node_num += j
            for _ in range(j):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return node_num
```

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        return self.getNodeNum(root)
    def getNodeNum(self,node):
        if not node:
            return 0
        
        leftNum = self.getNodeNum(node.left)
        
        rightNum = self.getNodeNum(node.right)
        treeNodeNum=  1+leftNum+ rightNum
        return treeNodeNum
```

# 110. Balanced Binary Tree
```python
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.getHeight(root) == -1:
            return False
        else:
            return True
        # post order traversal, the left node hight and right node hight return to the parent node then the node height = 1+ max(leftHeight, rightHeight)
        # check balance is the balanced = abs(leftHeight - rightHeight) <=1
        # most important thing is to transmit the height to the parent node, and if node sub tree height differenece larger than 1 , treat it as -1
    def getHeight(self,node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        if leftHeight == -1:
            return -1
        rightHeight = self.getHeight(node.right)
        if rightHeight == -1:
            return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
        height = 1+ max(leftHeight, rightHeight)
        return height
        
```

# 257. Binary Tree Paths
```python
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return [] 
        res = []
        path = []
        def dfs(node):
            if not node:
                return
            # append the node when enter the dfs(node)
            path.append(str(node.val))
            # if node is leaf node
            if node.left == None and node.right == None:
                res.append('->'.join(path))
            # if not leaf, keep traversal the left and right
            dfs(node.left)
            dfs(node.right)
            # after the level of dfs is executive, it will pop out the node
            path.pop()
        dfs(root)
        return res
```