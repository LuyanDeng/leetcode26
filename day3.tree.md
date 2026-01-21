# 226. Invert Binary Tree

```python

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```
### use level order and queue
iterate each level's node, swap the left and right child, push left and right child to the q,

```python
 if root == None:
            return root
        q = collections.deque()
        q.append(root)
        while q:
            
            level_size = len(q)
            # iterate each level each node, swap the left and right child
            for i in range(level_size):
                node = q.popleft()
                node.left, node.right =  node.right, node.left
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
```


## 101. Symmetric Tree

to test if the left subtree can convert to right subtree, and each node.val is same
To determine if a tree is symmetric, we examine the the left subtree and right subtree, because the root symmetric to itself.
if left is null, right not null, false
if right is null, left not null, false
left and right not null: left.val == right.val 
and we assume that a function isMirror(left, right) can tell you that ture and false
so node left.left is mirror to right.right; node left.right is mirror to right.left

```python
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left,right):
            if not right and not left:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left,right.right) and isMirror(left.right, right.left)
        return isMirror(root.left, root.right) if root else True
        

```   
# 104

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def getHeight(node):
            if not node:
                return 0
            leftHeight = getHeight(node.left)
            rightHeight =  getHeight(node.right)
            maxHeight = 1+ max(leftHeight, rightHeight)
            return maxHeight
        return getHeight(root)
```

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q =collections.deque()
        depth = 0
        q.append(root)

        
        while q:
            
            
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth
```


# 111. Minimum Depth of Binary Tree
the best way is to use level order traversal to find the minimum depth. 
In each iteration, the algorithm check each pop out node, if it has no left and right child, then return the depth of that level. if the node has left or right child, will continue iteration entire level, and move to next level

```python

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # initial depth value to 0
        depth = 0 
        # set a queue and add the root into it
        q = collections.deque()
        q.append(root)

        while q:
            depth +=1

            # iterate each level
            for _ in range(len(q)):
                # store each pop up node
                node = q.popleft()
                # check each node's children
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return depth

```

# 559. Maximum Depth of N-ary Tree
```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
            # if has node, the current depth is 1
        max_depth = 1
            # children depth set to 0 
        max_children_depth =0
            # iterate each child's depth
        for child in root.children:
            child_depth = self.maxDepth(child)
            if child_depth >max_children_depth:
                max_children_depth = child_depth
        return 1+max_children_depth
```
```python
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
            # if has node, the current depth is 1
        max_depth =0
        q = collections.deque()
        q.append(root)
        while q:
            max_depth +=1
            j = len(q)
           
            for i in range(j):
                node = q.popleft()
                for child in node.children:
                    q.append(child)
        return max_depth
```