class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        res = 0

        def dfs(i, j):
            if i >= ROW or i < 0 or j >= COL or j < 0 or grid[i][j] == 0:
                return 0
            
            area = 1
            grid[i][j] = 0
            for dr,dc in direction:
                area += dfs(i+dr, j+dc)
            return area

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    res = max(res, dfs(r, c))
        return res