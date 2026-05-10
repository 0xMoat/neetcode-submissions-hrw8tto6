class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res is left_product * right_product
        n = len(nums)
        res = [1] * len(nums)
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

