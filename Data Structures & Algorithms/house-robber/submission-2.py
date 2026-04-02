class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n] = max( dp[n-1], dp[n-2]+nums[n-1])
        
        a, b = 0, 0
        for n in nums:
            temp = max(b, a + n)
            a, b = b, temp
        return b