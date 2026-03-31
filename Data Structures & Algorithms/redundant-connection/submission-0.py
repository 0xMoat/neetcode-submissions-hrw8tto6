class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # N 个节点，初始化父节点指向自己
        parent = [i for i in range(len(edges)+1)]
        # 秩（Rank）优化：用于保持树的平衡, means tree's node
        rank = [1] * (len(edges)+1)

        def find(n):
            """查找根节点 + 路径压缩 (Path Compression)"""
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p


        def union(n1, n2):
            """合并两个节点所在的集合"""
            p1, p2 = find(n1), find(n2)

            # find cycle
            if p1 == p2:
                return False

            # use rank to reduce find time cost
            # increase tree's width rather than height
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True



        for u, v in edges:
            if not union(u, v):
                return [u, v]
        return []

