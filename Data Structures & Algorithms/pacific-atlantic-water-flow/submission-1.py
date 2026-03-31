class Solution:
    def pacificAtlantic_BFS(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res_pac = [[False] * COLS for _ in range(ROWS)]
        res_atl = [[False] * COLS for _ in range(ROWS)]

        source_pac = []
        source_atl = []
        for r in range(ROWS):
            source_pac.append((r, 0))
            source_atl.append((r, COLS - 1))
        for c in range(COLS):
            source_pac.append((0, c))
            source_atl.append((ROWS - 1, c))

        def bfs(source, res):
            q = collections.deque(source)
            while q:
                r, c = q.popleft()
                res[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                    res[nr][nc] == False and
                    heights[nr][nc] >= heights[r][c]):
                        q.append((nr, nc))
                        res[nr][nc] = True

        bfs(source_pac, res_pac)
        bfs(source_atl, res_atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if res_pac[r][c] == True and res_atl[r][c] == True:
                    res.append([r, c])

        return res

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        # 使用 set 记录可以到达太平洋和大西洋的坐标
        pac_reachable = set()
        atl_reachable = set()

        def dfs(r, c, reachable):
            # 标记当前点为可达
            reachable.add((r, c))
            
            # 向四个方向扩散
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                # 检查边界
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    # 如果没访问过，且满足“逆流”条件（内陆比沿海高）
                    if (nr, nc) not in reachable and heights[nr][nc] >= heights[r][c]:
                        dfs(nr, nc, reachable)

        # 1. 从左右边界开始 DFS
        for r in range(ROWS):
            # 左边界 -> 太平洋
            dfs(r, 0, pac_reachable)
            # 右边界 -> 大西洋
            dfs(r, COLS - 1, atl_reachable)

        # 2. 从上下边界开始 DFS
        for c in range(COLS):
            # 上边界 -> 太平洋
            dfs(0, c, pac_reachable)
            # 下边界 -> 大西洋
            dfs(ROWS - 1, c, atl_reachable)

        # 3. 找出两个 set 的交集，即为同时能流向两大海域的点
        return list(pac_reachable.intersection(atl_reachable))
