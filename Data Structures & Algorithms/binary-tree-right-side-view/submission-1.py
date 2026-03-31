# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        while q:
            rightSide = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide)
        return res

    def rightSideView(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res