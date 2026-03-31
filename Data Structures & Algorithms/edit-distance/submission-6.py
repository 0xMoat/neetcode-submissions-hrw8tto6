class Solution:
    def minDistance_classic(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] = 将 word1[:i] 转换为 word2[:j] 的最少操作数
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Base cases
        for i in range(m+1):
            dp[i][0] = i # delete all word1 characters
        for j in range(n+1):
            dp[0][j] = j # insert all word2 characters

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j], # delete last word1 char
                        dp[i][j-1], # insert last word2 char at the end of word1
                        dp[i-1][j-1] #replace last word1 char
                    )

        return dp[m][n]


    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        prev = [0] * (n+1)

        # Base cases
        for j in range(n+1):
            prev[j] = j # insert all word2 characters

        for i in range(1, m+1):
            curr = [i] + [0] * n  # curr[0] = i（全删除）
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(
                        prev[j],
                        curr[j-1],
                        prev[j-1],
                    )
            prev = curr
        return prev[n]