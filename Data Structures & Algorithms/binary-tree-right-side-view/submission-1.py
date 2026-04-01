# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def DFS_right(node , depth):
            if not node:
                return None

            if depth == len(res):
                res.append(node.val)

            DFS_right(node.right , depth + 1)
            DFS_right(node.left , depth + 1)

        DFS_right(root , 0)
        return res
