# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            if not node:
                return depth

            left_max = dfs(node.left, depth + 1)
            right_max = dfs(node.right, depth + 1)
            return max(left_max, right_max)

        return dfs(root, 0)
            