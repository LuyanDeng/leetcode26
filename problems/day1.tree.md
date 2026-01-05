# 144. Binary Tree Preorder Traversal
### Recursive Method
preorder Traversal: node - left subtree- right subtree
and in the subtree remain the same order
that means, the algorithsm 
1. visit root, 
2. visit left subtree
3. visit right subtree
use curr as the pointer, use an array arr to store the visited nodes

if the curr is None, means the recursion should stop.
```python

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def dfs(curr, arr):
            if curr == None:
                return
            arr.append(curr.val)
            dfs(curr.left, arr)
            dfs(curr.right, arr)
        dfs(root,arr)
        return arr


```
### iteration
we use stack to emulate the resurrsion, 
1. push the node(root) to the stack
2. pop it and add the value to the res arr
3. push the node right and then node left, becasue later the stack will pop the left node first 
```python
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

```
# 145. Binary Tree Postorder Traversal

```python
   def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr =[]
        def dfs(curr, arr):
            if curr == None:
                return
            dfs(curr.left, arr)
            dfs(curr.right, arr)
            arr.append(curr.val)
        dfs(root, arr)
        return arr

```

### iteration -- two stacks
```python
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        s1=[root]
        s2 = []
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
            
            
        return [node.val for node in reversed(s2)]

```
# 94. Binary Tree Inorder Traversal

```python
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def dfs(curr, arr):
            if curr == None:
                return
            dfs(curr.left, arr)
            arr.append(curr.val)
            dfs(curr.right, arr)
        dfs(root, arr)
        return arr

```