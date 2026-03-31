class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            print(visited)
            res += 1
        return res