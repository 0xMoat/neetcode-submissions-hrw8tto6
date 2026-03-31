class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, node):
        cur = node
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        # print(u, v, self.parent, self.rank)
        return True
class Solution:
    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        adj_dic = { i:[] for i in range(n)}
        for u, v in edges:
            adj_dic[u].append(v)
            adj_dic[v].append(u)

        visited = set()
        def dfs(curr):
            visited.add(curr)
            for n in adj_dic[curr]:
                if n not in visited:
                    dfs(n)

        res = 0
        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            res += 1
        return res

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res