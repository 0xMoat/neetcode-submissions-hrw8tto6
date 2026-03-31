class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        res = 0
        # 为什么不会漏掉，因为时间是连续的，
        # 在某个时间点之前，随着时间流逝，我们一直更新最低点，更新可能的最大收益，就一定是最终能获得的最大收益
        for i in range(len(prices)):
            if prices[i] <= prices[buy_idx]:
                buy_idx = i
            else:
                res = max(res, prices[i] - prices[buy_idx])
        return res