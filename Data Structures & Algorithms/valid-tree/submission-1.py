class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: all node connected, and no cycle
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * (n)

        def find(n):
            while n != parent[n]:
                # compress parent retrieve path
                parent[n] = parent[parent[n]]
                n = parent[n]
            return n

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # find cycle
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u, v in edges:
            if not union(u, v):
                return False
        return True