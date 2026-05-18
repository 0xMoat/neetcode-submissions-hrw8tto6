class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for i in range(2, len(cost)+1):
            temp = min(cost[i-1]+b, cost[i-2]+a)
            a, b = b, temp
        
        return b