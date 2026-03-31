# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        q = collections.deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                node.left, node.right = node.right, node.left
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return root

    def invertTree(self, root):
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        
        return root

