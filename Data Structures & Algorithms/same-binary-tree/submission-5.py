# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def preorder(node):
            res = []

            def dfs(node):
                if not node:
                    res.append(None)
                    return
                res.append(node.val)      # 👈 root FIRST
                dfs(node.left)
                dfs(node.right)

            dfs(node)
            return res

        return preorder(p) == preorder(q)

            
