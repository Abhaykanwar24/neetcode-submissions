# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        lastvisited = None
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack[-1]

            if node.right and lastvisited != node.right:
                cur = node.right
            else:
                res.append(node.val)
                lastvisited = stack.pop()


        return res



