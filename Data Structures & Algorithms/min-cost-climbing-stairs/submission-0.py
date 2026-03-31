class Solution:
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        # dp array represents the minimum cost to reach step i
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp [i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]    
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(2, len(cost)+1):
            temp = min(one + cost[i-2], two + cost[i-1])
            one, two = two, temp

        return two