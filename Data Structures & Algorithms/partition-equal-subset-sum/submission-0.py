class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1 or s == nums[0]:
            return False
        target = s // 2
        dp = set()
        dp.add(0) # add initial dumb sum value - 0
        for n in nums:
            new_dp = set()
            for dp_item in dp:
                if dp_item + n == target:
                    return True
                new_dp.add(dp_item)
                new_dp.add(dp_item + n)
            dp = new_dp
        return True if target in dp else False