class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        # total + target must be even
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        # 问题变成：从数组里选一些数，使它们的和等于 P，有多少种选法？
        # 这就是 0-1 背包的组合计数问题
        capacity = (total + target) // 2
        dp = [0] * (capacity + 1)
        dp[0] = 1

        for num in nums:
            for i in range(capacity, num -1, -1):
                dp[i] += dp[i-num]

        return dp[capacity]