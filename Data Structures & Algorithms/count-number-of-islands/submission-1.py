class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = collections.deque([(r,c)])
            grid[r][c] = "0"
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr not in range(ROWS) or nc not in range(COLS) or grid[nr][nc] == "0":
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    bfs(r, c)

        return res

            