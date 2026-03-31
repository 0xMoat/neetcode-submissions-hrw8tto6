# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        res = []
        while q:
            layer = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    layer.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if layer:
                res.append(layer)
        return res

    def levelOrderDFS(self, root):
        res = []

        def dfs(node, depth):
            if not node:
                return
            # only when it visits the depth first time, res will add a new list space 
            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return res
