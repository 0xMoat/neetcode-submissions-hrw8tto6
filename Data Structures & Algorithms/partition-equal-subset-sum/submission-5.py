class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0-1 背包，item放外层，cap内层逆序
        sumNums = sum(nums)
        if sumNums % 2 == 1:
            return False

        target = sumNums // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i-num]

        return dp[-1]