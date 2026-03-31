class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if (r + dr) in range(ROWS) and (c + dc) in range(COLS) and grid[r + dr][c + dc] == 2147483647:
                        grid[r + dr][c + dc] = step
                        q.append((r + dr, c + dc))
        
