class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if (len1 + len2) != len(s3):
            return False

        # dp[i][j] represents whether s1[:i] and s2[:j] can be formed to interleaving string 
        dp = [[False]*(len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True

        for i in range(1, len1+1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, len2+1):
            dp[0][j] = dp[0][j-1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len1+1):
            for j in range(1, len2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or (dp[i][j-1] and s2[j-1] == s3[j-1+i])

        return dp[len1][len2]


    def isInerleave(self, s1, s2, s3):
        len1, len2 = len(s1), len(s2)
        if (len1 + len2) != len(s3):
            return False

        dp = [False] * (len2 + 1)
        dp[0] = True
        for j in range(1, len2 + 1):
            dp[j] = dp[j-1] and s2[j - 1] == s3[j - 1]

        for i in range(1, len1 + 1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, len2 + 1):
                up = dp[j] and s1[i-1] == s3[i-1+j]
                left = dp[j-1] and s2[j-1] == s3[j-1+i]
                dp[j] = up or left

        return dp[len2]






