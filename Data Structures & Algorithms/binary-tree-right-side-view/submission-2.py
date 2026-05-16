# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        while q:
            length = len(q)
            right_side = None
            for _ in range(length):
                node = q.popleft()
                if node:
                    right_side = node.val
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                res.append(right_side)

        return res