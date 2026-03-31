class Solution:
    def jump_BFS_greedy(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res

    def jump(self, nums):
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0
        
        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i, end):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]


