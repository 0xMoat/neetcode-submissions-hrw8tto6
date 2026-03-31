class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []

        def dfs(i):
            if i >= len(nums):
                res.add(tuple(sorted(path[:])))
                return
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)

        dfs(0)
        return list(res)