class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        expected_dic = {}
        for i,n in enumerate(nums):
            if n in expected_dic:
                return [expected_dic[n], i]
            expected_dic[target-n] = i
        return