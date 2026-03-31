# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_val = p.val
        q_val = q.val

        def dfs(c):
            print("!", c.val)
            if p.val <= c.val <= q.val or q.val <= c.val <= p.val:
                return c

            if c.val > p.val and c.val > q.val:
                return dfs(c.left)
            else:
                return dfs(c.right)
            return

        return dfs(root) 