# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, leftCheck, rightCheck):
            if not node:
                return True

            if leftCheck < node.val < rightCheck:
                return dfs(node.left, leftCheck, node.val) and dfs(node.right, node.val, rightCheck)
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))