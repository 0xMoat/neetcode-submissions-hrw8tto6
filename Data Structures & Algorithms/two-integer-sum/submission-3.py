class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap: expected part -> index
        expect_dic = {}
        for i,n in enumerate(nums):
            if n in expect_dic:
                return [expect_dic[n], i]
            expect_dic[target - n] = i