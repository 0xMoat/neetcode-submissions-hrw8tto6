class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        one, two, res = nums[0], max(nums[0], nums[1]), 0
        for i in range(2, n):
            temp = max(one + nums[i], two)
            one, two = two, temp
        return two