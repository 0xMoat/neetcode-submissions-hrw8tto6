class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map: expect_num -> current_idx
        expect_dic = {}
        for i, n in enumerate(nums):
            expect = target - n
            if n in expect_dic:
                return [expect_dic[n], i]
            expect_dic[expect] = i
            print(expect_dic)
        return []