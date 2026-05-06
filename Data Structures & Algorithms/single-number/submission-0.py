class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res_check = set()
        for n in nums:
            if n in res_check:
                res_check.remove(n)
            else:
                res_check.add(n)
        return list(res_check)[0]