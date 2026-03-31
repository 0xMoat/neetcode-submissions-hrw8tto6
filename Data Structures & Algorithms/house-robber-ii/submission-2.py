class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.dpHelper(nums[:-1]), self.dpHelper(nums[1:]))

    def dpHelper(self, nums):
        one, two = 0, 0
        for num in nums:
            temp = max(one + num, two)
            one, two = two, temp
        return two
