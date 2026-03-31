class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        length1, length2 = len(text1), len(text2)
        # add dumb row & column, boundary: empty texts LCS = 0
        # dp represents LCS of two texts start from idx to end
        dp = [[0]* (length2 + 1) for _ in range(length1 + 1)]

        for i in range(length1 - 1, -1, -1):
            for j in range(length2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]
