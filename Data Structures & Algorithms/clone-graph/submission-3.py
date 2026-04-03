"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}
        
        def dfs(cur):
            if cur in oldToNew:
                return oldToNew[cur]  # ✅ 修正这里 cur 而不是 node

            oldToNew[cur] = Node(cur.val)
            for nei in cur.neighbors:
                oldToNew[cur].neighbors.append(dfs(nei))
            return oldToNew[cur]


        return dfs(node)