class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        maxProduct, minProduct = 1, 1
        for n in nums:
            candidates = (n, maxProduct*n, minProduct*n)
            maxProduct = max(candidates)
            minProduct = min(candidates)

            res = max(res, maxProduct)

        return res