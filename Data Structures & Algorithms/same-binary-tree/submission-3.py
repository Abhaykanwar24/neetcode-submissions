# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inorder(node):
            res = []

            def dfs(node):
                if not node:
                    res.append(None)
                    return
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)

            dfs(node)
            return res

        return inorder(q) == inorder(p)

            
