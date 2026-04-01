class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i] = True

                dfs()

                path.pop()
                visited[i] = False

        dfs()
        return res
                

            

                
