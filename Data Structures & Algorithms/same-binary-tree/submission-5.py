# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTreeDFS(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSameTree(self, p, q):
        q1 = collections.deque([p])
        q2 = collections.deque([q])

        while q1 and q2:
            q1_node = q1.popleft()
            q2_node = q2.popleft()

            if not q1_node and not q2_node:
                continue

            if q1_node and q2_node and q1_node.val == q2_node.val:
                q1.append(q1_node.left)
                q1.append(q1_node.right)
                q2.append(q2_node.left)
                q2.append(q2_node.right)
            else:
                return False

        return True
        
