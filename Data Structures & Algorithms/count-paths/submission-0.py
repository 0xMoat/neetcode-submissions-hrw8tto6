class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[0][0] = 1
                else:
                    left = dp[i][j-1] if j >= 1 else 0
                    up = dp[i-1][j] if i >= 1 else 0
                    dp[i][j] = left + up
        print(dp,m,n)
        return dp[m-1][n-1]
