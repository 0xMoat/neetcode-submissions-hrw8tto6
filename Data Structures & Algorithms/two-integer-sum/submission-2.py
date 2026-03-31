class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # map: expect_num -> current_idx
        prev_map = {}
        for i, n in enumerate(nums):
            expect = target - n
            if expect in prev_map:
                return [prev_map[expect], i]
            prev_map[n] = i
        return []