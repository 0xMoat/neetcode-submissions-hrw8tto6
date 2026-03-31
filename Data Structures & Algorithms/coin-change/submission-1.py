class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        dp[0] = 0
        min_coin = min(coins)
        for i in range(min_coin, amount+1):
            fewest = float("inf")
            for c in coins:
                if i-c >= 0 and dp[i-c] >= 0:
                    fewest = min(fewest, dp[i-c]+1)
            dp[i] = fewest if fewest != float("inf") else -1
        print(dp)
        return dp[-1]