class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 初始值 = 第0天执行该状态对应操作后的真实收益
        held = -prices[0]#第0天唯一能进入 held 的方式是买入，花了钱所以是负数
        sold = 0 # 第0天逻辑上不可能刚卖完（没买过），理论值是 -∞，但因为它只被 rest 的转移用到，而 rest 初始已经是 0，所以写 0 不影响结果
        rest = 0 #第0天什么都不做，收益就是 0

        for p in prices[1:]:
            held,sold,rest = max(rest - p, held), held + p, max(rest, sold)

        return max(sold, rest)