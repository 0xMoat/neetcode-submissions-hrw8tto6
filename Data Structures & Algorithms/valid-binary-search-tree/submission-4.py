# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left_check, node, right_check):
            if not node:
                return True
            
            if left_check < node.val < right_check:
                return dfs(left_check, node.left, node.val) and dfs(node.val, node.right, right_check)
            else:
                return False

        return dfs(float('-inf'), root, float('inf'))