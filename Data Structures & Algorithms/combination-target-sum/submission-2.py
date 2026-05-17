class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combin = []

        def dfs(i, count):
            if count == target:
                res.append(combin.copy())
                return
            
            if i > len(nums)-1 or count > target:
                return

            combin.append(nums[i])
            dfs(i, nums[i]+count)
            combin.pop()
            dfs(i+1, count)

        dfs(0,0)
        return res
