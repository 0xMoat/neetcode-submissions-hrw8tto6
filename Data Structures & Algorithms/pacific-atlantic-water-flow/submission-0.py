class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res_pac = [[False] * COLS for _ in range(ROWS)]
        res_atl = [[False] * COLS for _ in range(ROWS)]

        source_pac = []
        source_atl = []
        for r in range(ROWS):
            source_pac.append((r, 0))
            source_atl.append((r, COLS - 1))
            res_pac[r][0] = True
            res_atl[r][COLS - 1] = True
        for c in range(COLS):
            source_pac.append((0, c))
            source_atl.append((ROWS - 1, c))
            res_pac[0][c] = True
            res_atl[ROWS - 1][c] = True

        def bfs(source, res):
            q = collections.deque(source)
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < ROWS and 0 <= nc < COLS and \
                        res[nr][nc] == False and res[r][c] == True and \
                        heights[nr][nc] >= heights[r][c]:
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
