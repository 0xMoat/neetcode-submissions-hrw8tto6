class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        visited = [False] * len(nums)
        def dfs(depth):
            if depth == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                permutation.append(nums[i])
                visited[i] = True
                dfs(depth+1)

                permutation.pop()
                visited[i] = False
        dfs(0)
        return res