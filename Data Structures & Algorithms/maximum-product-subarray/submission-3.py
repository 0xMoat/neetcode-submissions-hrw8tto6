class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min, cur_max = 1, 1
        for n in nums:
            tmp = cur_max * n
            cur_max = max(n, tmp, cur_min*n)
            cur_min = min(n, tmp, cur_min*n)
            res = max(res, cur_max)
        return res