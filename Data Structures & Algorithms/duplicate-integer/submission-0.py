class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = set()
        for n in nums:
            if n not in dic:
                dic.add(n)
            else:
                return True
        return False