class Solution:
    def coinChange2(self, coins: List[int], amount: int) -> int:
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

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1+dp[i-c])

        return -1 if dp[amount] == amount+1 else dp[amount]