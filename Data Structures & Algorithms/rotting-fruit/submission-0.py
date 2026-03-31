class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = collections.deque()
        ROW, COL = len(grid),len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        res = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q and fresh > 0:
            # level iteration
            res += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for rd, cd in directions:
                    if 0 <= (r + rd) <= ROW - 1 and 0 <= (c + cd) <= COL - 1 and grid[r + rd][c + cd] == 1:
                        q.append((r+rd,c+cd))
                        grid[r + rd][c + cd] = 2
                        fresh -= 1

        return res if fresh == 0 else -1