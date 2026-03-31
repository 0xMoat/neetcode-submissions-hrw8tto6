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

        root, processed = Node(1), {}

        def dfs(curr_node, neighbors):
            if not neighbors or curr_node.val in processed:
                return

            processed[curr_node.val] = curr_node
            for n in neighbors:
                new_neighbor = Node(n.val) if n.val not in processed else processed[n.val]
                curr_node.neighbors.append(new_neighbor)
                dfs(new_neighbor, n.neighbors)
        
        dfs(root, node.neighbors)
        return root

