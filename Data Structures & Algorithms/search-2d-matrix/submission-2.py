class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            val = matrix[m // COLS][m % COLS]
            if val == target:
                return True
            elif val > target:
                r = m - 1
            else:
                l = m + 1

        return False