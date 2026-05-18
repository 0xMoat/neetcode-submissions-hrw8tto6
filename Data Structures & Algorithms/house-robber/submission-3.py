class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        a, b = 0,0
        for n in nums:
            temp = max(a+n, b)
            a, b = b, temp
        return b