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