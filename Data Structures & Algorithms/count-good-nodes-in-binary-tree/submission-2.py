# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def DFS(node ,maxValue):
            if not node:
                return 0

            res = 1 if node.val >= maxValue else 0
            maxValue = max(maxValue , node.val)
            res += DFS(node.left , maxValue)
            res += DFS(node.right , maxValue)

            return res


        return DFS(root,root.val)
        

        