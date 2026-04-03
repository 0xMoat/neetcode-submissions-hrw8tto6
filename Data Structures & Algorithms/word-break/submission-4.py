class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n + 1)
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                wl = len(word)
                if wl <= i and s[i-wl:i] == word and dp[i-wl]:
                    dp[i] = True
                    break
        return dp[-1]