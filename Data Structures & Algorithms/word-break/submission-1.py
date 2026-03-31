class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # dp[idx] means whether the string start with idx can be break
        dp = [False] * (n + 1)
        dp[-1] = True # this is a dumb item, can be consider as end of string

        for i in range(n, -1, -1):
            for word in wordDict:
                if i+len(word) <= n and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]