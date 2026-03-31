class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        res = 0
        for i in range(len(prices)):
            if prices[i] <= prices[buy_idx]:
                buy_idx = i
            else:
                res = max(res, prices[i] - prices[buy_idx])
        return res