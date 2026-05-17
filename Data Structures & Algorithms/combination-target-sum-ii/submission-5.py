class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combin = []

        nums.sort()

        def dfs(i, count):
            if count == target:
                res.append(combin.copy())
                return
            
            if i >= len(nums) or count > target:
                return

            combin.append(nums[i])
            dfs(i+1, nums[i]+count)
            combin.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, count)

        dfs(0,0)
        return res
