# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = collections.deque([root])
        res = []

        while q:
            current_level = []
            for _ in range(len(q)):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(current_level)
        return res


    def levelOrder(self, root):
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
