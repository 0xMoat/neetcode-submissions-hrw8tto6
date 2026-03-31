class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 以第 i 个元素结尾的连续子数组的最大和
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i]=max(nums[i], nums[i]+dp[i-1])
        return max(dp)
