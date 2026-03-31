class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = set()

        def dfs(depth):
            if depth >= len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in visited:
                    path.append(nums[i])
                    visited.add(nums[i])
                    dfs(depth+1)
                    path.pop()
                    visited.remove(nums[i])

        dfs(0)
        return res

            

                
