class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        held = -prices[0]
        sold = 0
        rest = 0

        for p in prices:
            held,sold,rest = max(rest - p, held), held + p, max(rest, sold)

        return max(sold, rest)