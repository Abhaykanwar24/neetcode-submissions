# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_result = []

        def DFS_right(currNode, depth):
            if not currNode:
                return None
            
            if depth == len(right_result):
                right_result.append(currNode.val)
                
            DFS_right(currNode.right, depth + 1)
            DFS_right(currNode.left, depth + 1)

        DFS_right(root , 0)
        
        return right_result