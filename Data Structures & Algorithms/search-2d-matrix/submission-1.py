class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            idx = l + (r - l) // 2
            mr, mc = idx // COLS, idx % COLS
            if matrix[mr][mc] > target:
                r = idx - 1
            elif matrix[mr][mc] < target:
                l = idx + 1
            else:
                return True
        
        return False