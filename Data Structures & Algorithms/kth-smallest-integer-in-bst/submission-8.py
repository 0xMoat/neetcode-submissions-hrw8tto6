# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = None
        self.k = k

        def dfs(node):
            if not node or self.res is not None:
                return

            # BST 第 k 小 = 中序遍历第 k 个，因为中序天然递增。
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.res

